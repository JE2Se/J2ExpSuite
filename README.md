# J2ExpSuite
一个以python3编写的的漏洞检测框架，可自定义，添加poc，exp

简单的写了一个框架，里面你的漏洞都没有集成，网络上有很多的poc，可以借鉴别人的POC轮子。我这里就不写了，只是把利用框架写出来。
（如果大家想一起去维护这个工具，大家可以把编写好的POC右键发送给我，共同参与到项目中来，做一个好的工具.邮箱:admin@je2se.com）

先来几个截图看看工具样子

## 脚本启动的样子
![image-20191128110919814](./doc/Xnip2020-06-11_12-43-27.jpg)

## 脚本的功能菜单
![image-20191128110919814](./doc/Xnip2020-06-11_12-43-54.jpg)

## 运行截图
![image-20191128110919814](./doc/Xnip2020-06-11_13-20-35.jpg)

老样子，Windows没有皮肤主题

选中某个参数后，程序会自动加载目标参数路径下的所有py脚本，加载后会运行，上面的图片是已phpstudy举例的，加载完后会自动进行检测。

## 看一下POC的编写

```python

# encoding: utf-8
from lib import *
import logging
from lib.Urldeal import urldeal

def XXX_POC(Url): #必须与脚本名称相同
    scheme, url, port = urldeal(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    ---------------------------------------
    try:
      #POC部分，按需更改
      urldata = scheme + "://" + url + ':' + str(port) + '/login.action'
      if "漏洞判断成功条件":
          print(Vcolors.RED +"[!] 存在【漏洞名称】漏洞\r版本号:什么漏洞\r" + Vcolors.ENDC)
    except:
        logging.error("【脚本名称】脚本出现异常")
        
```

编写后直接放入对应的路径下就行

如果你要添加新的检测项，请修改主文件，新建各路径下的__init__.py，可参考别的路径下的写法，编写XXXXScan的主方法，也可参考别的路径的文件写法


## 注意
缺的模块我就不放txt了，随报错随PIP吧


