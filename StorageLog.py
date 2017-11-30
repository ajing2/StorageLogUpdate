#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 16:22
# @Author  : lingxiangxiang
# @File    : StorageLog.py
import codecs
import threading
import time

import sys

class A(threading.Thread):
    def __init__(self):
        super(A, self).__init__()
        self.contexts = []
        self.lock = threading.Lock()
    def run(self):
        while 1:
            self.lock.acquire()
            if len(self.contexts) !=0:
                with open('1.log', 'a') as f:
                    for context in self.contexts:
                        f.write(context)
                del self.contexts[:]
            self.lock.release()

    def write(self, context):
        self.contexts.append(context)


if __name__ == '__main__':
    thread = A()
    thread.start()
    sys.stderr = thread
    sys.stdout = thread
    for i in xrange(1, 100):
        print("{0}".format(i))
        time.sleep(0.1)
    # thread.term

