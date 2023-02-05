# import asyncio
import requests
import nltk
# import pyttsx3
from newspaper import Article
from textblob import TextBlob
from repo import NewsRepo
import xml.etree.ElementTree as ET
from config import RSSList
from model import News
from datetime import datetime

DOWNLOAD = "./DOWNLOAD/"

headers = {'User-agent': 'Mozilla/5.0'}

async def newsContent():
    try:
        for news in RSSList:
            response = requests.get(news)
            root = ET.fromstring(response.text)
            links = [(item.find("link").text).replace(' ', '') for item in root.findall("./channel/item")]
            for i in links:
                article = Article(i)
                try:
                    article.download()
                    article.parse()
                    article.nlp()
                    analysis = TextBlob(article.text)
                    # audio = newsAudio(article.title, article.summary)
                    # print(article.images)
                    nws = News(nele=RSSList.index(news), date=datetime.today(),title=article.title, author=({} if article.authors is None else article.authors), body=article.summary, link=i, comment={}, sentiment=(1 if analysis.polarity > 0 else (3 if analysis.polarity < 0 else 2)))
                    await NewsRepo.insert(nws)
                except Exception:
                    pass
        return {
            'successful': True
        }
    except Exception as e:
        print(e)

    

# async def newsAudio(title:str, text: str):
#     try:
#         reader = pyttsx3.init()
#         reader.setProperty("rate", 120)
#         voices = reader.getProperty('voices')
#         reader.setProperty("voice", voices[1].id)
#         # print(str(title.replace(' ', '-')))
#         reader.save_to_file(text, f"{DOWNLOAD}/audio.mp3")
#         reader.runAndWait()
#     except Exception as e:
#         print(e)

# newsContent("https://www.indiatoday.in/rss/home")

# if __name__ == "__main__":
#     asyncio.run(newsContent())
    # asyncio.run(newsAnalyser("https://www.indiatoday.in/business/budget-2023/story/how-much-income-tax-do-you-pay-now-under-new-tax-regime-quick-guide-2329102-2023-02-01"))
    # test = "Finance Minister Nirmala Sitharaman on Wednesday revised the existing income tax slabs to provide some relief to the salaried class by announcing that no tax would be levied on annual income of up to Rs 7 lakh under the new tax regime. She also tweaked the concessional tax regime by hiking the tax exemption limit by Rs 50,000 to Rs 3 lakh. Under the revamped concessional tax regime, no tax would be levied for income up to Rs 3 lakh."
    # asyncio.run(newsAudio("Budget 2023 How much income tax do you pay now under new tax regime? Quick guide", test))
