# -*- coding:utf-8 -*-
#多进程
from multiprocessing import Process

import os


def run_proc(name):
    print 'Child process %s (%s) Running...' % (name,os.getpid())

if __name__ == '__main__':
    print "Parent process %s" % os.getpid()
    for i in range(5):
        p = Process()