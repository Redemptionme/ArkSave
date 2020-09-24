 
import os
import sys
import platform


# 添加需要安装的扩展包名称进去
#os.system("pip install GitPython")
#os.system("python -m pip install --upgrade pip")


import git
from git import *


def read_file(file):
        """
        read .md or .txt format file
        :param file: .md or .txt format file
        :return: data
        """
        with open(file,'r',encoding = 'utf8') as f:
            lines = f.readlines()
        data = []
        for line in lines:            
            data.append(line)
        return data



mddata = read_file('todo.md')

curFileList = os.path.split(os.path.realpath(__file__))
repo = Repo(curFileList[0])
remote = repo.remote()
remote.pull()

git = repo.git


git.add('.') 
logStr = ""

import time
ticks = time.time()
localtime = time.asctime( time.localtime(time.time()) )
import json
# data = {
#     "启动时间戳":0,
#     "保存时间戳":0,
#     "启动时间":0,
#     "保存时间":0,
#     "本次运行时长":0,
#     "总游戏时长":0,
# }

data={}
 
# 读取数据
with open(curFileList[0] + '\data.json', 'r',encoding = 'utf8') as f:
    data = json.load(f)

data["保存时间戳"] = ticks
data["保存时间"] = localtime
data["本次运行时长"] = data["保存时间戳"] - data["启动时间戳"]
data["总游戏时长"] = data["总游戏时长"] + data["本次运行时长"]

def secondsToGameStr(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)    
    return "%02d时%02d分%02d秒" % (h, m, s)


data["本次游戏时间"] = secondsToGameStr(data["本次运行时长"])
data["总游戏时间"] = secondsToGameStr(data["总游戏时长"])

# 写入 JSON 数据
with open(curFileList[0] + '\data.json', 'w',encoding = 'utf8') as f:
    json.dump(data, f)


logStr = "本次游戏时间 " + data["本次游戏时间"] + " 总游戏时间 " +  data["总游戏时间"]

for log in mddata:
    logStr = logStr + log
git.commit('-m', logStr)
git.push()

