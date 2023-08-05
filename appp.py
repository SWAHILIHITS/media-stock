import os,uvicorn
from bot import Bot
HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", 8080)   
uvicorn.run(Bot(), host=HOST, port=PORT)


