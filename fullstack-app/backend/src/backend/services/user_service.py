from fastapi import Depends, HTTPException
from datetime import datetime
from typing import Optional, List, Union
from sqlmodel import Session, select
from ..database.connection import get_session
from ..dto.user_dto import User, UserInput, UserUpdate
from ..repositories import user_repo as ur


def tambah_user(data_user: UserInput, session: Session):
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_user = User(
        first_name=data_user.first_name,
        last_name=data_user.last_name,
        whatsapp=data_user.whatsapp,
        created_at=waktu_sekarang,      
        updated_at=waktu_sekarang
    )
    
    return ur.create_user(db=session, data=new_user)

def tampilkan_user(id: Optional[int] = None, session: Session = Depends(get_session)):
    if id is None:
        return ur.get_users(db=session)
    user = ur.get_user_by_id(db=session,user_id=id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User dengan id {id} tidak ditemukan")
    return user


def edit_user(data_user: UserUpdate, session: Session = Depends(get_session)):
    return ur.update_user(db=session,user_data=data_user,time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
def hapus_user(id_input: int, session: Session = Depends(get_session)):
    return ur.delete_user(db=session,user_id=id_input)