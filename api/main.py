from fastapi import FastAPI
from Routers import endpoints

app = FastAPI()

app.include_router(endpoints.router)

@app.get("/")
def test():
    return {"Test": "OK"}