#!/usr/bin/python

'''
This module can login and logout WHUT campus network (which is provided by srun.com).
Anyone can uses it for free in any python program with the statement (as below) in its source code.
* From: DrRoy(royliu90@live.cn)
It requires  urllib, BeautifulSoup4 and lxml (lxml can be replaced by html.parser)
Its usage is as below (replace the 'username' and 'password' with your own):

import WhutNetUtil
util = WhutNetUtil.WhutNetUtil('username', 'password')
result = util.logout() # logout action
result = util.login() # login action

* warning:  BeautifulSoup from bs4 needs a module named 'lxml'.
You can replace it with 'html.parser' in line:
soup = BeautifulSoup(res, 'lxml')
And 'html.parser' doesnot need to install

If success, it returns True, or a string with error message if not.
The error message is from the origin page, and I donot know what contains in it.
I suggest you may logout first in order to make sure your device is offline

@author DrRoy
@email: royliu90@live.cn
@since 2017-01-09
'''

from urllib import parse  # 格式化post数据
from urllib import request  # 发送post请求
from bs4 import BeautifulSoup  # 处理登录or注销后的返回数据


class WhutNetUtil:
    def __init__(self, username, password):
        self.isLogin = False
        # 设置登录的用户名和密码
        self.username = username
        self.password = password
        # 以下内容不需要修改
        self.hosturl = r'http://172.30.16.58/srun_portal.php?url=www.srun.com&ac_id=10&sys='  # 登录页面的地址
        self.posturl = r'http://172.30.16.53/cgi-bin/srun_portal'  # 登录动作处理緖地址
        # 构造header
        self.headers = {
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0/ROY TOOL',
            'Referer': self.hosturl}

    def login(self):
        # 构造Post数据
        postData = {'action': 'login',
                    'uid': '-1',
                    'is_pad': '0',
                    'force': '0',
                    'ac_id': '10',
                    'page_error': '/ac_detect.php',
                    'pop': '1',
                    'ac_type': 'h3c',
                    'rad_type': '',
                    'gateway_auth': '0',
                    'local_auth': '1',
                    'is_debug': '0',
                    'is_ldap': '0',
                    'user_ip': '',
                    'mac': '',
                    'nas_ip': '',
                    'ssid': '',
                    'vlan': '',
                    'wlanacname': '',
                    'wbaredirect': '',
                    'page_succeed': 'http://172.30.16.53/help.html',
                    'page_logout': 'http://www.whut.edu.cn',
                    'page_error': 'http://172.30.16.53/help.html',
                    'username': self.username,
                    'password': self.password,
                    'save_me': '0',  # 不使用“记住密码”功能
                    'x': '53',
                    'y': '22'
                    }

        # 需要给Post数据编码
        postData = parse.urlencode(postData).encode('utf-8')

        # 通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
        req = request.Request(self.posturl, postData, self.headers)
        res = request.urlopen(req).read().decode('gbk')
        # You can replace 'lxml' with 'html.parser', and 'html.parser' doesnot need to install
        soup = BeautifulSoup(res, 'lxml')
        tag = soup.find(id='acct_msg')
        text = tag.text.strip()
        if text.startswith('连接成功'):
            return True
        else:
            return text

    def logout(self):
        # 构造Post数据，他也是从抓大的包里分析得出的。
        postData = {'action': 'logout'}

        # 需要给Post数据编码
        postData = parse.urlencode(postData).encode('utf-8')

        # 通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
        req = request.Request(self.posturl, postData, self.headers)
        res = request.urlopen(req)
        text = res.read().decode('utf8')
        if text.startswith('注销成功'):
            return True
        else:
            return text
