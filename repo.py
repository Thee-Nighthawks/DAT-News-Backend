from bson import ObjectId
from model import News, NewsType
from utils.exception import UnknownDBError
from config import *
from datetime import datetime

class NewsRepo():
    @staticmethod
    async def insert(news: News):
        datefmt = datetime.today()
        # datefmt= datetime(int(year), int(month), int(date))
        newspaper = {
            'nele': news.nele,
            'title' : news.title,
            'date' : datefmt,
            'author' : news.author,
            'body' : news.body,
            'audio': news.audio,
            'link': news.link,
            'comment' : news.comment,
            'sentiment' : news.sentiment
        }

        try:
            await database[NEWS_DB_NAME].get_collection(NEWS_COL_NAME).insert_one(newspaper)
            return {
                'successful': 'true'
            }
        except:
            return {
                'successful': 'false'
            }
        
    @staticmethod
    async def delete(id: str):
        try:
            await database[NEWS_DB_NAME].get_collection(NEWS_COL_NAME).delete_one({"_id": ObjectId(id)})
            return {
                'successful': 'true'
            }
        except:
            return {
                'successful': 'false'
            }

    @staticmethod
    async def update(id: str, typeOf: str, value: str):
        ob = {typeOf: value}
        try:
            await database.get_collection(NEWS_COL_NAME).update_one({"_id": ObjectId(id)}, {"$set": {ob}})   
            return {
                'successful': 'true'
            }     
        except: 
            return {
                'successful': 'false'
            }

    # @staticmethod
    # async def newspaperAlign(id: str):
    #     pass

    @staticmethod
    async def fetch(id: str):
        res = {}
        agg = [{ '$match': { '_id': ObjectId(id) } }]
        try:
            lis = database[NEWS_DB_NAME][NEWS_COL_NAME].aggregate(agg)
        except:
            raise UnknownDBError("find")
        async for do in lis:
            try:
                res = do
                res['successful'] = 'true'
            except Exception:
                res['successful'] = 'false'
        return res
    
    @staticmethod
    async def fetchAll():
        dets = []
        try:
            log = database[NEWS_DB_NAME].get_collection(NEWS_COL_NAME).find()
        except:
            return {
                'successful': 'false'
            }
        try:
            async for ar in log:
                det = {}
                det['nele'] = ar['nele']
                det['title'] = ar['title']
                det['date'] = ar['date']
                det['author'] = ar['author']
                det['body'] = ar['body']
                det['audio'] = ar['audio']
                det['link'] = ar['link']
                det['comment'] = ar['comment']
                det['sentiment'] = ar['sentiment']
                dets.append(det)
            return {'successful': 'true', 'detail': dets}
        except Exception:
            return {'successful': 'false'}

    @staticmethod
    async def search(details: str):
        rep=[]
        detail = '|'.join([".*" + wo + ".*" for wo in details])
        agg = [{'$match': { '$or': [ {'title': { '$regex': detail }}, {'body': { '$regex': detail }} ] }}]
        try:
            lisee = database[NEWS_DB_NAME].get_collection(NEWS_COL_NAME).aggregate(agg) #find
        except Exception as e:
            return {'successful': 'false'}
        try:
            async for do in lisee:
                res = {}
                res['nele'] = do['nele']
                res['title'] = do['title']
                res['date'] = do['date']
                res['author'] = do['author']
                res['body'] = do['body']
                res['audio'] = do['audio']
                res['link'] = do['link']
                res['comment'] = do['comment']
                res['sentiment'] = do['sentiment']
                rep.append(res)
            return {'successful': 'true', 'detail': rep}
        except Exception as e:
            print(e)
            return {'successful': 'false'}