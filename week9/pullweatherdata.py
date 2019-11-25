import time, random, requests
import DAN

ServerURL = 'https://6.iottalk.tw'      #with non-secure connection
#ServerURL = 'https://DomainName' #with SSL connection
Reg_addr = 'haha' #if None, Reg_addr = MAC address

DAN.profile['dm_name']='Dummy_Device'
DAN.profile['df_list']=['Dummy_Control',]
#DAN.profile['d_name']= 'Assign a Device Name' 

DAN.device_registration_with_retry(ServerURL, Reg_addr)
while True:
    try:
        ODF_data = DAN.pull('Dummy_Control')#Pull data from an output device feature "Dummy_Control"
        if ODF_data != None:
            ODF_data = ODF_data[0].split('$')
            # '溫度：+args[0]+"°C"+"濕度："+args[1]+"風力："+args[2]+"陣風："+args[3]+"雨量："+args[4]+"風向："+args[5]
            print('溫度：{0}°C 濕度：{1}風力：{2} 陣風：{3}雨量：{4} 風向：{5}'.format(ODF_data[0],ODF_data[1],ODF_data[2],ODF_data[3],ODF_data[4],ODF_data[5]))
    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

    time.sleep(0.2)