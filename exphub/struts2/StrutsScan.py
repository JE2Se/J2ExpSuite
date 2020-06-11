# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 12:39
@File:  StrutsScan.py
@Desc:
'''
from lib.ModelLoad import ONLoad
from lib import *
import os
import logging

dlist = []
#文件遍历
def StrutsScan(url):
    for file in os.listdir("./exphub/struts2/"):
        if os.path.splitext(file)[1] == '.py':
            if os.path.join(file) != "__init__.py" and os.path.join(file) != "StrutsScan.py":
                dlist.append(os.path.join(os.path.splitext(file)[0]))
    ONLoad(dlist)
    try:
        for defclass in dlist:
            print(Vcolors.OKGREEN + "[?] 正在执行" + defclass + "脚本检测.......\r" + Vcolors.ENDC)
            exec("from exphub.struts2.{0} import {1}".format(defclass, defclass))
            defclass += "(url)"
            exec(defclass)

    except:
        logging.error("StrutsScan脚本出现异常")