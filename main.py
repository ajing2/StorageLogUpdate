#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/3 21:42
# @Author  : lingxiangxiang
# @File    : main.py
import time

from utils import WriteLog
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def Xh():
    for i in xrange(1, 10000):
        print(i)
        # sys.stdout.write(str(i))
        time.sleep(0.1)





def main():
    writeLog = WriteLog("main.log")
    writeLog.start()
    sys.stdout = writeLog
    sys.stderr = writeLog
    Xh()

if __name__ == '__main__':
    main()