import sys
import numpy
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
rootPath = sys.path[0]

def scraping():
    data = []
    urls = [
        "https://www.mapnews.ma/en/actualites/politics/moroccan-sahara-five-questions-vice-president-american-university-new-england",
        "https://www.mapnews.ma/en/actualites/politics/moroccanness-sahara-confirmed-fact-and-law-french-lawyer",
        "https://www.mapnews.ma/en/actualites/politics/international-platform-defense-and-support-moroccan-sahara-calls-international"
    ]
    for url in urls:
        req = Request(url, headers={'User-Agent': ''})
        html = urlopen(req).read()
        soup = BeautifulSoup(html, features="html.parser")
        news = soup.find('div', attrs={'class': 'node-tpl-corps'}).find_all('p')
        for p in news:
            data.append(p.text.replace("&shy", '').replace(";\xad","").replace("\xad","").replace(u'\xa0', '').replace(',','.'))
    df = pd.DataFrame(data)
    numpy.savetxt(rootPath+'/Scraping/data/trueData.txt', df.values, fmt='%s', encoding='utf-8')

    data = []
    urls = [
        "https://www.spsrasd.info/news/en/articles/2021/02/13/31112.html",
        "https://www.spsrasd.info/news/en/articles/2021/02/10/31057.html",
        "https://www.spsrasd.info/news/en/articles/2021/02/13/31105.html",
        "https://www.spsrasd.info/news/en/articles/2021/02/13/31107.html",
        "https://www.spsrasd.info/news/en/articles/2021/02/13/31102.html",
        "https://www.spsrasd.info/news/en/articles/2021/02/09/31022.html",
        "https://www.spsrasd.info/news/en/articles/2021/01/28/30678.html",
        "https://www.spsrasd.info/news/en/articles/2021/01/28/30676.html",
        "https://www.spsrasd.info/news/en/articles/2021/01/26/30629.html",
        "https://www.spsrasd.info/news/en/articles/2021/01/09/30252.html",
        "https://www.spsrasd.info/news/en/articles/2020/12/14/29674.html",
        "https://www.spsrasd.info/news/en/articles/2021/02/10/31058.html",
        "https://www.spsrasd.info/news/en/articles/2021/02/16/31220.html",
        "https://www.spsrasd.info/news/en/articles/2016/07/09/2931.html",
        "https://www.spsrasd.info/news/en/articles/2018/04/17/14981.html"
    ]
    for url in urls:
        req = Request(url, headers={'User-Agent': ''})
        html = urlopen(req).read()
        soup = BeautifulSoup(html, features="html.parser")
        news = soup.find('div', attrs={'class': 'field-item even', 'property': 'content:encoded'})
        txt = news.get_text()
        data.append(txt.replace(u'\xa0', '').replace('\n\n','').replace(',','.'))
    df = pd.DataFrame(data)
    numpy.savetxt(rootPath+'/Scraping/data/fakeData.txt', df.values, fmt='%s', encoding='utf-8')