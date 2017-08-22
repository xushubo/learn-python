#coding=utf-8
import re
import requests

url = 'https://s.taobao.com/search'
payload = {'q': 'python','s': '1','ie':'utf8'}  #字典传递url参数    
title_list = []
price_list = []
sales_list = []
nick_list = []

with open('taobao_test.txt','w',encoding='utf-8') as file:

    for k in range(0,2):        #2次，就是2个页的商品数据

        payload ['s'] = 44*k+1   #此处改变的url参数为s，s为1时第一页，s为45是第二页，89时第三页以此类推                          
        resp = requests.get(url, params=payload)
        print('visiting:', resp.url)          #打印访问的网址
        resp.encoding = 'utf-8'  #设置编码
        title = re.findall(r'"raw_title":"([^"]+)"', resp.text)  #正则保存所有raw_title的内容，这个是书名，下面是价格，地址
        price = re.findall(r'"view_price":"([^"]+)"', resp.text)    
        loc = re.findall(r'"item_loc":"([^"]+)"', resp.text)
        sales = re.findall(r'"view_sales":"(\d+)[^"]+"', resp.text)
        fee = re.findall(r'"view_fee":"([^"]+)"', resp.text)
        nick = re.findall(r'"nick":"([^"]+)"', resp.text)
        x = len(title)           #每一页商品的数量

        for i in range(0,x) :    #把列表的数据保存到文件中
            file.write(str(k*44+i+1)+'书名：'+title[i]+'\n'+'价格：'+price[i]+'\n'+'销量：'+sales[i]+'\n'+'邮费:'+fee[i]+'\n'+'店名：'+nick[i]+'\n'+'地址：'+loc[i]+'\n\n')
            title_list.append(title[i])
            price_list.append(price[i])
            sales_list.append(int(sales[i]))
            nick_list.append(nick[i])

sales_top = sales_list[0]
sales_top_index = 0
for i in range(0, len(sales_list)):
    if sales_list[i]>sales_top:
        sales_top = sales_list[i]
        print(sales_top)
        sales_top_index = i
print('最畅销书本：', title_list[sales_top_index], '销量：', sales_top)