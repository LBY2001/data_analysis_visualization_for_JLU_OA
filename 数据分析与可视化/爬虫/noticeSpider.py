# -*- coding: utf-8 -*-
"""
 * Description: 
 * @author: xiaobudian
 * @date: 2022.03.02
"""
import requests
from lxml import html
import jieba
import wordcloud
import numpy as np
from PIL import Image
import pandas as pd

### html加载
url = "https://webvpn.jlu.edu.cn/https/77726476706e69737468656265737421fff60f962b2526557a1dc7af96/defaultroot/PortalInformation!jldxList.action"

headers = {
    'Cookie': 'show_vpn=0; heartbeat=1; show_faq=0; wengine_vpn_ticketwebvpn_jlu_edu_cn=2dc6df5e2ddd8796; refresh=1',
    'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 98.0.4758.102Safari / 537.36',
}

###文本爬取
etree = html.etree
page = 1;

# 可选取网站页数，每页30条通知
noticeList1 = []
noticeList2 = []
noticeList3 = []
for i in range(417):
    params = {
        "channelId": "179577",
        "startPage": page
    }
    resp = requests.get(url, headers=headers, params=params)
    resp.encoding = "utf-8"

    # 通知内容
    html = etree.HTML(resp.text)
    divs = html.xpath("/html/body/form/div/div[1]/div[1]/div/div[3]/div[1]/div")
    for div in divs:
        notice = div.xpath("a[1]/text()")
        temp = ''.join(notice)
        noticeList1.append(temp)
        print(temp)

    # 通知部门
    divs = html.xpath("/html/body/form/div/div[1]/div[1]/div/div[3]/div[1]/div")
    for div in divs:
        notice = div.xpath("a[2]/text()")
        temp = ''.join(notice)
        noticeList2.append(temp)

    # 通知时间
    divs = html.xpath("/html/body/form/div/div[1]/div[1]/div/div[3]/div[1]/div")
    noticeList = []  # 通知列表
    for div in divs:
        notice = div.xpath("span/text()")
        temp = ''.join(notice)
        noticeList3.append(temp)

    page = page + 1

dict1 = {"通知内容" : noticeList1}
dict2 = {"通知部门" : noticeList2}
dict3 = {"通知时间" : noticeList3}
dict2.update(dict3)
dict1.update(dict2)

df = pd.DataFrame(dict1)
print(df)
df.to_csv('../time_dist/result.csv', encoding='utf_8_sig')

resp.close()

