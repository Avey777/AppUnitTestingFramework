#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import os
from base.Phone_devices import Initdevices
PATH = os.path.abspath(os.path.dirname(os.getcwd()))
devices = Initdevices().get_android_devices()
android_devices = "".join([item[key] for item in devices for key in item])
print(str(android_devices))
#APP参数

# udid = '192.168.1.121:5555'
# udid = '73047c33'
deviceName = 'MI6'
udid = str(android_devices)
host = '127.0.0.1'
port = 4723
platform = 'Android'
version = '6.0'
noReset = True
unicodeK = 'True'
resetKeyboard = 'True'
appPath = PATH + r'\app安装包路径'
AppPackage = '包名'
AppActivity = '包签名'
localPort = '5472'





