# Git 常用命令

!!! abstract
    - 这里记录一些常用 git 命令与 git 知识
    - git 用户级信息设置可见: [Linux 基础配置](https://note.xuebasy.top/Tool/Linux/Linux_setup/#1-git)  
    

```bash
# 初始化仓库
git init # 初始化一个空的 Git 仓库

# 克隆仓库
git clone [url] # 克隆远程仓库到本地
git clone [url] --depth 1 # 浅克隆，只获取最近一次提交的历史记录
git clone [url] --branch <branch-name> # 克隆指定分支

# 查看仓库的配置
git config --list # 查看所有配置
git config --global --list # 查看全局配置
git config --system --list # 查看系统配置
git config --local --list # 查看当前仓库的配置

# 查看状态
git status # 查看当前仓库的状态，包括未暂存、已暂存和未跟踪的文件
git status --short # 以简洁方式显示状态

# 添加文件到暂存区
git add . # 添加当前目录下所有文件到暂存区
git add <file> # 添加指定文件到暂存区
git add -A # 添加整个仓库所有文件到暂存区（且会处理已删除的文件，并将其标记为删除，而git add . 不会）
git add -u # 添加已跟踪的文件的修改到暂存区（忽略新文件）

# 提交暂存区的内容到本地仓库
git commit -m "Commit message" # 提交暂存区的内容，并附上提交信息
git commit -am "Commit message" # 自动暂存已跟踪的文件并提交
git commit --amend # 修改最后一次提交（用于修改提交信息，哈希值不变。在暂存区有新内容时会提交合并修改内容，哈希值改变，原来的提交会被替换）
git commit --allow-empty # 允许无更新提交

# 查看提交历史
git log # 查看当前分支提交历史记录
git log --all # 查看所有分支的提交历史记录
git log --oneline # 以简洁的方式查看当前分支提交历史记录
git log --pretty=oneline # “同上”（但有完整哈希值）
git log --graph --oneline --all # 查看分支的提交历史图
git log --author="name" # 查看指定作者的提交历史
git log --since="2025-01-01" --until="2025-01-30" # 查看指定时间段的提交历史

# 查看分支
git branch # 列出所有本地分支
git branch -r # 列出所有远程分支
git branch -a # 列出所有远程和本地分支
git branch -vv # 列出本地每个分支的最新提交信息以及它们所跟踪的远程分支信息（配合 -a 使用可以同时查看远程仓库最新提交信息）
git branch <branch-name> # 创建一个新分支
git branch -d <branch-name> # 删除本地分支
git branch -D <branch-name> # 强制删除本地分支（即使未合并）
git branch -m <old-name> <new-name> # 重命名本地分支

# 切换分支
git switch <branch-name> # 切换到指定分支
git switch -c <branch-name> # 创建并切换到新分支
git switch --track origin/<branch-name> # 创建并切换到远程分支的本地跟踪分支（本地名为：origin/branch-name）
git switch <commit> # 切换到指定提交（进入“分离头指针”状态）

# 合并分支
git merge <branch-name> # 将指定分支合并到当前分支
git merge --no-ff <branch-name> # 使用非快进合并，保留分支历史
git merge --abort # 中止正在进行的合并

# 拉取远程仓库的更新
git fetch # 拉取远程仓库的更新（默认 origin/<current-branch>）
git pull # 拉取远程仓库的最新内容并合并到当前分支
git pull origin <branch-name> # “同上”（但指定仓库、分支）
git pull --rebase # 使用 rebase 拉取更新

# 推送本地分支到远程仓库
git push origin <branch-name> # 推送本地分支到远程仓库
git push -u origin <branch-name> # 推送并设置上游分支
git push --set-upstream origin <branch-name> # 推送并设置上游分支（命令全称）
git push --force # 强制推送（谨慎使用）
git push --force-with-lease # 安全的强制推送

# 查看远程仓库信息（<remote-name> 为远程仓库的本地别名，常用 origin）
git remote -v # 查看远程仓库的 URL 和别名
git remote add <remote-name> <url> # 添加远程仓库
git remote remove <remote-name> # 删除远程仓库
git remote rename <old-name> <new-name> # 重命名远程仓库的本地别名
git remote update # 更新远程仓库的引用信息
git remote prune <remote-name> # 清理远程仓库中已删除的分支

# 查看文件的差异
git diff # 查看工作区和暂存区之间的差异
git diff --staged # 查看暂存区和最后一次提交之间的差异
git diff --cached # 查看暂存区和最后一次提交之间的差异（同 --staged）
git diff <commit1>..<commit2> # 查看两次提交之间的积累差异（顺序影响 +/-）
git diff <branch1>..<branch2> # 查看两个分支之间目前的差异
# ".." 可简化为空格

# 撤销操作
git restore . # 撤销工作区所有未暂存的修改
git reset <file> # 从暂存区撤销指定文件的修改（保留工作区的修改）
git reset --soft <commit> # 回退到指定提交，保留暂存区和工作区的修改
git reset --mixed <commit> # 回退到指定提交，保留工作区的修改（默认行为）
git reset --hard <commit> # 回退到指定提交，丢弃暂存区和工作区的修改（谨慎使用）
git reset --hard HEAD # 撤销暂存区和工作区的所有修改
git clean -fd # 强制删除未跟踪的文件和目录（谨慎使用）
# 不影响：已跟踪的文件（即已经 git add 或提交过的文件）、被 .gitignore 规则忽略的文件（除非加 -x）、Git 子模块（需额外加 -ff 才能删除子模块）
git clean -fd -n  # 显示将被删除的文件，但不实际执行（推荐先进行）

# 撤销最后一次提交
git revert HEAD # 撤销最后一次提交，创建一个新的提交记录
git reset --soft HEAD~1 # 撤销最后一次提交，保留暂存区的修改
git reset --hard HEAD~1 # 撤销最后一次提交，丢弃暂存区和工作区的修改

# 标签操作
git tag <tag-name> # 创建一个轻量级标签
git tag -a <tag-name> -m "Tag message" # 创建一个带注释的标签
git push origin <tag-name> # 推送标签到远程仓库
git tag -d <tag-name> # 删除本地标签
git push origin :<tag-name> # 删除远程标签
git push origin --tags # 推送所有本地标签到远程仓库

# 查看文件的历史
git blame <file> # 查看文件的每一行的提交信息
git blame -L <start-line>,<end-line> <file> # 查看文件指定行范围的提交信息


# 查看文件的版本历史
git log -p <file> # 查看文件的提交历史和修改内容
git log --stat <file> # 查看文件的提交历史和修改统计

# 查看文件的当前版本
git show <commit>:<file> # 查看指定提交版本的文件内容

# 查看文件的当前状态
git ls-files # 列出当前仓库中所有被跟踪的文件
git ls-files --others --exclude-standard # 列出未跟踪的文件

# 查看仓库的状态
git count-objects -vH # 查看仓库中对象的大小和数量


# 查看分支的合并状态
git merge-base <branch1> <branch2> # 查看两个分支的共同祖先
git branch --merged # 查看已合并到当前分支的分支
git branch --no-merged # 查看未合并到当前分支的分支

# Rebase 操作
git rebase <branch-name> # 将当前分支的更改重新应用到指定分支
git rebase --interactive <branch-name> # 交互式 rebase，可以修改提交历史
git rebase --abort # 中止正在进行的 rebase
git rebase --continue # 继续正在进行的 rebase

# 检查仓库的完整性
git fsck # 检查仓库的完整性，查找损坏的对象

# 子模块操作
git submodule add <url> <path> # 添加子模块
git submodule update --init --recursive # 初始化并更新子模块
git submodule foreach <command> # 在每个子模块中执行命令

# 忽略文件
git update-index --assume-unchanged <file> # 忽略文件的本地修改
git update-index --no-assume-unchanged <file> # 取消忽略文件的本地修改
git rm --cached <file> # 从 Git 跟踪中移除文件（但保留本地文件）

# 查看仓库的引用
git show-ref # 查看仓库的所有引用（分支、标签等）
git for-each-ref # 遍历并显示仓库的引用信息（可附加 --format 和 --sort 等选项，略）

```

??? note "git 中的 <commit\>"
    git 中 <commit\> 用于指定提交，可以是以下类型：    
    1. 提交的哈希值：如 7890abc  
    2. 分支名：如 feature  
    3. 标签名：如 v1.0  
    4. HEAD 引用：如 HEAD 或 HEAD~1 或 HEAD^^  
    5. 远程分支引用：如 origin/feature（origin 远程仓库的 feature 分支）  
    6. 特殊引用：如 @{upstream} 或 @{u} （追踪其上游分支，可以为远程或本地，可通过 `git branch -vv` 查看）   

??? note "git 命令中的 origin"
    这是一个常用的远程仓库的本地别名，如果取了别的名称或有多个相关的远程仓库，注意对应替换
