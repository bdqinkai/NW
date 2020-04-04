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

import pandas as pd


def main():
    """
       主函数

    """
    t1=0
    t2=0
    t3=0
    t4=0

    a= 'd:\\alarm_time.csv'

    df = pd.read_csv(a)
    s = pd.DataFrame(df,columns=['ALARM_TIME_1','CANCEL_TIME_1'])
    t =s.values()
    for i in t:
        print(i)






if __name__ == '__main__':
    main()
