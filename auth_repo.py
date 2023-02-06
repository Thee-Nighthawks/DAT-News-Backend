from hashlib import sha256
from utils.admin import mailContent
from config import *
# from datetime import datetime
from utils.authentication import *
from model import *


class Auth():
    @staticmethod
    async def register(register: Register):
        log = {
            'mail': register.mail,
            'pass': str(sha256(str(register.password).encode()).hexdigest()),
            'name': register.name,
            'age': register.age,
            'gender': register.gender,
            'admin': register.admin,
            'verified': 'false'
        }
        try:
            authenticator[AUTH_DB_NAME].get_collection(AUTH_COL_NAME).insert_one(log)
            return {
                'successful': 'true',
                'otp': await email(register.name, register.mail) 
            }
        except Exception as e:
            print(e)
            return {
                'successful': 'false',
                # 'otp': await email(register.name, register.mail) 
            }
    
    @staticmethod
    async def login(login: Login):
        agg = [{'$match': {'mail':{'$eq': login.mail}, 'pass':{'$eq': str(sha256(str(login.password).encode()).hexdigest())}}}]
        try:
            log = authenticator[AUTH_DB_NAME].get_collection(AUTH_COL_NAME).aggregate(agg)
        except Exception:
            return {
                'login': 'false'
            }
        async for ar in log:
            return {'login': 'true', 'name': ar['name']}
        return {'login': 'false'}
    
    @staticmethod
    async def checkMail(mail: str):
        agg = [{'$match': {'mail':{'$eq': mail}}}]
        try:
            log = authenticator[AUTH_DB_NAME].get_collection(AUTH_COL_NAME).aggregate(agg)
        except:
            return {
                'available': 'false'
            }
        # print(log)
        async for ar in log:
            # print(ar)
            return {'available': 'true'}
        return {'available': 'false'}
    
    @staticmethod
    async def verifyMail(mail: str):
        try:
            authenticator[AUTH_DB_NAME].get_collection(AUTH_COL_NAME).update_one({'mail': mail.replace('%40', '@') if '%40' in mail else mail}, {"$set": {'verified': 'true'}})
            return {'verified': 'true'}
        except:
            return {
                'verified': 'false'
            }
        # return {'verified': 'false'}
    

    # Admin
    @staticmethod
    async def getUsers():
        dets = []
        try:
            log = authenticator[AUTH_DB_NAME].get_collection(AUTH_COL_NAME).find()
        except:
            return {
                'successful': 'false'
            }
        async for ar in log:
            det = {}
            det['mail'] = ar['mail']
            det['name'] = ar['name']
            det['age'] = ar['age']
            det['gender'] = ar['gender']
            dets.append(det)
        return {'successful': 'true', 'detail': dets}

    @staticmethod
    async def mailAll(subject: str, content: str):
        try:
            log = authenticator[AUTH_DB_NAME].get_collection(AUTH_COL_NAME).find()
        except:
            return {
                'successful': 'false'
            }
        async for ar in log:
            await mailContent(ar['mail'], subject, content)
        return {'successful': 'true'}