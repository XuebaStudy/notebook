!!! abstract
    记录一些使用 mkdocs 的基本命令，初次配置可参考：https://blog.csdn.net/qq_41261251/article/details/116021097
### git 状态查看
``` title=''
git status                  # 查看相关文件状态
git log                     # 查看git日志(哈希值、作者、时间、注释)
git log --pretty=oneline    # 查看git日志(仅哈希值、注释)
```
### git 文件操作
``` title=''
git add .               # 将所有已更改文件添加到缓存区
git commit -m "test"    # 将缓冲区文件提交，获得最新版本
git commit -am "test"   # 上述两步，一次解决 (新加入的文件需要初次 add)

# 以下（git开头）只能修改已经追踪的文件和文件夹
# 修改之后，相当于执行了 add ，直接 commit 就可以提交

git mv -v oldfile newfile         # 重命名文件(-v 显示信息)
git mv -v oldfolder newfolder     # 重命名文件夹 (若 newfolder 文件夹原本已经存在，则会将 oldfolder 移入 newfolder)
git mv -v oldfolder/ newfolder/   # (同上)

rm 'test.txt'           # 工作区删除文件
git add test.txt        # 版本库删除文件，还需要 commit
git commit -m "delete test"
```
### mkdocs 使用
``` title=''
# 在本地渲染相关笔记，可设置端口(如8000，则网站根目录为127.0.0.1:8000)

mkdocs serve    

# 将本地的仓库提交到Github仓库中的gh-pages分支(本地的git应为HEAD -> main)

mkdocs gh-deploy    

# 将Github仓库中的main分支更新至最新(HEAD -> main处)，同时在线笔记将更新

git push -u origin main 
```

!!! code "修改提交 便捷脚本"
    ```python
    import os
    name = "commit description"

    os.system('git add .')
    com =''.join(['git commit -m ',name])
    os.system(com)
    os.system('git push -u origin main')
    os.system('mkdocs gh-deploy')
    ```