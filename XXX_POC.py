# encoding: utf-8
from lib import *
import logging
from lib.Urldeal import urldeal

def XXX_POC(Url): #必须与脚本名称相同
    scheme, url, port = urldeal(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    urldata = scheme + "://" + url + ':' + str(port) + '/login.action'
    #POC部分，按需更改
    try:
        if "漏洞判断成功条件":
            print(Vcolors.RED +"[!] 存在【漏洞名称】漏洞\r版本号:什么漏洞\r" + Vcolors.ENDC)
    except:
        logging.error("【脚本名称】脚本出现异常")
