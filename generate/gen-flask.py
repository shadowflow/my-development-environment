#!/usr/bin/env python

import os
import sys

# project_name = sys.argv[1]
project_name = input("The project's name : \n")

os.mkdir(project_name)
os.chdir(project_name)

os.mkdir('static')
os.mkdir('templates')


# 创建config.py文件
content_config = """SQLALCHEMY_TRACK_MODIFICATIONS = False


# DIALECT = 'mysql'
# DRIVER = 'pymysql'
# USERNAME = 'root'
# PASSWORD = 'huajian'
# HOST = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'flaskTest'

# # 'dialect+driver://username:password@host:port/database?charset=utf8'

# SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
#     DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
"""
with open('config.py', 'w') as fconfig:
    fconfig.write(content_config)


# 创建主app文件
content_main = """from flask import Flask
from funcs import host_ip
app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.debug = True
    app.run(host=host_ip(), port=5000)
"""

with open('main.py', 'w') as fmain:
    fmain.write(content_main)


# 创建funcs.py 帮助文件，存储一些额外的帮助代码
content_funcs = """def host_ip():
    import socket
    # get ip of your computer
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('1.1.1.1', 1))
    ip = s.getsockname()[0]
    s.close()
    return ip
"""

with open('funcs.py', 'w') as ffuncs:
    ffuncs.write(content_funcs)
