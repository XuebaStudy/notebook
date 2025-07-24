## ncdu
> `ncdu` 是一个基于 ncurses 的磁盘使用分析器，提供了一个交互式的界面来查看和管理磁盘空间（比 `du` 更直观）

```bash title='Linux下使用示例'
# 安装 ncdu
sudo apt update && sudo apt install ncdu

# 使用 ncdu 扫描当前目录
ncdu .

# 使用 ncdu 扫描除了mnt目录外的所有目录
ncdu --exclude mnt /

```

<div style="display: flex; align-items: flex-start; justify-content: center; gap: 16px;">
  <img src="../../images/ncdu_1.png" alt="ncdu 界面1" width="300" />
  <img src="../../images/ncdu_2.png" alt="ncdu 界面2" width="300" />
</div>
<p style="text-align: center;">ncdu 界面截图</p>

??? "简要操作说明"
    - 使用方向键或 `j`/`k` 键移动光标
    - 按 `s` 进行顺、逆排序
    - 按 `Enter` 进入子目录
    - 按 `q` 退出
    - 按 `d` 删除选中的文件或目录
    - 按 `?` 查看帮助

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>