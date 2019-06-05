#!/usr/bin/python3
# coding=utf-8

import _thread
import time
import threading
import queue

if 0:
    # 为线程定义一个函数
    def print_time( threadName, delay):
       count = 0
       while count < 5:
          time.sleep(delay)
          count += 1
          print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

    # 创建两个线程
    try:
       _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
       _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
    except:
       print ("Error: 无法启动线程")

    while 1:
       pass



if 0:
    exitFlag = 0

    class myThread(threading.Thread):
        """继承创建自己的多线程类"""
        def __init__(self,threadID,name,counter):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter

        def run(self):
            print("开始线程：" + self.name)
            print_time(self.name,self.counter,5)
            print("退出线程：" + self.name)

    def print_time(threadName,delay,counter):
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName,time.ctime(time.time())))
            counter -= 1

    #创建新线程
    thread1 = myThread(1,"Thread-1",1)
    thread2 = myThread(2,"Thread-2",2)

    #开启新线程
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("退出主线程")


if 0:
    class myThread(threading.Thread):
        """继承线程和线程同步"""
        def __init__(self,threadID, name, counter):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter

        def run(self):
            print("线程开始：" + self.name)
            #获取锁，用于线程同步
            threadLock.acquire()
            print_time(self.name, self.counter, 3)
            #释放锁，开启下一个线程
            threadLock.release()

    def print_time(threadName,delay,counter):
        while counter:
            time.sleep(delay)
            print("%s: %s" % (threadName,time.ctime(time.time())))
            counter -= 1

    threadLock = threading.Lock()
    threads = []

    #创建新线程
    thread1 = myThread(1,"Thread-1",1)
    thread2 = myThread(2,"Thread-2",2)

    #开启新线程
    thread1.start()
    thread2.start()

    #添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)

    #等待所有线程完成
    for t in threads:
        t.join()
    print("退出主线程")


if 1:
    pass