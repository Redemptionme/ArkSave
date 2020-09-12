# coding: utf-8
import os
import sys
import platform
# 添加需要安装的扩展包名称进去
os.system("pip install GitPython")
os.system("python -m pip install --upgrade pip")


import git
from git import *


def read_file(file):
        """
        read .md or .txt format file
        :param file: .md or .txt format file
        :return: data
        """
        with open(file,'rb') as f:
            lines = f.readlines()
        data = []
        for line in lines:            
            data.append(line)
        return data







data = read_file('todo.md')

curFileList = os.path.split(os.path.realpath(__file__))
repo = Repo(curFileList[0])
remote = repo.remote()
remote.pull()

git = repo.git
git.add('.') 
git.commit('-m', data[0])

