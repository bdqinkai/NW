# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ssh
   Description :
   Author :       kaqin
   date：          2019/12/29
-------------------------------------------------
   Change Activity:
                   2019/12/29:
-------------------------------------------------
"""

import paramiko
import datetime


def ssh_exec(hostip,uname,passwd):
    '''SSH连接到基站'''

    try:
        ssh = paramiko.client.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            hostname = hostip,
            port = 22,
            username = uname,
            password = passwd
        )
        #stdin,stdout,stderr = ssh.exec_command("cat /ffs/run/config/lifedata/date_time.txt")
        stdin,stdout,stderr = ssh.exec_command("ls /ffs/run/config/lifedata/")

        print(stdout.read())
        ssh.close()

    #During handling of the above exception, another exception occurred

    except TimeoutError as e:
        raise NameError('connecting time out {}'.format(hostip)) from e

def sftp_file(hostip,uname,passwd):

    '''定义获取文件路径及文件名'''

    filepath = '/var/log'
    filename = 'temperature'

    dt=datetime.date.today()
    date=dt.strftime('%y%m%d')

    try:

        transport = paramiko.Transport((hostip, 22))
        transport.connect(username=uname, password=passwd)

        sftp = paramiko.sftp_client.SFTPClient.from_transport(transport)
        print(sftp.listdir(filepath))
        sftp.get('{}{}'.format(filepath, filename), '{}_{}_{}'.format(hostip,date,filename))
        sftp.close()

    except paramiko.ssh_exception.SSHException:
        print ('established connection failed because connected host has failed to respond {}'.format(hostip))


def main():

    uname='toor4nsn'
    passwd='oZPS0POrRieRtu'

    a = open('d:\ipadd.txt', 'r')

    for ip in a:

        hostip = ip.strip('\n')
        print('Connecting {}'.format(hostip))
        sftp_file(hostip,uname,passwd)

        #ssh_exec(hostip,uname,passwd)


if __name__ == '__main__':
    main()



