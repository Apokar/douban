# 豆瓣读书  爬搜索页的书名及信息
import urllib.request
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['douban_db']
data = db['data']

# 清空数据库，避免数据重复
db.data.drop()
# 存放爬出的内容
datalist = []
# 存放要爬的网址 list 集
urls = []

# 豆瓣搜索页
for i in (0, 15, 30, 45):
    urls.append(
        'https://book.douban.com/subject_search?start=' + str(i) + '&search_text=%E8%9D%99%E8%9D%A0%E4%BE%A0&cat=1001')

for url in urls:
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req).read().decode('UTF-8')

    soup = BeautifulSoup(res, 'html.parser')

    for res in soup.select('.subject-item'):
        title = res.find('h2').text.strip()
        info = res.select('.pub')[0].text.strip()
        result = {'title': title, 'info': info}
        datalist.append(result)

data.insert_many(datalist)
