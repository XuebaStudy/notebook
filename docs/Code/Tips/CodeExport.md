# 提取目录下文件结构与所有文件内容 (Windows PowerShell)

!!! abstract
    - “我现在有一个里面有比较复杂的文件结构的项目，我想要把整个项目的代码发给 GPT 看一下，解决问题，但是这样必须得一点一点的点开各个文件夹，然后上传文件，好麻烦（毕竟目前大多数 GPT 都不支持上传文件夹或压缩包”
    - “那我们就把目录下文件结构与所有文件内容提取到一个 .txt 文件中，把这个文件发给 GPT 吧😆”

!!! info "参数解释"
    - `outFileName`：输出文件名
    - `fileInclude`：需要导出内容的文件类型，务必在使用前检查是否完全涵盖要求    
        1. 不包含的也会出现在结构图中
        2. `.exe .doc`之类不易直接导出可视字符的文件类型不要包含在里面
    - `excludeRules`：排除的路径，支持相对路径和绝对路径
        1. `"$PWD\.vscode"` 精准匹配根目录下`\.vscode`文件夹
        2. `".vscode"` 匹配所有`.vscode`文件夹
        3. （但1、2是否“精准”，暂未全面测试）
        4. `"Icon233*.vue"` 匹配所有以`Icon233`开头的`.vue`文件

!!! note "脚本"
    ```bash
    $CodeExport = {
        $outFileName = "ZZZ_CodeExport.txt"
        $outFile = "$PWD\$outFileName"
        $fileInclude = @("*.py", "*.vue", "*.js", "*.html", "*.css", "*.json", "*.txt", "*.hpp", "*.cpp", "*.c", "*.h", "*.md")

        $excludeRules = @(
            ".git"
            "node_modules",
            "__pycache__",
            "Icon233*.vue"
        )

        function Test-ExcludePath {
            param([string]$Path)

            foreach ($rule in $excludeRules) {
                if ($rule.Contains("\")) {
                    if ($Path -like "$rule*") { return $true }
                } else {
                    $dirs = $Path -split '[\\/]'
                    if ($dirs -contains $rule) { return $true }
                }
            }

            # 新增文件名匹配逻辑
            foreach ($rule in $excludeRules) {
                if ($Path -like "*\$rule") { return $true }
            }

            return $false
        }

        "==== 目录结构 ==== ([]代表文件夹)`n" | Out-File $outFile -Encoding utf8

        function Format-DirectoryTree {
            param([string]$path, [string]$indent = "")
            Get-ChildItem -Path $path | Where-Object { 
                $_.Name -ne "ZZZ_CodeExport.txt" -and
                -not (Test-ExcludePath -Path $_.FullName)
            } | ForEach-Object {
                if ($_.PSIsContainer) {
                    "$indent[$($_.Name)]" | Out-File $outFile -Encoding utf8 -Append
                    Format-DirectoryTree -path $_.FullName -indent ($indent + "   ")
                } else {
                    "$indent$($_.Name)" | Out-File $outFile -Encoding utf8 -Append
                }
            }
        }

        Format-DirectoryTree -path $PWD.Path

        "`n==== 文件内容 ====`n" | Out-File $outFile -Encoding utf8 -Append

        Get-ChildItem -Recurse -Include $fileInclude | Where-Object {
            $_.Name -ne "ZZZ_CodeExport.txt" -and
            -not (Test-ExcludePath -Path $_.FullName)
        } | ForEach-Object {
            "`n【文件路径】$($_.FullName)`n" + [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8) | Out-File $outFile -Encoding utf8 -Append
        }
    }
    & $CodeExport
    
    ```

!!! note "运行方式"
    1. 将上述脚本修改后输入 PowerShell 中执行
    2. 之后如果不修改脚本中的设置，重新生成输出文件可以直接用`& $CodeExport`命令，覆盖旧文件（但使用新终端时需要重新输入脚本）

!!! success "运行结果示例"
    ```
    ==== 目录结构 ==== ([]代表文件夹)

    [.vscode]
    settings.json
    [test1]
    [test11]
        test123.txt
    test12.txt
    hello.c

    ==== 文件内容 ====


    【文件路径】D:\desktop\test\.vscode\settings.json
    {
        "files.associations": {
            "*.sqlbook": "sql",
            "*.ndjson": "jsonl",
        }
    }

    【文件路径】D:\desktop\test\test1\test11\test123.txt
    Here is the content of test123.txt.

    2333

    【文件路径】D:\desktop\test\test1\test12.txt
    Here is the content of test12.txt

    Hello World!


    【文件路径】D:\desktop\test\hello.c
    #include <stdio.h>

    int main() {
        printf("Hello, World!\n");
        return 0;
    }
    ```
