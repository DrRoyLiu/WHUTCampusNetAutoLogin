# WHUTCampusNetAutoLogin

武汉理工大学校园网自动登录脚本（只在教学区测试过，寝室不知道能不能用）

在校园网中，如果长时间不使用网络，网络连接会自动断开

用这个脚本可以让电脑保持联网状态

This python program can login and logout WHUT campus network (or all the network which is provided by srun.com)

WhutNetUtil.py can login or logout the WHUT campus network.

KeepNetAlive.py is an usage demo of WhutNetUtil.py, it can keeps the computer always online (the net will disconnect if the network of your computer is not using).

You can put the KeepNetAlive.py in scheduled task of Windows, or create a new service in Linux.

Anyone can uses it for free in any python program with the statement (as below) in its source code.
* From: DrRoy(royliu90@live.cn)

It requires  urllib, BeautifulSoup4 and lxml (lxml can be replaced by html.parser)

Its usage is as below (replace the 'username' and 'password' with your own):

* import WhutNetUtil
* util = WhutNetUtil.WhutNetUtil('username', 'password')
* result = util.logout() # logout action
* result = util.login() # login action

Warning:  BeautifulSoup from bs4 needs a module named 'lxml'.

You can replace it with 'html.parser' in line:

* soup = BeautifulSoup(res, 'lxml')

And 'html.parser' doesnot need to install

If success, it returns True, or a string with error message if not.

The error message is from the origin page, and I donot know what contains in it.

I suggest you may logout first in order to make sure your device is offline

@author DrRoy

@email: royliu90@live.cn

@since 2017-01-09
