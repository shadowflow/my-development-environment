import os
import shutil


def cwd():
    """返回当前工作路径"""
    return os.getcwd()


def ls(filepath='.'):
    """ 列表形式 返回 文件 和 文件夹 的名称"""
    return os.listdir(filepath)


def cd(path):
    """切换到某个目录"""
    os.chdir(path)


def touch(filename):
    """创建一个空文件"""
    with open(filename, 'w') as ff:
        ff.write('hello world')


def mkdir(dirname):
    """创建空的文件夹"""
    os.mkdir(dirname)


def rm(name):
    """删除文件或者文件夹"""
    if os.path.isdir(name):
        shutil.rmtree(name)
    else:
        os.remove(name)


def mv(src, dst):
    shutil.move(src, dst)


def cp(src, dst):
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        shutil.copy(src, dst)


def chmod(onefile, mode=0o755):
    """更改权限，注意用八进制"""
    os.chmod(onefile, mode)


def isdir(name):
    """是否为目录"""
    return os.path.isdir(name)


def isfile(name):
    """是否为文件"""
    return os.path.isfile(name)


def islink(name):
    return os.path.islink(name)
