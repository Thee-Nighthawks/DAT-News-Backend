from fastapi import APIRouter
from repo import NewsRepo
from auth_repo import Auth
from utils.article import newsContent
from utils.authentication import email
from utils.exception import UnknownDBError
from model import *
from typing import Union

router = APIRouter()


# Content based
# @router.post("/api/auth/register")
# async def add_content():
#     try:
#         # await newsContent()
#         return Response(code=200, status="Ok", message="Success added some data").dict(exclude_none=True)
#     except UnknownDBError: 
#         return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)


# Authorication based
@router.post("/api/auth/register")
async def auth_register(register: Register):
    try:
        # await newsContent()
        registerData = await Auth.register(register)
        return Response(code=200, status="Ok", message="Success save data", result=registerData).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)

@router.post("/api/auth/login")
async def auth_login(login: Login):
    try:
        # await newsContent()
        loginData = await Auth.login(login)
        return Response(code=200, status="Ok", message="Success checked the data", result=loginData).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)

@router.get("/api/auth/check-mail")
async def auth_check_mail(mail: str):
    try:
        # await newsContent()
        checkMail = await Auth.checkMail(mail)
        return Response(code=200, status="Ok", message="Success retrieve checked the mail", result=checkMail).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)

@router.get("/api/auth/verify-mail")
async def auth_verify_mail(mail: str):
    try:
        # await newsContent()
        verifyMail = await Auth.verifyMail(mail)
        return Response(code=200, status="Ok", message="Successfully verified the mail", result=verifyMail).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)

@router.post("/api/auth/verify-code")
async def auth_verify_mail(name: str, mail: str):
    try:
        # await newsContent()
        code = await email(name, mail)
        return Response(code=200, status="Ok", message="Successfully sent the code", result=code).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)


# Admin based
@router.get("/api/admin/all-user")
async def admin_all_user():
    try:
        # await newsContent()
        allUser = await Auth.getUsers()
        return Response(code=200, status="Ok", message="Success got all user", result=allUser).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)

@router.get("/api/admin/mail-all")
async def admin_mail_all(subject: str, content: str):
    try:
        # await newsContent()
        mailAll = await Auth.mailAll(subject, content)
        return Response(code=200, status="Ok", message="Success mailed all", result=mailAll).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)

@router.get("/api/admin/get-news")
async def admin_get_news():
    try:
        # await newsContent()
        newsletter = await newsContent()
        return Response(code=200, status="Ok", message="Success got all news", result=newsletter).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)


# News based 
@router.post("/api/news/insert")
async def insert(news: News):
    try:
        # await newsContent()
        res = await NewsRepo.insert(news)
        return Response(code=200, status="Ok", message="Success save data", result=res).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)

@router.post("/api/news/edit/{id}")
async def update(id:str, var:str, value:str, link: Union[str, None] = None):
    try:
        # await newsContent()
        if link != None:
            res = await NewsRepo.update(id, var, value, link=link)
        else:
            res = await NewsRepo.update(id, var, value)
        return Response(code=200, status="Ok", message="Success edited data", result=res).dict(exclude_none=True)
    except UnknownDBError:
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)

@router.delete("/api/news/delete/{id}")
async def delete(id:str):
    try:
        # await newsContent()
        res = await NewsRepo.delete(id)
        return Response(code=200, status="Ok", message="Success deleted data", result=res).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)

@router.get("/api/news/get/{id}")
async def fetch(id:str):
    try:
        # await newsContent()
        newspaper = await NewsRepo.fetch(id)
        return Response(code=200, status="Ok", message="Success retrieve the data", result=newspaper).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__, result=[]).dict(exclude_none=True)

@router.get("/api/news/get-all")
async def fetchAll():
    try:
        # await newsContent()
        newspaper = await NewsRepo.fetchAll()
        return Response(code=200, status="Ok", message="Success retrieve the data", result=newspaper).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__, result=[]).dict(exclude_none=True)
    

@router.get("/api/news/search/{details}")
async def fetch(details:str):
    try:
        # await newsContent()
        newspaper = await NewsRepo.search(details)
        return Response(code=200, status="Ok", message="Success retrieve the data", result=newspaper).dict(exclude_none=True)
    except UnknownDBError: 
        return Response(code=500, status="Internal Server Error", message=UnknownDBError.__str__).dict(exclude_none=True)
    
