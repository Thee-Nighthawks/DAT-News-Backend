import nltk
# import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app_router import router
# # News
# import schedule
# import time
from utils.article import newsContent

# if __name__ == "__main__":
#     asyncio.run(newsContent())

app = FastAPI()

nltk.download('punkt')

# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:80",
#     "http://localhost:4200"
# ]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return { "alive": True}

app.include_router(router)

# schedule.every().hour.do(newsContent)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


# if __name__ == "__main__":
#     asyncio.create_task(newsContent())
    # uvicorn.run(app, host="0.0.0.0", port=8000)