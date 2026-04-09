from typing import Optional
from pydantic import BaseModel

# Skema dasar untuk Role
class RoleBase(BaseModel):
    name: str

# Digunakan saat client mengirim data untuk membuat Role baru
class RoleCreate(RoleBase):
    pass

# Digunakan saat client mengirim data untuk update Role
class RoleUpdate(RoleBase):
    pass

# Format data yang dikirim balik ke client (Response)
class RoleResponse(RoleBase):
    id: int

    class Config:
        from_attributes = True