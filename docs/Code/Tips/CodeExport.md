# 提取目录下文件结构与所有文件内容 (Windows PowerShell & Linux Bash)

!!! abstract
    - “我现在有一个里面有比较复杂的文件结构的项目，我想要把整个项目的代码发给 GPT 看一下，解决问题，但是这样必须得一点一点的点开各个文件夹，然后上传文件，好麻烦（毕竟目前大多数 GPT 都不支持上传文件夹或压缩包”
    - “那我们就把**当前目录下**文件结构与所有文件内容提取到一个 .txt 文件中，把这个文件发给 GPT 吧😆”

!!! info "参数解释"
    - `outDir`：输出文件目录（可以是绝对路径或相对路径，相对路径是基于脚本运行时的工作目录（$PWD），而非脚本所在目录）
    - `outFileName`：输出文件名
    - `fileInclude`：需要导出内容的文件类型，务必在使用前检查是否完全涵盖要求    
        1. 在这当中**不包含**的文件：也会出现在“目录结构”中，但不输出到“文件内容”中
        2. `.exe .doc`之类不易直接导出可视字符的文件类型不要包含在里面
    - `excludeRules`：排除的路径（支持相对路径和绝对路径）
        1. 在这当中**包含**的文件：“目录结构”、“文件内容”中都不出现
        1. `"$PWD\.vscode"` 精准匹配根目录下`\.vscode`文件夹
        2. `".vscode"` 匹配所有`.vscode`文件夹
        3. `"Icon233*.vue"` 匹配所有以`Icon233`开头的`.vue`文件

## PowerShell 脚本
```bash
$CodeExport = {
    # >>> 参数设置 >>>
    $outDir = "."
    $outFileName = "ZZZ_CodeExport.txt"
    $fileInclude = @("*.py", "*.vue", "*.js", "*.html", "*.css", "*.json", "*.txt", "*.hpp", "*.cpp", "*.c", "*.h", "*.md")

    $excludeRules = @(
        ".git"
        "node_modules"
        "__pycache__"
        "Icon233*.vue"
    )
    # <<< 参数设置 <<<

    # 创建输出目录（自动递归创建）
    $outDir = [System.IO.Path]::GetFullPath((Join-Path $PWD $outDir))
    if (-not (Test-Path $outDir)) {
        New-Item -ItemType Directory -Path $outDir -Force | Out-Null
    }
    $outFile = Join-Path $outDir $outFileName
    Write-Host "输出文件路径：$outFile"

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

        # 文件名匹配逻辑
        foreach ($rule in $excludeRules) {
            if ($Path -like "*\$rule") { return $true }
            # 处理通配符规则
            if ($rule -like "*`**") {
                $fileName = [System.IO.Path]::GetFileName($Path)
                if ($fileName -like $rule) { return $true }
            }
        }

        return $false
    }

    # 清空或创建输出文件
    "==== 目录结构 ==== ([]代表文件夹)`n" | Out-File $outFile -Encoding utf8

    function Format-DirectoryTree {
        param([string]$path, [string]$indent = "")
        Get-ChildItem -Path $path | Where-Object { 
            $_.Name -ne $outFileName -and
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
        $_.Name -ne $outFileName -and
        -not (Test-ExcludePath -Path $_.FullName)
    } | ForEach-Object {
        try {
            $content = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
            "`n【文件路径】$($_.FullName)`n$content" | Out-File $outFile -Encoding utf8 -Append
        } catch {
            Write-Warning "无法读取文件: $($_.FullName)"
        }
    }

    Write-Host "代码导出完成，结果保存在：$outFile"
}
& $CodeExport

```

!!! info "运行方式"
    1. 将上述脚本修改参数后粘贴到 PowerShell 终端对应路径下执行
    2. 之后如果不修改脚本中的设置，重新生成输出文件可以直接用`& $CodeExport`命令，覆盖旧文件（但使用新终端时需要重新输入脚本）


## Bash 脚本
```bash
#!/bin/bash

# >>> 参数设置 >>>
outDir="."
outFileName="ZZZ_CodeExport.txt"
fileInclude=("*.py" "*.vue" "*.js" "*.html" "*.css" "*.json" "*.txt" "*.hpp" "*.cpp" "*.c" "*.h" "*.md")

excludeRules=(
    ".git"
    "node_modules"
    "__pycache__"
    "Icon233*.vue"
)
# <<< 参数设置 <<<

# 创建输出目录（自动递归创建）
mkdir -p "$outDir" || {
    echo "错误：无法创建目录 $outDir"
    exit 1
}

# 获取输出文件的绝对路径（避免相对路径问题）
outFile="$(realpath "$outDir")/$outFileName"
echo "输出文件路径：$outFile"

# 清空或创建输出文件
echo "==== 目录结构 ==== ([]代表文件夹)" > "$outFile"

# 生成目录树结构
function format_directory_tree {
    local path="$1"
    local indent="$2"
    
    for item in "$path"/*; do
        # 跳过输出文件本身
        if [[ "$(basename "$item")" == "$outFileName" ]]; then
            continue
        fi
        
        # 检查是否在排除规则中
        exclude=false
        for rule in "${excludeRules[@]}"; do
            if [[ "$item" == *"/$rule" || "$item" == *"/$rule/"* || "$(basename "$item")" == "$rule" ]]; then
                exclude=true
                break
            fi
            # 处理通配符规则
            if [[ "$rule" == *"*"* ]]; then
                if [[ "$(basename "$item")" == ${rule} ]]; then
                    exclude=true
                    break
                fi
            fi
        done
        
        if [[ "$exclude" == false ]]; then
            if [[ -d "$item" ]]; then
                echo "${indent}[$(basename "$item")]" >> "$outFile"
                format_directory_tree "$item" "${indent}   "
            else
                echo "${indent}$(basename "$item")" >> "$outFile"
            fi
        fi
    done
}

format_directory_tree "$PWD" ""

echo -e "\n==== 文件内容 ====\n" >> "$outFile"

# 动态生成 find 的 -name 参数
find_args=()
for pattern in "${fileInclude[@]}"; do
    find_args+=("-o" "-name" "$pattern")
done
find_args=("${find_args[@]:1}")  # 移除第一个多余的 "-o"

# 查找并输出文件内容
find "$PWD" -type f \( "${find_args[@]}" \) | while read -r file; do
    # 跳过输出文件本身
    if [[ "$(basename "$file")" == "$outFileName" ]]; then
        continue
    fi
    
    # 检查排除规则
    exclude=false
    for rule in "${excludeRules[@]}"; do
        if [[ "$file" == *"/$rule" || "$file" == *"/$rule/"* ]]; then
            exclude=true
            break
        fi
        # 处理通配符规则
        if [[ "$rule" == *"*"* ]]; then
            if [[ "$(basename "$file")" == ${rule} ]]; then
                exclude=true
                break
            fi
        fi
    done
    
    if [[ "$exclude" == false ]]; then
        echo -e "\n【文件路径】$file\n" >> "$outFile"
        cat "$file" >> "$outFile"
    fi
done

echo "代码导出完成，结果保存在：$outFile"
```

!!! info "运行方式"
    1. 将上述脚本保存为`CodeExport.sh`文件  
    2. 在对应终端路径下运行`bash CodeExport.sh`或`bash <Path_to_CodeExport>`  




## 运行结果示例
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
