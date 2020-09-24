 
import os
import sys
import platform


# 添加需要安装的扩展包名称进去
#os.system("pip install GitPython")
#os.system("python -m pip install --upgrade pip")


import git
from git import *

curFileList = os.path.split(os.path.realpath(__file__))
repo = Repo(curFileList[0])
remote = repo.remote()
remote.pull()

import time
ticks = time.time()
localtime = time.asctime( time.localtime(time.time()) )

import json
data={}

# data = {
#     "启动时间戳":0,
#     "保存时间戳":0,
#     "启动时间":0,
#     "保存时间":0,
#     "本次运行时长":0,
#     "总游戏时长":0,
#     "本次游戏时间":0,
#     "总游戏时间":0,
# }

 
# 读取数据
with open(curFileList[0] + '\data.json', 'r',encoding = 'utf8') as f:
    data = json.load(f)

data["启动时间戳"] = ticks
data["启动时间"] = localtime

import subprocess  
import os  
main = "D:\\Games\\Epic Games\\ARKSurvivalEvolved\\ShooterGame\\Binaries\\Win64\\ShooterGame.exe"
if os.path.exists(main):  
    print("开始运行游戏")
#    rc,out= subprocess.getstatusoutput(main)  
    #print (rc)    
    #print (out)
    

# 写入 JSON 数据
with open(curFileList[0] + '\data.json', 'w',encoding = 'utf8') as f:
    json.dump(data, f)

