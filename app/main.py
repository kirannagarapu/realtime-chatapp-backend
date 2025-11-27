from fastapi import FastAPI
from app.routers import auth, users

app = FastAPI(title="Realtime Chat Backend (dev)")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Chat API is running!"}
