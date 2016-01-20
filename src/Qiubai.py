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
page = 1
url = 'http://www.qiushibaike.com/8hr/page/'
fp = open('qiubai.txt', 'a+')

for i in range(0, 8):
    page += i
    url = '{0}{1}'.format(url, page)
    fp.write('Page {0}:\n'.format(page))

    httpHead = {'user-agent':'Googlebot/2.1 (http://www.googlebot.com/bot.html)'}
    request = urllib2.Request(url, headers=httpHead)
    html = urllib2.urlopen(request)
    htmlContent = html.read() #.decode('utf-8')
    
    #pattern = re.compile('<div class="content">(.*?)<!--\d*-->', re.S) #发布的正文
    pattern = re.compile('<div class="author.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)<!--\d*-->', re.S)
    items = pattern.findall(htmlContent)
    
    for item in items:
        #fp.write( item)
        
        fp.write('{0}: {1}\n'.format(item[0].strip(), item[1].strip()))
    
fp.close()

