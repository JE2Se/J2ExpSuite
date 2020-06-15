# encoding: utf-8
from lib import *
import logging
from lib.Urldeal import umethod

def XXX_POC(Url): #必须与脚本名称相同
    scheme, url, port = umethod(Url) #URL处理，拆分初协议
    
    #-----------POC部分，下，按需更改--------------------
    urldata = scheme + "://" + url + ':' + str(port) + '/login.action
    
    try:
        if "漏洞判断成功条件":
    #-----------POC部分，上，输出部分--------------------
            print(Vcolors.RED +"[!] 存在【漏洞名称】漏洞->版本号:什么漏洞\r" + Vcolors.ENDC)
    except:
        logging.error("【脚本名称】脚本出现异常")
