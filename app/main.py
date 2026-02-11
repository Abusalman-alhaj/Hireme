from fastapi import FastAPI
from .database import engine, Base
from . import models
from sqlalchemy import text
from .routers import users , jobs,applications
 

 


app = FastAPI()
app.include_router(users.router)
app.include_router(applications.router)
app.include_router(jobs.router)

@app.on_event("startup")
def startup():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("✅ Database connected")
    except Exception as e:
        print("❌ DB error:", e)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "HireMe API running 🚀"}

