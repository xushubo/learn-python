#coding=utf-8
import re
import requests

url = 'https://s.taobao.com/search'
payload = {'q': 'python','s': '1','ie':'utf8'}  #字典传递url参数    
file = open('taobao_test1.txt','w',encoding='utf-8')

for k in range(0,1):        #100次，就是100个页的商品数据

    payload ['s'] = 44*k+1   #此处改变的url参数为s，s为1时第一页，s为45是第二页，89时第三页以此类推                          
    resp = requests.get(url, params=payload)
    print(resp.url)          #打印访问的网址
    #resp.encoding = 'utf-8'  #设置编码
    file.write(resp.text)
file.close()