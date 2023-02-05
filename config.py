
import motor.motor_asyncio
import os

NEWS_MONGO_URL = "mongodb://localhost:27017" #"mongodb+srv://datnews:datnews@datnews.t5jm7tr.mongodb.net/?retryWrites=true&w=majority" # os.getenv("NEWS_MONGO_URL")
AUTH_MONGO_URL = "mongodb://localhost:27017" # "" # os.getenv("AUTH_MONGO_URL")
database =  motor.motor_asyncio.AsyncIOMotorClient(NEWS_MONGO_URL)
authenticator = motor.motor_asyncio.AsyncIOMotorClient(AUTH_MONGO_URL)

# News
NEWS_DB_NAME = "datnews" # os.getenv("NEWS_DB_NAME", "")

NEWS_COL_NAME = "datnews" # os.getenv("NEWS_COL_NAME", "")
# Auth
AUTH_DB_NAME = "datnewsauth" # os.getenv("AUTH_DB_NAME", "")

AUTH_COL_NAME = "datnewsauth" # os.getenv("AUTH_COL_NAME", "")


RSSList = ["https://www.indiatoday.in/rss/home"]

MAIL = "heimanpicturesofficial@gmail.com" # os.getenv("MAIL")
PASS = "dtdnprcnhvitwlkh" # os.getenv("PASS")

MSG_EMAIL = """
<!DOCTYPE html>
<html>
<head>
  <title>Verify Your Email Address</title>
</head>
<body>
  <h1>Dear {name},</h1>
  <p>Thank you for signing up with DAT News. To complete the registration process, we need to verify your email address.</p>
  <p>Please enter the following OTP code within the next 10 minutes:</p>
  <h2>{otp}</h2>
  <p>If you did not request this code, please contact us immediately at heimanpicturesofficial@gmail.com.</p>
  <p>Thank you for choosing DAT News.</p>
  <p>Best regards,</p>
  <p>Thee Nighthawks<br>DAT News</p>
</body>
</html>
"""

MSG_NUMBER = """
{date}. The OTP is {otp}.
"""
