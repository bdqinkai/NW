# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     SFP monitor
   Description :
   Author :       kaqin
   date：          2020/03/16
-------------------------------------------------
   Change Activity:
                   2020/03/16:
-------------------------------------------------
"""
import json
import glob
import pandas as pd
import numpy as np

def sfpinfo(path):
    sfp = []
    for json_file in glob.glob(path + '/*.json'):

        mrbts_id = json_file.split('\\')[4].split('_')[0]
        ip = json_file.split('\\')[4].split('_')[1]
        a = open(json_file, 'r')

        for i in a:

            if i.find('completed') >0:
                a = json.loads(i)
                df = pd.DataFrame(a)

                requestMessage = df['requestMessage']
                a = np.array(requestMessage).tolist()
                for j in a:
                    data = j['data']

                    s_linkPorts = list(pd.Series(data).get('linkPorts').values())[0]
                    d_linkPorts = list(pd.Series(data).get('linkPorts').values())[1]


                    linkType = pd.Series(data).get('linkType')
                    linkSpeed = pd.Series(data).get('linkSpeed')

                    moduleTemperature= list(pd.Series(data).get('measurements').values())[4]
                    s_moduleTemperature = list(moduleTemperature.values())[0]
                    d_moduleTemperature = list(moduleTemperature.values())[1]


                    TXSupplyVoltage = list(pd.Series(data).get('measurements').values())[0]
                    s_TXSupplyVoltage = list(TXSupplyVoltage.values())[0]
                    d_TXSupplyVoltage = list(TXSupplyVoltage.values())[1]

                    TXBiasCurrent = list(pd.Series(data).get('measurements').values())[1]
                    s_TXBiasCurrent = list(TXBiasCurrent.values())[0]
                    d_TXBiasCurrent = list(TXBiasCurrent.values())[1]

                    TXPower = list(pd.Series(data).get('measurements').values())[2]
                    s_TXPower = list(TXPower.values())[0]
                    d_TXPower = list(TXPower.values())[2]

                    RXOpticalPower = list(pd.Series(data).get('measurements').values())[3]
                    s_RXOpticalPower = list(RXOpticalPower.values())[0]
                    d_RXOpticalPower = list(RXOpticalPower.values())[2]


                    details = j['details']
                    connectorType = list(pd.Series(details).get('hardwareParameters').values())[0]
                    s_connectorType = list(connectorType.values())[0]
                    d_connectorType = list(connectorType.values())[1]

                    serialNumber = list(pd.Series(details).get('hardwareParameters').values())[2]
                    s_serialNumber = list(serialNumber.values())[0]
                    d_serialNumber = list(serialNumber.values())[1]

                    vendorPartNumber = list(pd.Series(details).get('hardwareParameters').values())[3]
                    s_vendorPartNumber = list(vendorPartNumber.values())[0]
                    d_vendorPartNumber = list(vendorPartNumber.values())[1]

                    waveLength = list(pd.Series(details).get('staticParameters').values())[0]
                    s_waveLength = list(waveLength.values())[0]
                    d_waveLength = list(waveLength.values())[1]

                    transmissionMode = list(pd.Series(details).get('staticParameters').values())[1]
                    s_transmissionMode = list(transmissionMode.values())[0]
                    d_transmissionMode = list(transmissionMode.values())[1]

                    transmissionRate = list(pd.Series(details).get('staticParameters').values())[2]
                    s_transmissionRate = list(transmissionRate.values())[0]
                    d_transmissionRate = list(transmissionRate.values())[1]

                    # 输出结果
                    s_value = [mrbts_id,ip,s_linkPorts,linkType,linkSpeed,s_moduleTemperature,s_TXSupplyVoltage,s_TXBiasCurrent,s_TXPower,s_RXOpticalPower,s_connectorType,s_serialNumber,s_vendorPartNumber,s_waveLength,s_transmissionRate,s_transmissionMode]
                    sfp.append(s_value)
                    d_value = [mrbts_id,ip,d_linkPorts,linkType,linkSpeed,d_moduleTemperature,d_TXSupplyVoltage, d_TXBiasCurrent, d_TXPower, d_RXOpticalPower,d_connectorType,d_serialNumber,d_vendorPartNumber,d_waveLength,d_transmissionRate,d_transmissionMode]
                    sfp.append(d_value)

        col_name = ['mrbts_id','ip','dn','linktype','linkspeed', 'moduleTemperature', 'TXSupplyVoltage', 'TXBiasCurrent', 'TXPower', 'RXOpticalPower','connectorType','serialNumber','vendorPartNumber','waveLength','transmissionRate','transmissionMode']
        json_df = pd.DataFrame(sfp, columns=col_name)
        json_df.to_csv('sfp_info_sbts.csv', index=None)

        print('{}解析完成,共计{}行'.format(json_file.split('\\')[4],json_df.shape[0]))


def main():
    path = ('D:\\Python_WS\\NW\\sfp')
    sfpinfo(path)

if __name__ == '__main__':
    main()
