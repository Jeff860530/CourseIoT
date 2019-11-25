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
print("陣風：",df_tmp[0][5])
print("濕度：",df_tmp[0][8])
print("雨量：",df_tmp[0][10])

'''
#########################################################################################
import pandas as pd
print ('Region :', region,'Building table ...')
col_list = ['觀測時間', '溫度(°C)', '溫度(°F)', '天氣', '風向', '風力 (m/s)|(級)', '陣風 (m/s)|(級)', '能見度(公里)', '相對溼度(%)', '海平面氣壓(百帕)', '當日累積雨量(毫米)', '日照時數(小時)']
df = pd.DataFrame(columns = col_list)
df_tmp = pd.DataFrame(df_tmp)
df_tmp.columns = col_list
df = pd.concat([df, df_tmp], axis=0)   
df = df.reset_index(drop=True)    
#print(df)
temperature = df['溫度(°C)'][1]
print("日期：",df['觀測時間'][0])
print("溫度：",df['溫度(°C)'][0])

print("風向：",df['風向'][1])
print("風力：",df['風力 (m/s)|(級)'][0])
print("陣風：",df['風力 (m/s)|(級)'][0])
print("濕度：",df[ '相對溼度(%)'][0])
print("雨量：",df['當日累積雨量(毫米)'][0])

df.to_csv(( region + '.csv'), encoding = 'utf-8')
'''