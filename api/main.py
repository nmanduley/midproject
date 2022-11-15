from fastapi import FastAPI
from api.Routers import endpoints

app = FastAPI()

app.include_router(endpoints.router)

@app.get("/")
def test():
    return {"Test": "OK"}

# sys.path.append(os.path.abspath(..)) # Donde va? 