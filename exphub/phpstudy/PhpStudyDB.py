# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 19:25
@File:  PhpStudyDB.py
@Desc:
'''

from lib import *
import logging
from lib.Urldeal import urldeal
import requests

def PhpStudyDB(Url): #必须与脚本名称相同
    scheme, url, port = urldeal(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    urldata = scheme + "://" + url + ':' + str(port) + '/phpmyadmin/index.php'
    post_data = {
        "pma_username": "root",
        "pma_password": "root",
        "server": "1",
        "target": "index.php"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Accept-Language": "zh-CN",
        "X-Forwarded-For": "8.8.8.8",
        "Connection": "close",
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        "Content-Type": "application/x-www-form-urlencoded",
    }
    try:
        a =requests.post(urldata, data=post_data, headers=headers, timeout=4, verify=False)
        a1 = requests.get(urldata, headers=headers, timeout=4, verify=False)
        con = a.text
        con2 = a1.text
        if con2.lower().find('navigation.php')!=-1 and con.lower().find('frame_navigation')!=-1:
            print(Vcolors.RED +"[!] 存在PhpStudy默认数据库界面口令漏洞\r默认口令root/root\r" + Vcolors.ENDC)
    except:
        logging.error("PhpStudyDB脚本出现异常")