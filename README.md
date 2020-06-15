# J2ExpSuite
这是一个以python3编写的的漏洞检测框架，可自定义，添加poc，exp，定向检测，初衷是为了什么呢？我想搞一个全面一点的漏洞检测框架，输入一个url，在选择检测漏洞类型，直接出结果，还要满足POC可集成，简单编写就能加载进去。主要是为了快速的检测漏洞高的存在，POC主要类型为RCE，读文件，注入漏洞，文件上传等类型漏洞，主要为了撕口子。于是我花了一天的时间搞出了这个框架，初步的满足了我的想法，可自定义poc，指定参数进行漏洞检测。（开开心心）

于是开始着手编写POC，发现好多啊，跟我之前做的都是无用功，无奈跟以前的poc不兼容，再写就还是造轮子，我尝试写了一部分，但是感觉写POC写的越多，这个工具就越来越不属于我，都是再用别人的POC，自己写吧，好多，好多啊！！！@#￥%……

{生活}{POC} orz

最终我选择了放弃~干脆就开源这个框架算了，POC什么的，慢慢写吧，
如果大家想一起去维护这个工具，大家可以把编写好的POC邮件发送给我，共同参与到项目中来，做一个好的工具，服务大家，创建一个良好的安全圈氛围，我的邮箱是:admin@je2se.com（好吧，是因为我懒）

先来几个截图看看工具样子

## 脚本启动的样子
![image-20191128110919811](./doc/Xnip2020-06-11_12-43-27.jpg)

## 脚本的功能菜单
![image-20191128110919812](./doc/Xnip2020-06-11_12-43-54.jpg)

## 运行截图
![image-20191128110919814](./doc/Xnip2020-06-11_13-20-35.jpg)

老样子，Windows没有皮肤主题，为什么没适配Windows，这是鼓励大家好好的工作，努力赚钱买苹果。（好吧，还是我懒~）

选中某个参数后，程序会自动加载目标参数路径下的所有py脚本，加载后会运行，上面的图片是已phpstudy举例的，加载完后会自动进行检测。

## 目前支持漏洞

框架/组件/中间件 |  漏洞名称 | 更新时间
-|-|-
Phpstudy | Phpstudy后门漏洞 | 2020年06月11日 
  ~|默认口令/空口令 | 2020年06月12日 
 Conference| CVE_2019_3396 | 2020年06月12日 
 Spring |Spring_CNVD_2016_04742|2020年06月12日 
  ~|Spring_CNVD_2016_04742|2020年06月12日
  ~|Spring_CVE_2020_5405|2020年06月12日
  ~|Spring_CVE_2019_3799|2020年06月12日
  ~|Spring_CVE_2018_1273|2020年06月12日
  ThinkPhp|ThinkPHP_SQLi_XFF_POC|2020年06月15日
  ~|ThinkPHP_Input_RCE_POC|2020年06月15日
  ~|ThinkPHP_PAY_SQLI_POC|2020年06月15日
  ~|ThinkPHP_Multi_SQL_LEAK_POC|2020年06月15日
  ~|ThinkPHP_Method_Filter_Code_Exec|2020年06月15日
  ~|ThinkPHP_Lite_Code_Exec_POC|2020年06月15日
  ~|ThinkPHP_Index_Showid_RCE_POC|2020年06月15日
  ~|ThinkPHP_Invoke_Func_Code_Exec|2020年06月15日
  ~|ThinkPHP_Index_Contruct_RCE|2020年06月15日
  ~|ThinkPHP_Driver_Display_RCE|2020年06月15日
  ~|ThinkPHP_Debug_Index_IDS_Sqli|2020年06月15日
  ~|ThinkPHP_Construct_Debug_RCE|2020年06月15日
  ~|ThinkPHP_Construct_Code_Exec_Verify|2020年06月15日
  ~|ThinkPHP_Checkcode_Time_Sqli|2020年06月15日
  别着急|正在写|持续更新
  要不然|大家|一起来~


    
    


## 看一下POC的编写

```python

# encoding: utf-8
from lib import *
import logging
from lib.Urldeal import umethod

def XXX_POC(Url): #必须与脚本名称相同
    scheme, url, port = umethod(Url)
    #------------POC部分，按需更改--------------
    try:
      urldata = scheme + "://" + url + ':' + str(port) + '/login.action'
      if "漏洞判断成功条件":
    #------------POC部分，按需更改--------------
          print(Vcolors.RED +"[!] 存在【漏洞名称】漏洞->版本号:什么漏洞\r" + Vcolors.ENDC)
    except:
        logging.error("【脚本名称】脚本出现异常")
        
```

编写后直接放入对应的路径下就行

如果你要添加新的检测项，请修改主文件，新建各路径下的__init__.py，可参考别的路径下的写法，编写XXXXScan的主方法，也可参考别的路径的文件写法

## 注意

没有放pip依赖列表，随运行，随安装吧~（没错，我是真的懒）

## 项目地址

项目地址：https://github.com/JE2Se/J2ExpSuite

我还想白嫖几个star，说不定哪天我更新POC呢~

## 项目愿景
后期会加入到指纹识别
