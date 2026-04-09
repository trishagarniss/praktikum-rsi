from fastapi import Depends, HTTPException
from datetime import datetime
from typing import Optional, List, Union
from sqlmodel import Session, select,Field
from ..database.connection import get_session
from ..dto.user_dto import UserInput, UserUpdate
from ..repositories import user_repo as ur
from ..database.schema.models import User


def tambah_user(data_user: UserInput, db: Session= Depends(get_session)):
    
    new_user = User(
        first_name=data_user.first_name,
        last_name=data_user.last_name,
        whatsapp=data_user.whatsapp
    )
    
    return ur.create_user(db=db, data=new_user)

def tampilkan_user(id: Optional[int] = None, db:Session= Depends(get_session)):
    if id is None:
        return ur.get_users(db=db)
    user = ur.get_user_by_id(db=db,user_id=id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User dengan id {id} tidak ditemukan")
    return user


def edit_user(data_user: UserUpdate, db: Session= Depends(get_session)):
    user = ur.update_user(db=db,user_data=data_user,time=datetime.now())
    if not user:
        raise HTTPException(status_code=404, detail=f"User dengan id {data_user.id} tidak ditemukan")
    return user
    
def hapus_user(id_input: int, db: Session= Depends(get_session)):
    user = ur.delete_user(db=db,user_id=id_input)
    if not user:
        raise HTTPException(status_code=404, detail=f"User dengan id {id} tidak ditemukan")
    return user