import requests
from bs4 import BeautifulSoup
import time

print("뉴스 크롤링 중 . . .")

today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
clock = time.strftime('%H:%M 기준', time.localtime(time.time()))

url = 'https://news.naver.com/main/home.nhn'
raw = requests.get(url, headers={'User-Agent': 'Chrome/89.0.4389.90'})
html = BeautifulSoup(raw.text, 'html.parser')

hd_articles  = html.select("ul.hdline_article_list > li")
articles = html.select("ul.mlist2.no_bg > li")
file = open(today + '.txt', 'w', -1, "utf-8")

file.write(clock + "\n\n")

file.write("헤드라인 뉴스)\n")
for i in range(0, len(hd_articles)):
    title = hd_articles[i].select_one("div.hdline_article_tit > a").text
    file.write(str(title).strip() + "\n")
    
    link = hd_articles[i].select_one('div.hdline_article_tit > a').attrs["href"]
    file.write("https://news.naver.com/" + str(link) + "\n")
    
    file.write("\n")
file.write("-" * 40 + "\n")

file.write("정치)\n")
for i in range(0, 5):
    title = articles[i].select_one("a").text
    file.write(str(title).strip() + "\n")
    
    link = articles[i].select_one('a').attrs["href"]
    file.write(str(link) + "\n")
    
    file.write("\n")
file.write("-" * 40 + "\n")

file.write("경제)\n")
for i in range(5, 10):
    title = articles[i].select_one("a").text
    file.write(str(title).strip() + "\n")
    
    link = articles[i].select_one('a').attrs["href"]
    file.write(str(link) + "\n")
    
    file.write("\n")
file.write("-" * 40 + "\n")

file.write("사회)\n")
for i in range(10, 15):
    title = articles[i].select_one("a").text
    file.write(str(title).strip() + "\n")
    
    link = articles[i].select_one('a').attrs["href"]
    file.write(str(link) + "\n")
    
    file.write("\n")
file.write("-" * 40 + "\n")

file.write("생활/문화)\n")
for i in range(15, 20):
    title = articles[i].select_one("a").text
    file.write(str(title).strip() + "\n")
    
    link = articles[i].select_one('a').attrs["href"]
    file.write(str(link) + "\n")
    
    file.write("\n")
file.write("-" * 40 + "\n")

file.write("세계)\n")
for i in range(20, 25):
    title = articles[i].select_one("a").text
    file.write(str(title).strip() + "\n")
    
    link = articles[i].select_one('a').attrs["href"]
    file.write(str(link) + "\n")
    
    file.write("\n")
file.write("-" * 40 + "\n")

file.write("IT/과학)\n")
for i in range(25, 30):
    title = articles[i].select_one("a").text
    file.write(str(title).strip() + "\n")
    
    link = articles[i].select_one('a').attrs["href"]
    file.write(str(link) + "\n")
    
    file.write("\n")
file.write("-" * 40 + "\n")

print("크롤링 완료 ! ! !")
file.close()

