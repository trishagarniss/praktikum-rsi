from fastapi import Depends, HTTPException
from datetime import datetime
from typing import Optional, List, Union
from sqlmodel import Session, select
from database.connection import get_session
from dto.user_dto import User, UserInput, UserUpdate
from app import app

#@app.post("/tambah_user")
def tambah_user(data_user: UserInput, session: Session = Depends(get_session)):
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_user = User(
        first_name=data_user.first_name,
        last_name=data_user.last_name,
        whatsapp=data_user.whatsapp,
        created_at=waktu_sekarang,
        updated_at=waktu_sekarang
    )
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    return {
        "message": "Data berhasil ditambahkan",
        "data": new_user
    }

#@app.get("/tampilkan_user", response_model=Union[List[User], User])
def tampilkan_user(id: Optional[int] = None, session: Session = Depends(get_session)):
    if id is None:
        users = session.exec(select(User)).all()
        return users
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User dengan id {id} tidak ditemukan")
        
    return user

#@app.put("/edit_user")
def edit_user(data_user: UserUpdate, session: Session = Depends(get_session)):
    db_user = session.get(User, data_user.id)
    
    if db_user:
        data_lama = db_user.model_copy()
        db_user.first_name = data_user.first_name
        db_user.last_name = data_user.last_name
        db_user.whatsapp = data_user.whatsapp
        db_user.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        
        return {"message": "Data diubah!", "data lama": data_lama, "data baru": db_user}
    
    return {"message": "Tidak ada id tersebut di dalam Database User", "id": data_user.id}

#@app.delete("/hapus_user")
def hapus_user(id_input: int, session: Session = Depends(get_session)):
    db_user = session.get(User, id_input)
    
    if db_user:
        session.delete(db_user)
        session.commit()
        return {"message": "Data dihapus!", "data": db_user}
    
    return {"message": "Tidak ada id tersebut di dalam Database User", "id": id_input}