

## 压缩与解压
> `sudo apt install p7zip-full` 安装7z工具


| Command | Meaning |
| :--- | :--- |
| `7z a -tzip [archive.zip] [source]` | **压缩单个文件夹/文件**<br>`a`: Add (添加/压缩), `-tzip`: 指定 zip 格式 |
| `7z a -tzip [zip_name] [f1] [f2]` | **压缩多个文件/文件夹** |
| `-mx=0` / `-mx=9` | **设置压缩级别 (0-9)**<br>`-mx=0`: 仅存储, `-mx=9`: 最大压缩 |
| `-p[password]` | **(压缩)设置/(解压)解开密码保护**<br>`-p` 后无空格直接接密码（可用单引号包裹，防止特殊字符出错），<br>也可以后不接密码以交互式输入（更安全） |
| `-x![pattern]` | **排除特定文件** (支持通配符 `*`)<br>`-x!`: 排除模式 |
| `7z x [zip_name]` | **解压到当前目录**<br>`x`: Extract with full paths |
| `7z x [zip_name] -o[dir]` | **解压到指定目录**<br>`-o` 后无空格直接接路径 |

## 内存管理
|Command|Meaning|
|---|---|
|`du -h .`|查看当前目录下所有文件占用内存大小 (加上`-s`表示非递归)|


??? note "光标与阅读"
    |Shortcut|Meaning|
    |---|---|
    |Ctrl + Shift + Up|向上滚动终端（一行）|
    |Ctrl + PgUp|向上滚动终端（一页）|
    |Ctrl + End|（滚动后）回到光标位置|  
??? note "tree"
    ``` title='Linux下使用示例'
    $tree                   # 以树状图形式列出当前目录下所有文件的组织结构(含子目录)
    $tree <directory>       # 以树状图形式列出 directory 下所有文件的组织结构(含子目录)
    $tree ~/ > tree.txt     # 将用户目录下文件结构树状图保存在 tree.txt 文件中
    $tree -L 3              # 所列出树状图层数至多为3
    $tree -x                # 仅列出当前目录下树状图(不含子目录)

    ```

    ??? note "其他参数使用"
        -a 显示所有文件和目录。  
        -A 使用ASNI绘图字符显示树状图而非以ASCII字符组合。  
        -C 在文件和目录清单加上色彩，便于区分各种类型。  
        -d 显示目录名称而非内容。  
        -D 列出文件或目录的更改时间。  
        -f 在每个文件或目录之前，显示完整的相对路径名称。  
        -F 在执行文件，目录，Socket，符号连接，管道名称名称，各自加上”*”,”/”,”=”,”@”,”|”号。  
        -g 列出文件或目录的所属群组名称，没有对应的名称时，则显示群组识别码。  
        -i 不以阶梯状列出文件或目录名称。  
        -I <范本样式> 不显示符合范本样式的文件或目录名称。  
        -l 如遇到性质为符号连接的目录，直接列出该连接所指向的原始目录。  
        -n 不在文件和目录清单加上色彩。  
        -N 直接列出文件和目录名称，包括控制字符。  
        -p 列出权限标示。  
        -P <范本样式> 只显示符合范本样式的文件或目录名称。  
        -q 用”?”号取代控制字符，列出文件和目录名称。  
        -s 列出文件或目录大小。  
        -t 用文件和目录的更改时间排序。  
        -u 列出文件或目录的拥有者名称，没有对应的名称时，则显示用户识别码。 

        来源：https://blog.csdn.net/xuehuafeiwu123/article/details/53817161 

    ??? example "`$tree -L 2`使用效果"
        ``` title=''
        xueba@Ubuntu:~$ tree -L 2
        .
        ├── Desktop
        ├── Documents
        ├── Downloads
        ├── ics2024
        │   ├── abstract-machine
        │   ├── fceux-am
        │   ├── init.sh
        │   ├── Makefile
        │   ├── nemu
        │   └── README.md
        ├── Music
        ├── Pictures
        ├── Public
        ├── snap
        │   ├── firefox
        │   └── snapd-desktop-integration
        ├── Templates
        ├── Test
        │   ├── gdb_t
        │   ├── hello.c
        │   ├── input
        │   ├── Makefile
        │   └── output
        └── Videos
        ```
    ??? warning "Windows下使用方式不同"
        - Windows 自带的`tree`命令功能非常少，甚至不支持层数限制，建议使用以下 PowerShell 脚本替代：

        ```powershell
        function Get-DirectoryTree {
            param (
                [string]$Path,
                [int]$Depth = 0,
                [int]$MaxDepth = 2,
                [string]$Indent = ""
            )

            if ($Depth -ge $MaxDepth) { return }

            $items = Get-ChildItem -Path $Path
            $lastItemIndex = $items.Count - 1

            foreach ($item in $items) {
                $isLastItem = $item -eq $items[$lastItemIndex]
                if ($item.PSIsContainer) {
                    $connector = if ($isLastItem) { "└── " } else { "├── " }
                    Write-Host "$Indent$connector$($item.Name)"
                    $newIndent = if ($isLastItem) { "$Indent    " } else { "$Indent│   " }
                    Get-DirectoryTree -Path $item.FullName -Depth ($Depth + 1) -MaxDepth $MaxDepth -Indent $newIndent
                } else {
                    $connector = if ($isLastItem) { "└── " } else { "├── " }
                    Write-Host "$Indent$connector$($item.Name)"
                }
            }
        }

        # 调用函数，指定路径和最大深度，注意修改 D:\xxx\xxx 为实际路径
        Get-DirectoryTree -Path "D:\xxx\xxx" -MaxDepth 2

        ```

## 其他
|Command|Meaning|
|---|---|
|`find . -type f -name 'abc*' -delete`|删除该目录下以abc开头的文件（' '内可换为其他正则表达式）|
|`find . -name "*.[ch]" | xargs grep "#include" | sort | uniq`|列出一个C语言项目中所有被包含过的头文件|
|`ps aux --sort=-%mem | head -n 6`|列出当前目录下占用内存最大的前5个进程|
|`ps aux | grep mysqld`|查看 mysql 服务是否启动|
|`sudo systemctl stop mysql`|停止 mysql 服务|


!!! warning "markdown 表格中的特殊字符"
    - markdown表格中可用`&#124;`代替`|`，或者把`|`置于<code>&#96;&#96;</code>内防止影响表格结构
    - <code>&#96; &#96;</code> 效果同`<code> </code>`; <code>&#96;</code> == `&#96`


<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
