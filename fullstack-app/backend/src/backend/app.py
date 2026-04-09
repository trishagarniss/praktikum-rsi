from fastapi import FastAPI
from src.backend.routes import role_route
from src.backend.routes import event_route

app = FastAPI(
    title="API Praktikum RSI Kelompok 2",
    description="Dokumentasi API untuk tugas CRUD"
)

@app.get("/")
def read_root():
    return {"message": "Server Backend Sedang Berjalan Cuyy!"}

app.include_router(role_route.router)
app.include_router(event_route.router)

if __name__ == "__main__":
    import uvicorn
    # Pakai "app:app" karena nama file app.py
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
