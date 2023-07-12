import requests
from bs4 import BeautifulSoup
import time
import webbrowser
import os

### 현재 시각을 불러옵니다. ###
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
clock = time.strftime('%H:%M 기준', time.localtime(time.time()))

url = 'https://news.naver.com/main/home.nhn'
raw = requests.get(url, headers={'User-Agent': 'Chrome/89.0.4389.90'})
html = BeautifulSoup(raw.text, 'html.parser')

hd_articles  = html.select("ul.hdline_article_list > li")
articles = html.select("ul.mlist2.no_bg > li")

def printNews(idx):
    if(idx == 0):
        print("헤드라인)\n")
    elif(idx == 1):
        print("정치)\n")
    elif(idx == 2):
        print("경제)\n")
    elif(idx == 3):
        print("사회)\n")
    elif(idx == 4):
        print("생활/문화)\n")
    elif(idx == 5):
        print("세계)\n")
    elif(idx == 6):
        print("IT/과학)\n")

    if(idx == 0):
        for i in range (0, 5):
            print(i, end=") ")
            title = hd_articles[i].select_one("div.hdline_article_tit > a").text
            if(i == 4):
                print(str(title).strip())
            else:
                print(str(title).strip() + "\n")
    else:
        for i in range(0, 5):
            print(i, end=") ")
            title = articles[(idx - 1) * 5 + i].select_one("a").text
            if(i == 4):
                print(str(title).strip())
            else:
                print(str(title).strip() + "\n")

def connectNews(newsIndex, category):
    if(category == 0):
        index = newsIndex
        link = hd_articles[index].select_one('div.hdline_article_tit > a').attrs["href"]
        link = "https://news.naver.com/" + str(link)

        webbrowser.open_new(link)
    else:
        index = (category - 1) * 5 + newsIndex
        link = articles[index].select_one('a').attrs["href"]
        
        webbrowser.open_new(str(link))


idx = 0
while True:
    os.system('cls')
    ### os.system('clear')

    print(today)
    print(clock)
    print("-" * 90)
    printNews(idx)
    print("-" * 90)

    print("q : quit, n : next, l : last, 0 ~ 4 : news index(connect)\n")
    userInput = input("type input: ")

    if(userInput == "q"):
        break
    elif(userInput == "n"):
        if(idx < 6):
            idx += 1
            continue
    elif(userInput == "l"):
        if(idx > 0):
            idx -= 1
            continue

    if(userInput.isalpha()):
        print("Invalid Input")
        time.sleep(1)
    elif(userInput.isnumeric()):
        userInput = int(userInput)
        if(0 <= userInput <= 4):
            connectNews(userInput, idx)
        else:
            print("Invalid Input")
            time.sleep(1)
    else:
        print("Invalid Input")
        time.sleep(1)
