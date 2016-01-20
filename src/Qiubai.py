#!/usr/bin/python
#coding:utf-8

import sys
import re
import urllib, urllib2
'''
描述：抓取糗百首页发表的段子，没有考虑图片
问题：1. 解析出来有好多回车
2. 内容中的<br/>没有去掉
'''

url = 'http://www.qiushibaike.com/'
httpHead = {'user-agent':'Googlebot/2.1 (http://www.googlebot.com/bot.html)'}
request = urllib2.Request(url, headers=httpHead)
html = urllib2.urlopen(request)
htmlContent = html.read() #.decode('utf-8')

pattern = re.compile('<div class="content">(.*?)<!--\d*-->', re.S)
items = pattern.findall(htmlContent)
fp = open('qiubai.txt', 'a')
for item in items:
    fp.write( item)
    
fp.close()