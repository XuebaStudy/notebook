# Conda 常用命令

```bash
# 列举
conda info --env
conda env list

# 创建
conda create -n <env_name>
conda create -n <env_name> python=x.x

# 复制
conda create --name <new_env_name> --clone <old_env_name> 

# 删除（务必先退出相关环境）（“重命名 = 复制 + 删除”）
conda remove --name <env_name> --all

# 删除环境中的某个包
conda remove --name <env_name>  <package>

# 激活或者切换
conda activate <env_name>
 
# 关闭
conda deactivate

# 分享
conda env export > environment.yml  # 当前工作目录下生成一个environment.yml
conda env export -n <env_name> > <PATH>/<env_name>.yml # 导出指定环境的包列表到指定路径
conda env create -n <env_name> -f environment.yml # 拿到environment.yml文件后，将该文件放在工作目录下，可以通过以下命令从该文件创建环境
# 如果你的环境中有 pip 安装的包，这个方法可能会无效...(TODO)

# 列举包
conda list
conda list -n <env_name>

# 安装包
conda install  <package>
conda install -n <env_name> <package>
conda install --channel https://conda.anaconda.org/anaconda <package=x.x> # 指定版本和channel

# 升级包
conda update conda
conda update <package>      

# 查找包
conda search <package>      # 查看指定包可安装版本信息命令
conda search <package> --channel conda-forge    # 指定频道搜索

# 卸载包
conda uninstall <package>

# 清理包
conda clean -p          # 删除没有用的包，这个命令会检查哪些包没有在包缓存中被硬依赖到其他地方，并删除它们
conda clean -t          # 删除tar包
conda clean -y --all    # 删除所有的安装包及cache


# 获取版本号
conda -V

# 获取帮助
conda -h
conda env -h
conda search -h

```