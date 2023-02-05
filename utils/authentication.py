
# import asyncio
from email.mime.multipart import MIMEMultipart
import random
import smtplib
from email.mime.text import MIMEText
from config import *

# MAIL = "heimanpicturesofficial@gmail.com"
# PASS = "dtdnprcnhvitwlkh"


# MSG_EMAIL = """
# <!DOCTYPE html>
# <html>
# <head>
#   <title>Verify Your Email Address</title>
# </head>
# <body>
#   <h1>Dear {name},</h1>
#   <p>Thank you for signing up with DAT News. To complete the registration process, we need to verify your email address.</p>
#   <p>Please enter the following OTP code within the next 10 minutes:</p>
#   <h2>{otp}</h2>
#   <p>If you did not request this code, please contact us immediately at heimanpicturesofficial@gmail.com.</p>
#   <p>Thank you for choosing DAT News.</p>
#   <p>Best regards,</p>
#   <p>Thee Nighthawks<br>DAT News</p>
# </body>
# </html>
# """

# MSG_NUMBER = """
# {date}. The OTP is {otp}.
# """


async def email(name:str, mail:str):
    try:
        otp = ''.join([str(random.randint(0,9)) for i in range(6)])
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(MAIL, PASS)
        message = MIMEMultipart("alternative")
        message["Subject"] = "OTP verification for DAT News"
        message["From"] = MAIL
        message["To"] = mail
        msg = MIMEText(MSG_EMAIL.format(name=name, otp=otp), "html")
        message.attach(msg)
        server.sendmail(MAIL, mail, message.as_string())
        server.quit()
        return otp
    except Exception as e:
        print("Auth: "+e)

async def mobile(name: str, number: int):
    otp = ''.join([str(random.randint(0,9)) for i in range(6)])
    
    return otp

# if __name__ == "__main__":
#     asyncio.run(email("Akkil", "akkilcharanmg@gmail.com"))