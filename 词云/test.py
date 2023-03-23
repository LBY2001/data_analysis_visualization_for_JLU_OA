# -*- coding: utf-8 -*-
"""
 * Description:
 * @author: xiaobudian
 * @date: 2022.03.01
"""
import requests
from lxml import html
import jieba
import wordcloud
import numpy as np
from PIL import Image
import pandas as pd

# ### html加载
# url = "https://webvpn.jlu.edu.cn/https/77726476706e69737468656265737421fff60f962b2526557a1dc7af96/defaultroot/PortalInformation!jldxList.action"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
#     "Cookie" : "show_vpn=0; heartbeat=1; show_faq=0; wengine_vpn_ticketwebvpn_jlu_edu_cn=54dd5337db7bfc7f; remember_token=HAKEhEUsKUTWWuEwzZaKtLyVTwLJRgDbenFwGCjZpcXttChwcLLkaDacrjxeDTPF; refresh=1"
# }
#
# ###文本爬取
# etree = html.etree
# page = 1;
# #
# # # 可选取网站页数，每页30条通知
# # for i in range(417):
# #     params = {
# #         "channelId": "179577",
# #         "startPage": page
# #     }
# #     resp = requests.get(url, headers=headers, params=params)
# #     resp.encoding = "utf-8"
# #     noticeList = []  # 通知文本列表
# #
# #     html = etree.HTML(resp.text)
# #     divs = html.xpath("/html/body/form/div/div[1]/div[1]/div/div[3]/div[1]/div")
# #     for div in divs:
# #         notice = div.xpath("a[1]/text()")
# #         temp = ''.join(notice)
# #         noticeList.append(temp)
# #         print(temp)
# #     page = page + 1
# # resp.close()

###词云生成
jieba.add_word("鼎新")
jieba.add_word("学年")

read_csv = pd.read_csv('../数据分析与可视化/time_dist/result.csv')
noticeList = []
for i in range(len(read_csv)):
    noticeList.append((read_csv['通知内容'][i]))

results = " ".join(noticeList)
words = jieba.lcut(results) #words列表

# wordCloud停用词
stopwords = set(wordcloud.STOPWORDS)
stopwords.add("关于")
stopwords.add("通知")
stopwords.add("吉林大学")
stopwords.add("及")
stopwords.add("各")
stopwords.add("的")
stopwords.add("处")
stopwords.add("年")
stopwords.add("等")
stopwords.add("与")
stopwords.add("日")
#

pic = np.array(Image.open("../数据分析与可视化/time_dist/吉大校徽.png"))
w = wordcloud.WordCloud(font_path="../数据分析与可视化/time_dist/msyh.ttf", mask=pic, background_color="white", stopwords=stopwords)
w.generate(" ".join(words))
w.to_file("../数据分析与可视化/成果图/通知词云.png")

