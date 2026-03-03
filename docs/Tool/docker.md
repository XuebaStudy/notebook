# docker 常用命令

## 容器准备
```bash
# 拉取镜像
docker pull <xx/xx/xxx>:<latest>

# 创建并命名容器、挂载目录、进入容器（仅需初始执行一次）
docker run -it --name <container_name> -v /d/desktop/workdir:/root/workdir <xx/xx/xxx>:<latest> /bin/bash && cd /root/workdir

# 进入已经创建（未运行）的容器
docker start -i <container_name>
# 进入正在运行的容器并切换到工作目录
docker exec -it <container_name> /bin/bash && cd /root/workdir


# 交互式进入容器
docker run -it <xx/xx/xxx>:<latest> /bin/bash
# 挂载本地目录到容器
docker run -v /d/desktop/workdir:/root/workdir <xx/xx/xxx>:<latest>
# 停止、删除容器（务必先退出相关容器）
docker stop <container_name>
docker rm <container_name>

```

## 容器管理
```bash
# 查看所有容器（包括已停止的）
docker ps -a

# 查看正在运行的容器
docker ps
```