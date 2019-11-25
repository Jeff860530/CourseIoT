import requests
import time
from io import open

region = 'Tainan'
url = 'https://www.cwb.gov.tw/V7/observe/24real/Data/46741.htm'


def f(url, fn):
	headers = {
     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
	}
	res = requests.get(url, headers=headers)
	res.encoding = 'utf-8'

	open(fn,'wb').write(res.text.encode('utf-8'))

fn = region+ '.html'.format(0,0)
f(url, fn)


from bs4 import BeautifulSoup

def get_element(soup, tag, class_name):
    data = []
    table = soup.find(tag, attrs={'class':class_name})
    rows = table.find_all('tr')
    del rows[0]
    
    for row in rows:
        first_col = row.find_all('th')
        cols = row.find_all('td')
        cols.insert(0, first_col[0])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) 
    return data

   
file_name = region+".html"

f = open (file_name,'r', encoding='utf-8')
s = f.readlines()
s = ''.join(s)

soup = BeautifulSoup(s, "lxml")

df_tmp = get_element(soup, 'table','BoxTable')

print(type(df_tmp))
print(df_tmp[0])
print("日期：",df_tmp[0][0])
print("溫度：",df_tmp[0][1])
print("風向：",df_tmp[0][4])
print("風力：",df_tmp[0][5])
print("陣風：",df_tmp[0][6])
print("濕度：",df_tmp[0][8])
print("雨量：",df_tmp[0][10])

import time, random, requests
import DAN

ServerURL = 'https://6.iottalk.tw'      #with non-secure connection
#ServerURL = 'https://DomainName' #with SSL connection
Reg_addr = 'xaxas' #if None, Reg_addr = MAC address

DAN.profile['dm_name']='0858611_weather'
DAN.profile['df_list']=['AtPressure', 'Humidity','Windspeed','presentwind','rain','winddirection']
#DAN.profile['d_name']= 'Assign a Device Name' 

DAN.device_registration_with_retry(ServerURL, Reg_addr)
#DAN.deregister()  #if you want to deregister this device, uncomment this line
#exit()            #if you want to deregister this device, uncomment this line

while True:
    try:
        DAN.push ('AtPressure', df_tmp[0][1])
        DAN.push ('Humidity', df_tmp[0][8])
        DAN.push ('Windspeed', df_tmp[0][5])
        DAN.push ('presentwind',df_tmp[0][6])
        DAN.push ('rain',df_tmp[0][10])
        DAN.push ('winddirection',df_tmp[0][4])

    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

    time.sleep(0.2)

