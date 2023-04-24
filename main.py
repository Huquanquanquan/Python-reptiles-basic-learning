
# 请求模块
import requests
# 解析数据模块
from lxml import etree

# //   : 根目录
# []   : 谓语条件
# /    : 选择元素
# @    : 提取元素

# url地址
url = 'https://yz.chsi.com.cn/kyzx/zcdh/'

# 请求url地址    404 出错  302 重定向
html = requests.get(url).text

# 解析数据
doc = etree.HTML(html)
# 提取链接元素
href_url = doc.xpath('//ul[@class="news-list"]/li/a/@href')

for qianzui in href_url:
    # 拼接前缀
    new_url = 'https://yz.chsi.com.cn' + qianzui

    # 再次发起网络请求
    html_2 = requests.get(new_url).text

    # 抓取
    # 标题

    doc2 = etree.HTML(html_2)
    biaoti = doc2.xpath('//div[@class="title-box"]/h2/text()')

    print(biaoti)


