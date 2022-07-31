import requests
from bs4 import BeautifulSoup as Bs4
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import time
import html2text
import html2markdown

# 修改浏览器信息。python自带浏览器会被反爬虫
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

head_url = 'https://www.w3cschool.cn/hadoop' ## hadoop教程
# head_url = 'https://www.w3cschool.cn/hive_manual/' ## hive教程

requests.packages.urllib3.disable_warnings() #消除warning

response = requests.get(head_url, headers=headers,verify=False)
homepage = Bs4(response.text,"lxml")
# ele = soup.select("#nestable_handbook > ol > li:nth-child(1) > ol > li > div > a")
ele = homepage.select("li[class='dd-item']")[0]
ele = ele.select('a')

b= ele[5]
print(b.get('title'),b.findParent('ol').find_previous_sibling('div',class_='dd-content folder-open').findChild('a').get('title'))

# 新建md文件，方便后面写入。后面文件不覆盖文档
wnt = open(f'./hadoop笔记.md','w',encoding='utf-8')
wnt.close()

relation = {} # 用于定制标题等级

for i in ele:
    if i.get('href'):
        relation[i.get('title')] = ''
        suburl = head_url[:-len('/hadoop')] + i.get('href')
        print(suburl,i.get('title'))

        # 用于定制标题等级
        try:
            parent = i.findParent('ol').find_previous_sibling('div', class_='dd-content folder-open').findChild('a').get('title')
            if parent in relation.keys():
                relation[i.get('title')] = relation[parent] + '#'
        except:
            pass

        subhtml = requests.get(suburl, headers=headers,verify=False)
        soup = Bs4(subhtml.content,"lxml")
        cnt = soup.select("div[class='wkcontent']")

        # print(cnt[0].decode_contents())
        # break

        # with open(f"./hadoop笔记.md",'a',encoding='utf-8') as file:
        #     # a = cnt[0].get_text()
        #     # print(type(a))
        #     # while '\n' in a:
        #     #     a.remove('\n')
        #     file.write(f"\n\n #{relation[i.get('title')]} {i.get('title')} \n")
        #     file.write(html2markdown.convert(cnt[0].decode_contents()))

        # with open(f'./test.md','a',encoding='utf-8') as file:
        #     # file.write(f"# {i.get('title')}   ")
        #     file.write(html2markdown.convert(cnt[0].text))

        # ###### 模拟浏览器行为操作
        # br = webdriver.Chrome()
        # br.get(suburl)
        #
        # save_me = ActionChains(br).key_down(Keys.CONTROL) \
        #     .key_down('s').key_up(Keys.CONTROL).key_up('s')
        # save_me.perform()

