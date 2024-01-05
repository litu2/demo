from fastapi import FastAPI
from fastapi.routing import APIRoute
from app.api.api_v1.api import api_router


app=FastAPI()

app.include_router(api_router)

#if __name__ =="__main__":
 #   uvicorn.run("main:app",host="0.0.0.0",port=54321)
