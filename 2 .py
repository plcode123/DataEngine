import requests
import pandas as pd
import numpy
from bs4 import BeautifulSoup
#请求URL
def get_page_content(request_url):
    url='http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-1.shtml'
    #伪装浏览器
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(request_url,headers=headers,timeout=10)
    # 通过content创建BeautifulSoup对象
    content=html.text
    soup=BeautifulSoup(content,'html.parser',from_encoding='utf-8')
    return soup
def analysis(soup):
    temp=soup.find('div',class_='tslb_b')
    #创建DataFrame
    # print(soup.title)
    df = pd.DataFrame(columns=['id','brand','car_model','type','desc','problem','datetime','status'])
    #找到表格里面的每一行
    tr_list=temp.find_all('tr')
    for tr in tr_list:
        #提取投诉信息
        temp = {}
        td_list=tr.find_all('td')
        #第一个tr 没有 td ，其余有8个td
        if len(td_list)>0:
            #解析各个字段内容
            id,brand,car_model,type,desc,problem,datetime,status=td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text
            temp['id'],temp['brand'],temp['car_model'],temp['type'],temp['desc'],temp['problem'],temp['datetime'],temp['status']= id,brand,car_model,type,desc,problem,datetime,status
            df=df.append(temp,ignore_index=True)
    return df
#df = analysis(soup)
#print(df)
page_num=3
base_url='http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
# 创建DataFrame
# print(soup.title)\
result = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
for  i in range(page_num):
    request_url=base_url+str(i+1)+'.shtml'
    soup=get_page_content(request_url)
    df=analysis(soup)
    print(df)
    result=result.append(df)
result.to_csv('result1.csv',index=False)