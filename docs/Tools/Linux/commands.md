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

## 3.快捷键举隅
|Shortcut|Meaning|
|---|---|
|Ctrl + Shift + Up|向上滚动终端（一行）|
|Ctrl + PgUp|向上滚动终端（一页）|
|Ctrl + End|（滚动后）回到光标位置|



