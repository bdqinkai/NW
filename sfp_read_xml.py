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
from xml.etree import ElementTree
import glob
import pandas as pd


def sfpinfo(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ElementTree.parse(xml_file)
        root = tree.getroot()
        for i in root.findall('SFP'):

            mrbts = i.find('_distname')
            if mrbts != None:
                mrbts = mrbts.text
                if mrbts != None:
                    mrbts_str = mrbts.split('/')[0]
                    mrbts_id = mrbts_str.replace("MRBTS-", "")
                else:
                    mrbts_id= mrbts

            # sfp.append(mrbts_id)

            dn = i.find('_distname')
            if dn != None:
                dn = dn.text
            # sfp.append(dn)

            port = i.find('_physicalPort')
            if port != None:
                port = port.text
            # sfp.append(port)

            vendor = i.find('_sfpVendor')
            if vendor != None:
                vendor = vendor.text
            # sfp.append(vendor)

            sn = i.find('_sfpSerialNumber')
            if sn != None:
                sn = sn.text
                # sn = sn_str.replace(' ', '')
            # sfp.append(sn)

            type = i.find('_sfpType')
            if type != None:
                type = type.text
            # sfp.append(type)

            wavelength = i.find('_waveLength')
            if wavelength != None:
                wavelength_Str = wavelength.text
                wavelength = wavelength_Str.split(' ')[0]
            # sfp.append(wavelength)

            transmissionMode = i.find('_transmissionMode')
            if transmissionMode != None:
                transmissionMode = transmissionMode.text
            # sfp.append(transmissionMode)

            transmissionRate = i.find('_transmissionRate')
            if transmissionRate != None:
                transmissionRate_Str = transmissionRate.text
                transmissionRate = transmissionRate_Str.split(' ')[0]
            # sfp.append(transmissionRate)

            transmissionDistance = i.find('_transmissionDistance')
            if transmissionDistance != None:
                transmissionDistance_Str = transmissionDistance.text
                transmissionDistance = transmissionDistance_Str.split(' ')[0]
            # sfp.append(transmissionDistance)

            temperature = i.find('_temperature')
            if temperature != None:
                temperature_Str = temperature.text
                temperature = temperature_Str.split(' ')[0]
            # sfp.append(temperature)

            txVoltage = i.find('_txVoltage')
            if txVoltage != None:
                txVoltage_str = txVoltage.text
                txVoltage = txVoltage_str.split(' ')[0]
            # sfp.append(txVoltage)

            txCurrent = i.find('_txCurrent')
            if txCurrent != None:
                txCurrent_str = txCurrent.text
                txCurrent = txCurrent_str.split(' ')[0]
            # sfp.append(txCurrent)

            txPower = i.find('_txPower')
            if txPower != None:
                txPower_str = txPower.text
                txPower = txPower_str.split(' ')[0]
            # sfp.append(txPower)

            rxPower = i.find('_rxPower')
            if rxPower != None:
                rxPower_str = rxPower.text
                rxPower = rxPower_str.split(' ')[0]
            # sfp.append(rxPower)

            value = (
            mrbts_id, dn, port, vendor, sn, type, wavelength, transmissionMode, transmissionRate, transmissionDistance,
            temperature, txVoltage, txCurrent, txPower, rxPower)
            xml_list.append(value)
        col_name = ['mrbts_id',
                    'distname',
                    'physicalPort',
                    'sfpVendor',
                    'sfpSerialNumber',
                    'sfpType',
                    'waveLength(nm)',
                    'transmissionMode',
                    'ransmissionRate(Mb/s)',
                    'transmissionDistance(m)',
                    'temperature',
                    'txVoltage',
                    'txCurrent',
                    'txPower',
                    'rxPower'
                    # 'rxPower({})'.format(rxPower_str.split(' ')[1])
                    ]

        xml_df = pd.DataFrame(xml_list, columns=col_name)
        # print(xml_df)
        xml_df.to_csv('sfp_info_0401.csv', index=None)
        # count=int(xml_df.shape[0])
        print('解析{}完成,共计{}行'.format(xml_file.split('_')[2],xml_df.shape[0]))


def main():


    path = ('D:\\Python_WS\\NW\\sfp')
    sfpinfo(path)

if __name__ == '__main__':
    main()
