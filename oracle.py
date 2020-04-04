#coding=utf-8
#import math
import os
import re
#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
import sys
print(sys.stdout.encoding)
import codecs
from tkinter import *
import tkinter.messagebox
from openpyxl import Workbook
from datetime import datetime
from tkinter import filedialog
import cx_Oracle
sqlstr=""
filepath=""
def selectmode():
    global dbDatas
    if CheckVar1.get()== 1 and CheckVar2.get() == 1 and CheckVar3.get() == 1:
        dbDatas = (
        ("SWYDX","Ysnd8s2_324","10.87.85.175:1521/oss","OMC2"),
        ("SWYDX","Ysnd8s2_324","10.217.9.80:1521/oss","OMC1"),
        ("SWYDX","Ysnd8s2_324","10.87.86.50:1521/oss","OMC3"),
        ("SWYZNJDPT","Hkswe2_0325","10.87.86.204:1521/oss","OMC4"),
        ("SWYDX","Ysnd8s2_324","10.87.72.50:1521/oss","OMC5"),
        ("SWYDX","Ysnd8s2_324","10.87.69.50:1521/oss","OMC6"),
        ("SWYDX","Ysnd8s2_324","10.217.29.50:1521/oss","OMC26"),
        ("SWYDX","Ysnd8s2_324","10.217.29.180:1521/oss","OMC27"),
        ("SWYDX","Ysnd8s2_324","10.87.67.50:1521/oss","OMC30"),
        ("SWYDX","Ysnd8s2_324","10.217.28.50:1521/oss","OMC28"),
        ("SWYDX","Ysnd8s2_324","10.217.26.50:1521/oss","OMC29"),
        ("SWYZNJDPT","Hkswe2_0325","10.217.15.44:1521/oss","OMC31"),
		("SWYZNJDPT","Hkswe2_0325","10.217.15.174:1521/oss","OMC32")
        )
    elif CheckVar1.get()== 1 and CheckVar2.get() == 1 and CheckVar3.get() == 0:
        dbDatas = (
        ("SWYDX","Ysnd8s2_324","10.87.85.175:1521/oss","OMC2"),
        ("SWYDX","Ysnd8s2_324","10.217.9.80:1521/oss","OMC1"),
        ("SWYDX","Ysnd8s2_324","10.87.86.50:1521/oss","OMC3"),
        ("SWYDX","Ysnd8s2_324","10.87.72.50:1521/oss","OMC5"),
        ("SWYDX","Ysnd8s2_324","10.87.69.50:1521/oss","OMC6"),
        ("SWYDX","Ysnd8s2_324","10.217.29.50:1521/oss","OMC26"),
        ("SWYDX","Ysnd8s2_324","10.217.29.180:1521/oss","OMC27"),
       ("SWYDX","Ysnd8s2_324","10.87.67.50:1521/oss","OMC30"),
        ("SWYDX","Ysnd8s2_324","10.217.28.50:1521/oss","OMC28"),
        ("SWYDX","Ysnd8s2_324","10.217.26.50:1521/oss","OMC29"),
        ("SWYZNJDPT","Hkswe2_0325","10.217.15.44:1521/oss","OMC31"),
		("SWYZNJDPT","Hkswe2_0325","10.217.15.174:1521/oss","OMC32")
        )
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1 and CheckVar3.get() == 0:
        dbDatas = (
        ("SWYDX","Ysnd8s2_324","10.217.28.50:1521/oss","OMC28"),
        ("SWYDX","Ysnd8s2_324","10.217.26.50:1521/oss","OMC29"),
        ("SWYZNJDPT","Hkswe2_0325","10.217.15.44:1521/oss","OMC31")
        )
    elif CheckVar1.get() == 1 and CheckVar2.get() == 0 and CheckVar3.get() == 0:
        dbDatas = (
        ("SWYDX","Ysnd8s2_324","10.87.85.175:1521/oss","OMC2"),
        ("SWYDX","Ysnd8s2_324","10.217.9.80:1521/oss","OMC1"),
        ("SWYDX","Ysnd8s2_324","10.87.86.50:1521/oss","OMC3"),
        ("SWYDX","Ysnd8s2_324","10.87.72.50:1521/oss","OMC5"),
        ("SWYDX","Ysnd8s2_324","10.87.69.50:1521/oss","OMC6"),
        ("SWYDX","Ysnd8s2_324","10.217.29.50:1521/oss","OMC26"),
        ("SWYDX","Ysnd8s2_324","10.217.29.180:1521/oss","OMC27"),
        ("SWYDX","Ysnd8s2_324","10.87.67.50:1521/oss","OMC30"),
		("SWYZNJDPT","Hkswe2_0325","10.217.15.174:1521/oss","OMC32")
        )
    elif CheckVar1.get() == 0 and CheckVar2.get() == 0 and CheckVar3.get() == 1:
        dbDatas = (
        ("SWYZNJDPT","Hkswe2_0325","10.87.86.204:1521/oss","OMC4"),
        )
    return dbDatas
#创建窗口
wds = tkinter.Tk()

def queryFn(sql):
    #inputText(sql)
    #sql = sql[1:]
    #print(len(sql))
    wb = Workbook()
    ws = wb.active
    #allx = 0
    inputText("开始连接数据库")
    for dbs in dbDatas:
        inputText("正在连接"+dbs[2]+'--'+dbs[3]+"....")
        try:
            print(dbs[0]+'--'+dbs[1]+'--'+dbs[2]+'--'+dbs[3])
            dbo = cx_Oracle.connect(dbs[0]+'/'+dbs[1]+'@'+dbs[2],encoding="utf8")
            #os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'
            inputText(dbs[2]+"--数据库连接成功")
            if type(sql) == str:   #无临时表sql解析为str类型进行查询
                cursor = dbo.cursor()
                cursor.execute(sql)
            else:
                for i in range(0,len(sql)): #临时表类型sql解析为list类型查询
                    try:
                        cursor = dbo.cursor()
                        cursor.execute(sql[i]) #SELECT * FROM c_lte_lncel
                    except BaseException :
                        continue
            res = cursor.fetchall()
            i=0
            title = [i[0] for i in cursor.description] #识别表头
            if res == None:
                inputText(dbs[2]+"--未查询到数据")
            else:
                inputText(dbs[2] + "查询到"+str(len(res))+"条数据")
                for row in res:
                    t=list(row)
                    t.append(dbs[3])
                    ws.append(t)
            cursor.close()
            dbo.close()
        except BaseException:
            inputText("BaseException")
            #inputText("sql可能存在错误")
        except Exception:
            inputText("Exception")
    ws.append(list(title)) #表头插入最后一行
    wb.save(createTimestr() + '.xlsx')
    inputText("数据导出完成!")
    tkinter.messagebox.showinfo('提示', '数据导出完成!')
    return

def toSql():
    # 导入sql文件
    otn=[]
    filepath = filedialog.askopenfilename()
    inputText("选择文件--"+filepath)
    # 读取文件内容
    fs = open(filepath,encoding='utf-8')
    global sqlstr
    temp_1 = fs.read()
    if len(re.findall('(?i)create table', temp_1)) > 0 :
        s  = temp_1.split(';')
        for i in range(0,len(s)):
            if len(s[i])> 0 and s[i].strip():
                otn.append(s[i].strip())
            sqlstr = otn
    else:
        s  = temp_1.strip()
        sqlstr = s
    #print(sqlstr)
        #else:
           # inputText("sql不正确")
    fs.close()
    return sqlstr

def createTimestr():
    curtime = datetime.now()
    curtime = str(curtime.year) + exporttime(curtime.month) + exporttime(curtime.day) + exporttime(
        curtime.hour) + exporttime(curtime.minute) + exporttime(curtime.second)
    return curtime

def exporttime(num):
    if num < 10:
        return str(0)+str(num)
    else:
        return str(num)

def clickfn():
    queryFn(sqlstr)
    return

def inputText(str1):
    hintstr.insert("end", str1+'\n\n')
    hintstr.yview_moveto(1)
    hintstr.update()  # 动态更新text
    return



wds.title('oracle数据导出工具')
wds.geometry("%dx%d+%d+%d"%(600,380,(wds.winfo_screenwidth()-600)/2,(wds.winfo_screenheight()-380)/2))
Label(wds,text="",justify=LEFT,width=20,height=1).grid(row=0,column=0)
#Label(wds,text="说明:本工具为导出oracle数据作用，请在下方输入查询的数据库和sql语句后，点击按钮进行查询。结果会导出excel表到本地").grid(row=0,column=0)
btn = Button(wds,text="导入sql",width=8,activebackground="gray",bd=4,command=toSql,padx=1,pady=2).grid(row=1,column=0)
btn = Button(wds,text="开始查询",activebackground="gray",bd=4,command=clickfn,padx=2,pady=2).grid(row=1,column=1)
Label(wds,text="",justify="left",width=20,height=1).grid(row=3,column=0)
Label(wds,text="操作进度 :",justify="center",width=16,height=2).grid(row=4,column=0)
hintstr = Text(wds,width=50,height=12)
hintstr.grid(row=4,column=1)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
C1 = Checkbutton(wds, text = "TDD", variable = CheckVar1,command = selectmode,onvalue = 1, offvalue = 0).grid(row=2,column=0)
C2 = Checkbutton(wds, text = "NB/FDD", variable = CheckVar2, command = selectmode ,onvalue = 1, offvalue = 0).grid(row=2,column=1)
C3 = Checkbutton(wds, text = "5G", variable = CheckVar3, command = selectmode ,onvalue = 1, offvalue = 0).grid(row=2,column=2)
#C1.pack()
#C2.pack()


wds.mainloop()
