# Linux 基础配置

!!! abstract
    当你使用一个新的Linux系统时，你需要进行的一些基础配置。

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
  - https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
  - https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
  - defaults

remote_read_timeout_secs: 1500.0
remote_connect_timeout_secs: 20.0
auto_activate_base: false

```
