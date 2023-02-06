from bson import ObjectId
from model import News, NewsType
# from utils.exception import UnknownDBError
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
        except Exception:
            return {
                'successful': 'false'
            }

    @staticmethod
    async def update(id: str, typeOf: str, value: str, **kwargs):
        ob = {}
        # ob[typeOf] = value
        try:
            for key, vale in kwargs.items():
                if key == "link":
                    link = vale
            if (typeOf == "author"):
                rt = database[NEWS_DB_NAME].get_collection(NEWS_COL_NAME).aggregate([{ '$match': { '_id': ObjectId(id) } }])  
                arr = [] if [rt['author'] async for rt in rt] == [None] else [rt['author'] async for rt in rt]
                arr.append({value: link})
                ob[typeOf] = arr
                print(ob)
            elif (typeOf == "comment"):
                rt = database[NEWS_DB_NAME].get_collection(NEWS_COL_NAME).aggregate([{ '$match': { '_id': ObjectId(id) } }])  
                arr = [] if [rt['comment'] async for rt in rt] == [None] else [rt['comment'] async for rt in rt]
                arr.append({value: link})
                ob[typeOf] = arr
                print(ob)
            else:
                ob[typeOf] = value
            await database[NEWS_DB_NAME].get_collection(NEWS_COL_NAME).update_one({"_id": ObjectId(id)}, {"$set": ob})   
            return { 'successful': 'true' }     
        except Exception as e: 
            print(e)
            return { 'successful': 'false'}

    # @staticmethod
    # async def newspaperAlign(id: str):
    #     pass

    @staticmethod
    async def fetch(id: str):
        agg = [{ '$match': { '_id': ObjectId(id) } }]
        try:
            lis = database[NEWS_DB_NAME].get_collection(NEWS_COL_NAME).aggregate(agg)
        except Exception as e:
            print(e)
        try:
            async for do in lis:
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
            return {'successful': 'true', 'detail': res}
        except Exception:
            return {'successful': 'false'}
    
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