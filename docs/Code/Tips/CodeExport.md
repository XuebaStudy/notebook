# 提取目录下文件结构与所有文件内容

!!! abstract
    - “我现在有一个里面有比较复杂的文件结构的项目，我想要把整个项目的代码发给 GPT 看一下，解决问题，但是这样必须得一点一点的点开各个文件夹，然后上传文件，好麻烦（毕竟目前大多数 GPT 都不支持上传文件夹或压缩包”
    - “那我们就把目录下文件结构与所有文件内容提取到一个 .txt 文件中，把这个文件发给 GPT 吧😆”

!!! info "参数解释"
    - `outFileName`：输出文件名
    - `fileInclude`：需要导出内容的文件类型，务必在使用前检查是否完全涵盖要求    
        1. 不包含的也会出现在结构图中
        2. `.exe .doc`之类不易直接导出可视字符的文件类型不要包含在里面

!!! note "单次输入版（可直接点右上角的复制，粘贴到 PowerShell 中使用）"
    ```bash
    $outFileName="ZZZ_CodeExport.txt";$outFile="$PWD\$outFileName";$fileInclude=@("*.py","*.js","*.html","*.css","*.json","*.txt","*.hpp","*.cpp","*.c","*.h","*.md");"==== 目录结构 ==== ([]代表文件夹)`n"|Out-File $outFile -Encoding utf8;function Format-DirectoryTree{param([string]$path,[string]$indent="")$items=Get-ChildItem -Path $path|Where-Object{$_.Name-ne$outFileName};foreach($item in $items){if($item.PSIsContainer){"$indent[$($item.Name)]"|Out-File $outFile -Encoding utf8 -Append;Format-DirectoryTree -path $item.FullName -indent ($indent+"   ")}else{"$indent$($item.Name)"|Out-File $outFile -Encoding utf8 -Append}}};Format-DirectoryTree -path $PWD.Path;"`n==== 文件内容 ====`n"|Out-File $outFile -Encoding utf8 -Append;Get-ChildItem -Recurse -Include $fileInclude|Where-Object{$_.Name-ne$outFileName}|ForEach-Object{"`n【文件路径】$($_.FullName)`n"+[System.IO.File]::ReadAllText($_.FullName,[System.Text.Encoding]::UTF8)|Out-File $outFile -Encoding utf8 -Append}
    ```

!!! note "结构清晰版"
    ```bash
    $outFileName = "ZZZ_CodeExport.txt";
    $outFile = "$PWD\$outFileName";
    $fileInclude = @("*.py", "*.js", "*.html", "*.css", "*.json", "*.txt", "*.hpp", "*.cpp", "*.c", "*.h", "*.md");
    "==== 目录结构 ==== ([]代表文件夹)`n" | Out-File $outFile -Encoding utf8;
    function Format-DirectoryTree {
        param([string]$path, [string]$indent = "")
        $items = Get-ChildItem -Path $path | Where-Object { $_.Name -ne "ZZZ_CodeExport.txt" };
        foreach ($item in $items) {
            if ($item.PSIsContainer) {
                "$indent[$($item.Name)]" | Out-File $outFile -Encoding utf8 -Append;
                Format-DirectoryTree -path $item.FullName -indent ($indent + "   ")
            }
            else {
                "$indent$($item.Name)" | Out-File $outFile -Encoding utf8 -Append
            }
        }
    };
    Format-DirectoryTree -path $PWD.Path;
    "`n==== 文件内容 ====`n" | Out-File $outFile -Encoding utf8 -Append;
    Get-ChildItem -Recurse -Include $fileInclude | Where-Object { $_.Name -ne "ZZZ_CodeExport.txt" } | ForEach-Object {
        "`n【文件路径】$($_.FullName)`n" + [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8) | Out-File $outFile -Encoding utf8 -Append
    }
    ```

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
