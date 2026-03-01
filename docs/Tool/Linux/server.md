# Linux 服务器建网站

!!! abstract
    在 Linux 服务器上部署网站（静态/含前后端服务）的一些常见命令、流程

```bash
chmod +x /path/to/file  # 修改文件权限为可执行

# 查看某个服务状态（如 nginx、mysql、your-app）
systemctl status nginx
# 查看所有运行中的服务
systemctl list-units --type=service --state=running
# 检查服务是否开机自启
systemctl is-enabled <your-service>
```

## 部署静态网站（仅前端）
Nginx主配置文件：`/etc/nginx/nginx.conf`
Nginx站点配置文件：`/etc/nginx/sites-available/<your-site>`，然后软链接到`/etc/nginx/sites-enabled/<your-site>`
> 不要直接在 `sites-enabled/` 中编辑文件！应始终编辑 `sites-available/` 中的源文件

## 部署含后端服务的网站
待补充（需要考虑后端运行服务、权限保护等问题）