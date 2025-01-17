
## 跳转
- **头文件跳转**：将光标移至头文件名处，（普通模式）按下`gf`可跳转至对应文件中；按下`Ctrl + 6`可以返回。
??? failure "Can't find `test/miss_file` in path 报错"
    1. 在Terminal中输入`vim ~/.vimrc`
    2. 在配置文件中加入`set path+=~/test/**`（set path命令接受\*之类的通配符. (\*表示任何字符)，该命令表示允许搜索test目录下所有名为miss_file的文件）（`set path+=~/test/**3`表示...最大深度为3）

- **函数、变量跳转**：使用工具ctags
    1. 首先在Terminal包含源文件的目录下使用`ctags -R`生成 tags 文件
    2. 用vim打开源文件，将光标移至想要跳转的函数或变量上，按`Ctrl + ]`即可跳转至其定义处，按`Ctrl + t`可原路返回
    3. (注：用vim打开子目录下文件时，需要使用相对路径，不可直接进入子目录，否则无法查找到 tags 文件)

