import urllib.request as urllib2, time, os, platform, re, string
from bs4 import BeautifulSoup  # 处理登录or注销后的返回数据
import WhutNetUtil

'''
This python program can make sure the computer is online by relogin when the net goes down.
It checks the status of network every 10 seconds.
It is a usage demo for WhutNetUtil.py

Anyone can uses it for free in any python program with the statement (as below) in its source code.
* From: DrRoy(royliu90@live.cn)

@author DrRoy
@email: royliu90@live.cn
@since 2017-01-09
'''

# start
print('keep net alive thread on')
plat = platform.platform().lower()
pid = os.getpid()


def record(msg):
    if (plat.startswith('windows')):
        fp = open(r"C:/KeepNetAlive.log", "a")
    else:
        fp = open("/home/KeepNetAlive.log", "a")
    t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    fp.write('%s: %s \n' % (t, msg))
    fp.close()


if (plat.startswith('windows')):
    fp = open("C:/KeepNetAlive.pid", "wt")
else:
    fp = open("/home/KeepNetAlive.pid", "wt")
fp.write("%d" % pid)
fp.close()

logaction = WhutNetUtil.WhutNetUtil('username', 'password') # 

# main
while True:
    try:
        # the code of 'http://www.royliu.cn' is 'utf8'
        # the code of login page is 'gbk'
        # so it may cause an exception if it is not login
        page = urllib2.urlopen('http://www.royliu.cn').read().decode("utf8")
        soup = BeautifulSoup(page, 'lxml')
        title = soup.title.text.strip()
        if title == '用户登录':
            if logaction.login():
                record('login')
    except Exception as e:
        # exception means it is offline
        record(e)
        page = urllib2.urlopen('http://www.royliu.cn').read().decode("gbk")
        soup = BeautifulSoup(page, 'lxml')
        title = soup.title.text.strip()
        if title == '用户登录':
            if logaction.login():
                record('login')

    time.sleep(10)
