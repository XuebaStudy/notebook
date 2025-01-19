## 1.一些常用的命令行工具(记不住就man): 

- 文件管理 - cd, pwd, mkdir, rmdir, ls, cp, rm, mv, tar
- 文件检索 - cat, more, less, head, tail, file, find
- 输入输出控制 - 重定向, 管道, tee, xargs
- 文本处理 - vim, grep, awk, sed, sort, wc, uniq, cut, tr
- 正则表达式
- 系统监控 - jobs, ps, top, kill, free, dmesg, lsof

## 2.命令使用举隅  
|Command|Meaning|
|---|---|
|`find . -type f -name 'abc*' -delete`|删除该目录下以abc开头的文件（' '内可换为其他正则表达式）|
|`find . -name "*.[ch]" | xargs grep "#include" | sort | uniq`|列出一个C语言项目中所有被包含过的头文件|

- markdown表格中可用`&#124;`代替`|`，或者把`|`置于<code>&#96;&#96;</code>内防止影响表格结构
- <code>&#96; &#96;</code> 效果同`<code> </code>`; <code>&#96;</code> == `&#96`
## 3.其他
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
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
