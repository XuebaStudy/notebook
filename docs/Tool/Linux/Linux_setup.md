# Linux 基础配置

!!! abstract
    当你使用一个新的Linux系统时，你需要进行的一些基础配置。（本内容由 Ubuntu 22.04 为基础）
    - 同步设置：`.bashrc`, `.bash_custom`, `.viminfo`, `.condarc`, `git设置`
    - 完全克隆（加上）：`.ssh`

## 1. git

```bash
git --version    # 查看 git 版本

## 如果未安装
sudo apt update
sudo apt install git
##

git config --list    # 查看 git 全局设置

git config --global user.name "<Your Name>"
git config --global user.email "<your_email@example.com>"

git config --global color.ui auto    # 启用颜色输出

ls ~/.ssh    # 查看 ssh 密钥（例如：id_ed25519是私钥文件，id_ed25519.pub是公钥文件，可能有其他类型，如果没有需要自行创建...）
ssh-keygen -t ed25519 -C "<your_email@example.com>" # 生成 ed25519 ssh 密钥

ssh -T git@github.com    # 查看 ssh 公钥是否成功加入了 github.com

```



## 2. Miniconda

```bash

conda --version    # 查看 conda 版本

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh    # 下载最新版本的 Miniconda 安装脚本
bash Miniconda3-latest-Linux-x86_64.sh    # 运行安装脚本


# 按要求安装完后（同意协议、设置默认路径、自动添加环境变量入.bashrc）
source ~/.bashrc
rm Miniconda3-latest-Linux-x86_64.sh
```

- 将 ~/.condarc 改为以下推荐设置

```
show_channel_urls: true

channels:
  - defaults

default_channels:
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/main
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/r
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/msys2

custom_channels:
  conda-forge: https://mirrors.bfsu.edu.cn/anaconda/cloud
  pytorch: https://mirrors.bfsu.edu.cn/anaconda/cloud

remote_read_timeout_secs: 1500.0
remote_connect_timeout_secs: 20.0
auto_activate_base: true


```



## 3. Bash 个性化设置

- 添加自定义命令（别名）

```bash
vim ~/.bash_custom    # 创建个性化设置文件（可通用）
vim ~/.bashrc
source ~/.bashrc

```

```bash
# .bash_custom 文件
# >>> conda >>>

alias act='conda activate'
alias deact='conda deactivate'
# 这样就可以用 'act base' 命令代替 'conda activate base' 了（其他可自行添加）

# <<< conda <<<


```

```bash
# .bashrc 文件

# ...
# Here are custom setting files
if [ -f ~/.bash_custom ]; then
	. ~/.bash_custom
fi

# ...
```
- bash 与 zsh 环境共享（同时设为使用zsh）
```bash
# .bashrc 文件末尾

# ...

if [[ $__USE_ZSH -eq 1 ]]; then
    echo "ENTER ZSH!"
    exec zsh
fi

```
```bash
# .zshrc 文件开头

if [[ -v __USE_ZSH ]]; then
  unset __USE_ZSH
else
  echo "ENTER BASH!"
  export __USE_ZSH=1
  exec bash
fi

# ...

# 这样设置后，在进入终端时会先输出:
# ENTER BASH!
# ENTER ZSH!
# 再显示zsh终端，此时既有bash又有zsh环境
```


## 4. Vim 配置文件

- 全局的可见`/etc/vim/vimrc`, 用户的可见`~/.vimrc`
    ```
??? note "~/.vimrc"
    ```vim
    
    set background=dark

    filetype plugin indent on

    set showmatch       " Show matching brackets.
    set ignorecase      " Do case insensitive matching
    set smartcase       " Do smart case matching
    set incsearch       " Incremental search
    "set autowrite      " Automatically save before commands like :next and :make
    set hidden      " Hide buffers when they are abandoned
    "set mouse=a        " Enable mouse usage (all modes)

    setlocal noswapfile " 不要生成swap文件
    set bufhidden=hide " 当buffer被丢弃的时候隐藏它
    "colorscheme evening " 设定配色方案
    set number " 显示行号
    set cursorline " 突出显示当前行
    set ruler " 打开状态栏标尺

    set expandtab " 使用空格代替Tab
    set tabstop=4 " 设置Tab键的宽度为4个空格
    set shiftwidth=4 " 设置自动缩进的宽度为4个空格

    set nobackup " 覆盖文件时不备份
    set autochdir " 自动切换当前目录为当前文件所在的目录
    set backupcopy=yes " 设置备份时的行为为覆盖
    set hlsearch " 搜索时高亮显示被找到的文本
    set noerrorbells " 关闭错误信息响铃
    set novisualbell " 关闭使用可视响铃代替呼叫
    set t_vb= " 置空错误铃声的终端代码
    set matchtime=2 " 短暂跳转到匹配括号的时间
    set magic " 设置魔术
    set smartindent " 开启新行时使用智能自动缩进
    set backspace=indent,eol,start " 不设定在插入状态无法用退格键和 Delete 键删除回车符
    set cmdheight=1 " 设定命令行的行数为 1
    set laststatus=2 " 显示状态栏 (默认值为 1, 无法显示状态栏)
    set statusline=\ %<%F[%1*%M%*%n%R%H]%=\ %y\ %0(%{&fileformat}\ %{&encoding}\ Ln\ %l,\ Col\ %c/%L%) " 设置在状态行显示的信息

    set encoding=utf-8  " 设定打开文件的编码为utf-8
    set fileencoding=utf-8  " 设定保存文件的编码为utf-8

    set foldenable " 开始折叠
    set foldmethod=syntax " 设置语法折叠
    set foldcolumn=0 " 设置折叠区域的宽度
    setlocal foldlevel=1 " 设置折叠层数为 1
    nnoremap <space> @=((foldclosed(line('.')) < 0) ? 'zc' : 'zo')<CR> " 用空格键来开关折叠 (Normal Mode下)

    inoremap jj <Esc> "输入 jj 时, 自动将其解释为按下 Esc , 即进入Normal Mode (Insert Mode下)
    ```
  
- 插件安装可以参考[ vim-plug 官方文档](https://github.com/junegunn/vim-plug)




