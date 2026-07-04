from fastapi import FastAPI

from app.database import Base
from app.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Firm 1 Asset Manager"
)


@app.get("/")
def home():

    return {
        "company": "Firm 1",
        "status": "Running",
        "message": "Asset Manager API"
    }