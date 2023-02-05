

# import asyncio
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from config import *

async def mailContent(mail:str, subject: str, content: str):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MAIL, PASS)
    message = MIMEMultipart("alternative")
    message["Subject"] = f"{subject}"
    message["From"] = MAIL
    message["To"] = mail
    msg = MIMEText(content, "html")
    message.attach(msg)
    server.sendmail(MAIL, mail, message.as_string())
    server.quit()


# if __name__ == "__main__":
#     asyncio.run(mailContent("akkilcharanmg@gmail.com", "Test for mail contents", "This will have body of the content."))