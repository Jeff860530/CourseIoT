import requests, time
import csmapi, DAN
from datetime import datetime as dt##

ServerURL = 'https://6.iottalk.tw' #Change to your IoTtalk IP or None for autoSearching
Reg_addr='getAlias-Default' # if None, Reg_addr = MAC address

DAN.profile['dm_name']='Timer0858611'
DAN.profile['df_list']=['Timer0858611',]
#DAN.profile['d_name']= 'Assign a Device Name' 
light = 0
DAN.device_registration_with_retry(ServerURL, Reg_addr)

while 1:
    try:
        alias = DAN.get_alias('Timer0858611')
        if 1:#alias != []:
            TimeStr2 = dt.now().strftime('%H:%M:%S')
            TimeObj2 = dt.strptime(TimeStr2,'%H:%M:%S')
            print("TimeObj2:",TimeObj2)
            
            StrList = alias[0].split('~')
            TimeObj5 = dt.strptime(StrList[0],'%H:%M:%S')
            print("star time",TimeObj5)
            TimeObj6 = dt.strptime(StrList[1],'%H:%M:%S')
            print("end time",TimeObj6)
            if (TimeObj2>TimeObj5 and TimeObj2<TimeObj6 and light != 1 ):
                light = 1
                print(light)
                DAN.push("Timer0858611",1)
            if (TimeObj2>TimeObj6 and light != 0 ):
                light = 0
                print(light)
                DAN.push("Timer0858611",0)
    except Exception as e:
        print(e)


    time.sleep(1)