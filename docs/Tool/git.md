
``` title=''
git log --author="xueba"    # 查找作者为xueba的提交记录

git commit --allow-empty    # 允许无更新提交

git branch              # 展示所有分支
git checkout -b <branch_name>   # 创建新分支branch_name，并checkout(将其设为main)
git checkout pa0        # checkout 分支pa0

git diff                # 查看与上一次提交的差别
git diff <branch_name> main   # 显示branch_name分支与main分支的差别

git log --oneline --graph --all
```

```
❯ git pull origin main
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

❯ git remote -v
Git_test        git@github.com:XuebaStudy/Git_test.git (fetch)
Git_test        git@github.com:XuebaStudy/Git_test.git (push)

❯ git remote rename Git_test origin
Renaming remote references: 100% (1/1), done.

❯ git remote -v
origin  git@github.com:XuebaStudy/Git_test.git (fetch)
origin  git@github.com:XuebaStudy/Git_test.git (push)

❯ git pull origin main
From github.com:XuebaStudy/Git_test
 * branch            main       -> FETCH_HEAD
```