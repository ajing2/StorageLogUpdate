#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/3 21:55
# @Author  : lingxiangxiang
# @File    : utils.py
import codecs
import threading

import os


class WriteLog(threading.Thread):
    def __init__(self, logName):
        super(WriteLog,  self).__init__()
        self.logName = logName
        self.lock = threading.Lock()    #课上这里写是Lock没有写()
        self.contexts = []
        self.mkfile()

    def mkfile(self):
        if not os.path.exists(self.logName):
            with codecs.open(self.logName, 'w') as f:
                f.write("This file is log for {0}\n".format(self.logName))

    def write(self, context):
        self.contexts.append(context)

    def run(self):
        while 1:
            self.lock.acquire()
            if len(self.contexts) != 0:
                with codecs.open(self.logName, "a") as f:
                    for context in self.contexts:
                        f.write(context)
                del self.contexts[:]
            self.lock.release()




# class A(threading.Thread):
#     def __init__(self):
#         super(A, self).__init__()
#         self.contexts = []
#         self.lock = threading.Lock()
#     def run(self):
#         while 1:
#             self.lock.acquire()
#             if len(self.contexts) !=0:
#                 with open('main.log', 'a') as f:
#                     for context in self.contexts:
#                         f.write(context)
#                 del self.contexts[:]
#             self.lock.release()
#
#     def write(self, context):
#         self.contexts.append(context)