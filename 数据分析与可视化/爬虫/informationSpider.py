import requests
import os
#from bs4 import BeautifulSoup
from lxml import etree
import wordcloud
import csv
import matplotlib.pyplot as plt
if __name__ == '__main__':
    #xpath 最常用最便捷 用路径
    #etree 实例化etree对象 将被解析的页面原码加载到该对象中
    #etree 方法结合xpath表达式实现定位
    list=['美国', '日本', '韩国', '英国', '俄罗斯', '加拿大', '澳大利亚', '德国', '新加坡']
    list1=['美国', '日本', '韩国', '英国', '俄罗斯', '加拿大', '德国','澳大利亚', '新加坡','法国','荷兰','西班牙','乌克兰','意大利','朝鲜','以色列','瑞典','泰国','奥地利','蒙古国','丹麦','瑞士','比利时','印度','马来西亚','挪威','阿根廷','芬兰','波兰','爱尔兰','捷克','巴西','印度尼西亚','希腊','葡萄牙','匈牙利','越南','白俄罗斯','南非','墨西哥','埃及','冰岛','斯里兰卡','斯洛伐克','保加利亚','柬埔寨','赞比亚','尼泊尔','立陶宛','秘鲁','伊拉克','菲律宾','哈萨克斯坦','也门','爱沙尼亚','埃塞俄比亚','卢森堡','尼日利亚','约旦','乍得','摩洛哥','拉脱维亚','塞尔维亚','阿曼']
    list2=['南岭校区','朝阳校区','南湖校区','新民校区','和平校区','前卫南区','前卫北区']
    list_ans=[]
    headers = {
        'Cookie':'Cookie: show_vpn=0; heartbeat=1; show_faq=0; wengine_vpn_ticketwebvpn_jlu_edu_cn=769f35c4961e5ded; refresh=0',
        'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 98.0.4758.102Safari / 537.36',
    }
    f=open('../time_dist/国家(1).csv',mode='w',encoding='utf-8',newline='')
    writer = csv.writer(f)
    writer.writerow(['country','number'])
    for s in list1:
        #print(s)
        url='https://webvpn.jlu.edu.cn/https/77726476706e697374686562657374' \
            '21fff60f962b2526557a1dc7af96/defaultroot/PortalInformation!' \
            'jldxList.action?searchnr=' \
            ''+s+'&searchlx=0&pagerURL=%3F1%3D1%26searchnr' \
            '%3D%25E5%2581%259C%25E6%25B0%25B4%26searchlx%3D0'
        response=requests.get(url=url,headers=headers)
        page_text=response.text
        tree=etree.HTML(page_text)
        str1=tree.xpath('//*[@id="rightIframe"]/div/div[3]/div[2]/table/tr/td/table/tr/td[2]/text()[2]')
        str2=str(str1)
        str3=''
        num=0
        flag=False
        for c in str2:
            #print(c)
            num=num+1
            if(num==16 and c!='0'):
                flag=True
            if(num==17):
                flag=True
            if(c=='\\' and flag==True):
                break
            if(flag==True):
                str3=str3+c
        a=int(str3)
        list_ans.append(a)
        print(s,str3)
        #writer.writerow([s,a])
        writer.writerow([s,str3])
    f=open('../time_dist/校区.csv',mode='w',encoding='utf-8',newline='')
    writer = csv.writer(f)
    writer.writerow(['Campus','Number'])
    for s in list2:
        #print(s)
        url='https://webvpn.jlu.edu.cn/https/77726476706e697374686562657374' \
            '21fff60f962b2526557a1dc7af96/defaultroot/PortalInformation!' \
            'jldxList.action?searchnr=' \
            ''+s+'&searchlx=0&pagerURL=%3F1%3D1%26searchnr' \
            '%3D%25E5%2581%259C%25E6%25B0%25B4%26searchlx%3D0'
        response=requests.get(url=url,headers=headers)
        page_text=response.text
        tree=etree.HTML(page_text)
        str1=tree.xpath('//*[@id="rightIframe"]/div/div[3]/div[2]/table/tr/td/table/tr/td[2]/text()[2]')
        str2=str(str1)
        str3=''
        num=0
        flag=False
        for c in str2:
            #print(c)
            num=num+1
            if(num==16 and c!='0'):
                flag=True
            if(num==17):
                flag=True
            if(c=='\\' and flag==True):
                break
            if(flag==True):
                str3=str3+c
        a=int(str3)
        list_ans.append(a)
        print(s,str3)
        #writer.writerow([s,a])
        writer.writerow([s,str3])