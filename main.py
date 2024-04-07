#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/26 18:39
# @Author  : ys
# @File    : main.py
# @Software: PyCharm

import os
import subprocess

temp = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-

def PrintWrold(string):
    print(string)
    print("===========================================")


if __name__ == "__main__":
    PrintWrold({})
    pass
'''

def MakeNewFiles(num):
    if not os.path.exists("test"):
        os.makedirs("test")
    for i in range(num):
        file_name = "Hello_{}.py".format(i+1)
        file = os.path.join("test",file_name)
        with open(file, 'w') as f:
            f.write(temp.format(i+1))

def ReFile(num):
    if isinstance(num,int):
        file_name = "Hello_{}.py".format(num)
        file = os.path.join("test", file_name)
        with open(file, 'w') as f:
            f.write(temp.format(num))
    if isinstance(num,list):
        for i in num:
            file_name = "Hello_{}.py".format(i)
            file = os.path.join("test", file_name)
            with open(file, 'w') as f:
                f.write(temp.format(i))

def DoneFiles():
    # 创建一个字典来存储每个子进程的输出管道
    output_pipes = {}

    # 遍历目录中的文件
    for filename in os.listdir("test"):
        # 拼接文件路径
        filepath = os.path.join("test", filename)
        # 只处理文件，忽略子目录
        if os.path.isfile(filepath) and filepath.endswith('.py'):
            # 使用 subprocess 调用命令行执行 Python 脚本，并捕获输出管道
            process = subprocess.Popen(['python', filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output_pipes[filename] = process.stdout  # 存储输出管道
    # 读取并打印每个子进程的输出
    for filename, output_pipe in output_pipes.items():
        print(f'Output of {filename}:')
        for line in output_pipe:
            print(line, end='')  # 打印输出


if __name__ == "__main__":
    #MakeNewFiles(33)
    #Need_Reback = [1,2]
    #ReFile(Need_Reback)
    #ReFile(1)

    DoneFiles()
