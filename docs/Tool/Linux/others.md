## tmux
```bash title='Linux下使用示例'
#安装 tmux（Ubuntu/Debian 系统）
sudo apt-get install tmux

tmux    #启动 tmux（默认创建一个编号为 0 的新会话）
tmux new -s <name>    #创建名为 name 的新会话

#记前缀键为<prefix>，默认是 Ctrl+b，可以按后文配置修改为 Ctrl+a（更容易按），前缀键仅在 tmux 界面有用
<prefix> d    #分离当前会话（会话继续后台运行）
Alt+D   #按下文修改配置后可以直接 detach

<prefix> s    #弹出可视化会话列表，使用键盘的 ↑↓ 方向键选择会话，按 Enter 即可进入。

tmux ls   #列出所有会话
tmux attach -t <name>   #重新连接到指定会话

tmux kill-session -t <会话名称/编号>    #删除会话
```
- 按下文修改配置后，可以在 tmux 界面按 `Ctrl+b :` 然后输入 `source-file ~/.tmux.conf` 重新加载配置。
??? note "~/.tmux.conf"
    ```bash
    # 设置前缀键为 Ctrl+a（比默认的 Ctrl+b 更容易按）
    unbind C-b
    set -g prefix C-a
    bind C-a send-prefix
    # Alt+D 直接 detach
    bind-key -n M-d detach-client

    # 启用鼠标支持（可以鼠标点击切换面板/窗口）
    set -g mouse on

    # 设置状态栏颜色
    set -g status-bg colour235
    set -g status-fg colour250

    # 添加并加载一次后，以后修改配置只需要按 Ctrl+b 然后按 r，就能一键重载配置，并且屏幕底部还会弹出 "Config reloaded!" 的提示
    bind r source-file ~/.tmux.conf \; display-message "Config reloaded!"

    ```



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