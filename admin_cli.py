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

import os


def admin_cli(mrbts_id,ip):
    uname = 'Nemuadmin'
    pw= 'nemuuser'
    host = str(ip).strip('\n')
    # print(host)
    ports ='443'
    json_data = '{\\"requestId\\":123456,\\"requestType\\":\\"infoModel\\",\\"parameters\\":{\\"name\\":\\"sfp\\",\\"parameters\\":{\\"action\\":\\"getLinksWithParameters\\"}}}'
    cmd = 'admin-cli.bat --bts-username={} --bts-password={} --bts-host={} --bts-port={} --data={} > D:\\Python_WS\\NW\sfp\\{}_{}_sfp.json'.format(uname,pw,host,ports,json_data,mrbts_id,host)
    print(cmd)
    os.system(cmd)

def main():
    """
       主函数

    """

    a= open('d:\\iplist.csv',encoding='utf-8')

    for i in a:
        mrbts_id = i.split(',')[0]
        ip = i.split(',')[1]
        # print(mrbts_id,ip)
        admin_cli(mrbts_id,ip)




if __name__ == '__main__':
    main()


