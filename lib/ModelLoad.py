# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 12:11
@File:  ModelLoad.py
@Desc:
'''
import sys
import time
from lib import *
import logging


class ONLoad:
    try:
        def __init__(self,name: str):
            self.name = name
            j=1
            for i in name:
                prompt = Vcolors.OKBLUE + "[+] 加载中: " + Vcolors.ENDC + (Vcolors.RED+ "模块{}->{}" +Vcolors.ENDC).format(j,i)
                j += 1
                sys.stdout.write("\r" + prompt)
                time.sleep(0.2)
                sys.stdout.flush()
            sys.stdout.write(Vcolors.OKGREEN +"\r" + "[*] ---------------加载结束---------------" + Vcolors.ENDC)
            sys.stdout.flush()
            liststr=""
            for s in name:
                liststr +="\t<->\t\b\b{}\n".format(s)
            print(Vcolors.PURPLE + "\n" + liststr.strip("\n") + Vcolors.ENDC)
            print(Vcolors.OKBLUE + "[*] ---------------开始测试---------------" + Vcolors.ENDC)
            #load1=["\\","/","一"]
            #for t in range(10000):
             #   for q in load1:
              #      prompt = Vcolors.OKBLUE + "[+] 测试中: "  + q + Vcolors.ENDC
               #     sys.stdout.write("\r" + prompt)
                #    time.sleep(0.2)
                 #   sys.stdout.flush()
    except:
        logging.error("ModelLoad.py文件运行异常")