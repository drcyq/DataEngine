# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:12:00 2020

@author: DongRunchao
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 得到页面的内容
def get_page_content(request_url):
    #设置headers头部
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(request_url,headers=headers,timeout=10)
    content = html.text
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def analysis(soup):
    # 找到所有的评论模块
    div_data = soup.find_all('div',class_='search-result-list-item')
    df=pd.DataFrame(columns=['名称','价格区间','产品图片链接'])
    temp={}
    for com in div_data:
        #用户名
        carname = com.find('p',class_='cx-name text-hover').get_text()
        temp['名称']=carname
        price = com.find('p',class_='cx-price').get_text()
        temp['价格区间']=price        
        picurl = com.find('img',class_='img')['src']
        temp['产品图片链接']=picurl            
        
        df=df.append(temp,ignore_index=True)

    return df

#主函数  
base_url = 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8'
soup = get_page_content(base_url)
if __name__ == '__main__':
    df = analysis(soup)
    print("yiche crab finish") 
    df.to_csv("易车网大众品牌汽车.csv",index=False)
