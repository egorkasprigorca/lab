# news-top-stories__others-inner-hider

from lxml import html
import requests
import sqlite3

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

URL = "https://lenta.ru"

class Record:
    title: str
    link: str

def main():
    conn = sqlite3.connect("lab3/db.db")
    cursor = conn.cursor()
    cursor.execute("drop table records;")
    cursor.execute('''
    CREATE TABLE records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT NOT NULL,
        title TEXT NOT NULL,
        link TEXT NOT NULL,
        date datetime NOT NULL
    );
    ''')
    text = requests.get(url=URL, headers=headers).text
    tree = html.fromstring(text)
    top_news = tree.xpath("//div[@class='topnews']")
    for div in top_news:
        links = div.xpath(".//a[@class='card-mini _topnews']/@href")
        titles = div.xpath(".//h3[@class='card-mini__title']")
        times = div.xpath(".//time[@class='card-mini__info-item']")
        for link, title, time in zip(links, titles, times):
            title = title.text_content()
            link = f"{URL}/{link}"
            _text = requests.get(url=link, headers=headers).text
            _tree = html.fromstring(_text)
            source = _tree.xpath("//a[@class='topic-authors__author']")[0].text_content()
            time = _tree.xpath("//a[@class='topic-header__item topic-header__time']")[0].text_content()
            cursor.execute('''
            INSERT INTO records (source, title, link, date) VALUES (?, ?, ?, ?);
            ''', (source, title, link, time))
            print(f"Title: {title}, Link: {link}, Time: {time}, Source: {source}")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()