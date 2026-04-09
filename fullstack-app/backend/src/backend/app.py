from fastapi import FastAPI
from src.backend.routes import account_route

app = FastAPI(
    title="API Praktikum RSI Kelompok 2",
    description="Dokumentasi API untuk tugas CRUD"
)

@app.get("/")
def read_root():
    return {"message": "Server Backend Sedang Berjalan Cuyy!"}


app.include_router(account_route.router)

if __name__ == "__main__":
    import uvicorn
    # Pakai "app:app" karena nama file app.py
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
