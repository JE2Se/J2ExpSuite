# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 10:53
@File:  J2ExpSuite.py
@Desc:  主文件time
'''

import sys
from lib import *
from exphub import *

#程序开始
if __name__ == '__main__':
    #判断py版本
    if sys.version_info.major < 3:
        sys.stdout.write(Vcolors.PURPLE + "J2ExpSuite 仅支持Python 3.x版本~\n" + Vcolors.ENDC)
        exit()
    #模块部分
    import argparse
    import pyfiglet

    #头部信息部分
    ascii_banner = pyfiglet.figlet_format("J2.ExpSuite")
    print(Vcolors.RED + ascii_banner+Vcolors.ENDC)
    print(Vcolors.OKBLUE + "\t\t\t\tPower by JE2Se" +"   "+ Vcolors.PURPLE + "V1.0" +"\n" +Vcolors.ENDC)
    parser = argparse.ArgumentParser()

    #脚本执行帮助部分
    print(Vcolors.PURPLE + "\t~请输入 -h 获取命令帮助~" + "\n" + Vcolors.ENDC +Vcolors.OKBLUE)
    parser.add_argument("-u" , "--url",type=str, help="填写待测试的URL链接~~(必填)")
    parser.add_argument("-s2" , "--struts", help = '添加 -struts 参数，将进行struts漏洞检测  ~~', action='store_true')
    parser.add_argument("-wl" , "--weblogic", help = '添加 -weblogic 参数，将进行weblogic漏洞检测  ~~', action='store_true')
    parser.add_argument("-tp" , "--thinkphp", help='添加 -thinkphp 参数，将进行ThinkPHP漏洞检测  ~~', action='store_true')
    parser.add_argument("-sh" , "--shiro", help='添加 -shiro 参数，将进行Apache Shiro漏洞检测  ~~', action='store_true')
    parser.add_argument("-sp" , "--spring", help='添加 -spring 参数，将进行Spring漏洞检测  ~~', action='store_true')
    parser.add_argument("-tm" , "--tomcat", help='添加 -tomcat 参数，将进行Tomcat漏洞检测  ~~', action='store_true')
    parser.add_argument("-cf" , "--conference", help='添加 -conference 参数，将进行Conference漏洞检测  ~~', action='store_true')
    parser.add_argument("-ps", "--phpstudy", help='添加 -phpstudy 参数，将进行PhpStudy后门漏洞检测  ~~', action='store_true')
    args = parser.parse_args()
    params = vars(args)

    #URL处理
    if args.url:
        url=args.url
        print(Vcolors.BROWN + " 感谢使用J2ExpSuite工具，正在运行，参数分析中......" + Vcolors.ENDC)
        print(Vcolors.CYAN + "[+] 待测试的链接为：" + Vcolors.ENDC + Vcolors.RED + url + Vcolors.ENDC)
        #导入文件处理簇
        if args.struts:
            print(Vcolors.CYAN + "[+] 测试模块内容为：" + Vcolors.ENDC + Vcolors.RED +"Struts2漏洞检测" + Vcolors.ENDC)
            StrutsScan(url)
        if args.weblogic:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED +"Weblogic漏洞检测" + Vcolors.ENDC)
        if args.thinkphp:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED +"ThinkPHP漏洞检测" + Vcolors.ENDC)
        if args.shiro:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED +"Apache Shiro漏洞检测" + Vcolors.ENDC)
        if args.tomcat:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED +"Tomcat漏洞检测" + Vcolors.ENDC)
        if args.spring:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED +"Spring漏洞检测" + Vcolors.ENDC)
        if args.conference:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "Conference漏洞检测" + Vcolors.ENDC)
        if args.phpstudy:
            print(Vcolors.CYAN + "[+] 测试的模块内容为：" + Vcolors.ENDC + Vcolors.RED + "PhpStudy后门漏洞检测" + Vcolors.ENDC)