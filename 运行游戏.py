 
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



import subprocess  
import os  
main = "D:\\Games\\Epic Games\\ARKSurvivalEvolved\\ShooterGame\\Binaries\\Win64\\ShooterGame.exe"
if os.path.exists(main):  
    rc,out= subprocess.getstatusoutput(main)  
    print (rc)
    print ('*'*10)
    print (out)