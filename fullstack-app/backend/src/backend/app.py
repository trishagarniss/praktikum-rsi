from fastapi import FastAPI
from src.backend.routes import role_route

app = FastAPI(
    title="API Praktikum RSI Kelompok 2",
    description="Dokumentasi API untuk tugas CRUD"
)

@app.get("/")
def read_root():
    return {"message": "Server Backend Sedang Berjalan Cuyy!"}

app.include_router(role_route.router)