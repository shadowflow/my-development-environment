# 配置开发环境

## 一、基本环境

-----

### 1、安装字体

1. 在 `/usr/share/fonts` 下面建立一个文件夹，比如 `mkdir  mononoki`
2. 把需要的字体全部复制到`mononoki`文件夹里面。
3. 命令行执行 `fc-cache -fv` 刷新字体缓存。
4. OK，成功


### 2、版本控制git

#### 常见命令

1. `git clone xxxx`
2. `git add --all `     `git commit -m "xxxx" `       `git push -u origin master` 
3. `git pull` 

#### 生成秘钥

1. 再  `~/.ssh` 目录之下, ```ssh-keygen -t rsa -C "your_email@example.com"```

#### 不用每次都输入用户名字密码：

1. 在命令行输入命令:

   ```
   git config --global credential.helper store
   ```

   这一步会在用户目录下的`.gitconfig`文件最后添加：

   ```
   [credential]
       helper = store
   ```

2. push 代码
   `push`你的代码 (`git push`), 这时会让你输入`用户名`和`密码`, 这一步输入的用户名密码会被`记住`, 下次再push代码时就不用输入用户名密码!这一步会在用户目录下生成文件`.git-credential`记录用户名密码的信息。

#### 初始化的时候

```bash
echo "alias gg='git add * && git commit -m "update" && git push'" >> ~/.bashrc

git config --global user.email "xxxxxxx@xx.com"
git config --global user.name "xxxxx"

git config --global credential.helper store
```





### 3、umake

> ubuntu下很方便的开发软件安装工具，详情查看umake --help

#### 安装umake

```
apt install ubuntu-make -y
```

#### 安装软件

```bash
umake ide pycharm-professional
umake ide visual-studio-code
```

#### 设置环境变量

```bash
echo 'export PATH=$PATH:/root/.local/share/umake/bin' >> ~/.bashrc
```



### 4、cmake

#### 安装

```bash
apt install build-essential cmake make -y
```

#### 基本命令

```
cmake path  &&  make
```

#### 单目录，单文件

CMakeLists.txt

```
cmake_minimum_required (VERSION 3.9)

project (demo)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ./exercise/)

add_executable(demo main.cc)
```

#### 单目录，多文件

```
cmake_minimum_required (VERSION 3.9)

project (Demo2)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ./debug/)

aux_source_directory(./sources/ DIR_SRCS)
add_executable(Demo ${DIR_SRCS})
```
----



### 5、vscode

#### 安装vscode

```
umake ide visual-studio-code
```

#### 安装必备通用插件

1. beautify                    前端代码美化
2. c/c++                          c++必备，提供智能提示、自动补全、代码格式化……
3. python                      python必备，提供智能提示、自动补全、代码格式化……
4. vscode-icons            项目栏里面的图标漂亮点
5. one dark pro            漂亮的vscode主题。
6. path intellisense      路径智能补全。

#### 配置

> vscode部分插件不能自动生效，比如vscode-icons 和 One Dark Pro ，需要配置一下, 参考我的配置。

快键键  ctrl+ ,       或者 file -> preference -> setting    在右侧的用户配置里面输入如下。

我使用了mononoki这种编程字体，ubuntu没有自带，请修改。

```
{
    "workbench.iconTheme": "vscode-icons",
    "editor.fontSize": 18,
    "editor.fontFamily": "mononoki",
    "editor.formatOnSave": true,
    "workbench.colorTheme": "One Dark Pro",
    "vsicons.dontShowNewVersionMessage": true,
    "python.pythonPath": "python3",
    "window.zoomLevel": 1,
    "explorer.confirmDelete": false,
    "python.formatting.provider": "autopep8",
    "explorer.confirmDragAndDrop": false
}
```

#### 快捷键

ctrl +`     打开terminal

alt + shift +f  自动格式化代码

ctrl + ,       打开配置文件

ctrl + alt + n    安装code-runner插件后，此快捷键可以直接运行代码。

ctrl + alt +m   安装code-runner插件后，次快捷键可以强制停止运行代码。

#### root用户需要指定user-dir

```
mkdir ~/.vscode
echo "alias code='vscode --user-data-dir=/root/.vscode'" >> ~/.bashrc
```



### 6、pycharm

#### 安装

```
umake ide pycharm-professional
```



### 7、root登陆桌面（可选）

```
=== ubuntu17.10 root登录修改方法
===注意，请手动修改==

sudo vim /etc/gdm3/custom.conf

autologin-user=root
Enabling automatic login
[security]
AllowRoot=true

sudo vim /etc/pam.d/gdm-password
#auth required pam_succeed_if.so user != root quiet_success

sudo vim /etc/pam.d/gdm-autologin
#auth required pam_succeed_if.so user != root quiet_success

reboot
```



## 二、详细编程语言环境

### 1、python

#### 初始化

```
apt install python3-pip -y
```

使用vscode编写python会需要这两个包。

```
pip install pylint autopep8 pep8
```

#### 虚拟环境

1. ` pip3 install virtualenv virtualenvwrapper`

2. 写入环境变量

   ```
   echo 'export VIRTUALENVWRAPPER_PYTHON="/usr/bin/python3"' >> ~/.bashrc
   echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
   source ~/.bashrc
   ```

3. 常用指令

   ```
   mkvirtualenv zqxt：创建运行环境zqxt
   	mkvirtualenv -p python3 xxxxx

   workon zqxt: 工作在 zqxt 环境 或 从其它环境切换到 zqxt 环境

   deactivate: 退出终端环境

   rmvirtualenv ENV：删除运行环境ENV

   mkproject mic：创建mic项目和运行环境mic

   mktmpenv：创建临时运行环境

   lsvirtualenv: 列出可用的运行环境

   lssitepackages: 列出当前环境安装的包
   ```

   ​


### 2、c++

> 写大项目请用IDE

#### 项目模板生成脚本

参见本目录下cppgen.sh

使用方法:  创建新项目`./cppgen.sh xxxxxx`  

​		   编译执行`./running.sh` 
