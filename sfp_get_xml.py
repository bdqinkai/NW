# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     cli
   Description :
   Author :       kaqin
   date：          2019/10/16
-------------------------------------------------
   Change Activity:
                   2019/10/16:
-------------------------------------------------
"""
import os, pymysql
import tkinter
from tkinter.ttk import *


def main():
    """
       主函数

    """

    a = open('d:\ipadd.txt', 'r')

    for ip in a:
        # print(ip)
        ipadd = ip.strip('\n')
        print(ipadd)
        # sshservice = os.system("sshservice.bat -pw Nemuadmin:nemuuser -enable -ne {}".format(ipadd))
        sfpmonitor = os.system("sfpmonitor.bat -pw Nemuadmin:nemuuser -xml -ne {}".format(ipadd))
        # getactivealarms = os.system("getactivealarms.bat -pw Nemuadmin:nemuuser -ne {}".format(ipadd))
        # getalarmhistory = os.system("getalarmhistory.bat -pw Nemuadmin:nemuuser -ne {}".format(ipadd))
        # a = os.system("sfpmonitor.bat -pw Nemuadmin:nemuuser -enable -ne {}".format(ipadd))
        # a = os.system("sfpmonitor.bat -pw Nemuadmin:nemuuser -enable -ne {}".format(ipadd))
        print(a)


if __name__ == '__main__':
    main()


