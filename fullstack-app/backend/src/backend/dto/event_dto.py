from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 1. Skema Dasar (Atribut yang dikirim oleh klien/Swagger)
class EventBase(BaseModel):
    name: str
    description: str
    quota: int
    started_at: datetime
    ended_at: datetime

# 2. Skema untuk Request Create (POST)
class EventCreate(EventBase):
    pass

# 3. Skema untuk Request Update (PUT)
class EventUpdate(EventBase):
    pass # Ingat: ID tidak perlu dimasukkan di sini karena diambil dari URL Route

# 4. Skema untuk Response yang dikirim kembali ke Swagger
class EventResponse(EventBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    # MANTRA WAJIB biar nggak error 500 saat baca dari database
    class Config:
        from_attributes = True