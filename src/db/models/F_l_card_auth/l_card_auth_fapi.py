
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_l_card_auth.l_card_auth as a
from  db.models.F_l_card_auth.l_card_auth_pyd import l_card_authInfoBase, l_card_authInfoCreate, l_card_authInfoUpdate,l_card_authInfoInDBBase, l_card_authInfo
#import db.models.l_card_auth_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/l_card_auth/", response_model=l_card_authInfo)
def create_l_card_auth(l_card_auth: l_card_authInfoCreate, db: Session = Depends(get_db)):
    db_l_card_auth = a.l_card_auth(**l_card_auth.dict())
    db.add(db_l_card_auth)
    db.commit()
    db.refresh(db_l_card_auth)
    return db_l_card_auth

# Get all records
@app.get("/l_card_auth/", response_model=List[l_card_authInfo])
def read__l_card_auth_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.l_card_auth).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/l_card_auth/l_card_auth_id", response_model=l_card_authInfo)
def read_l_card_auth(l_card_auth_id: int, db: Session = Depends(get_db)):
    db_l_card_auth = db.query(db.models.l_card_authInfo).filter(db.models.l_card_authInfo.col_f1 == l_card_auth_id).first()
    if db_l_card_auth is None:
        raise HTTPException(status_code=404, detail="l_card_auth info not found")
    return db_l_card_auth

# Update a record
@app.put("/l_card_auth/l_card_auth_id", response_model=l_card_authInfo)
def update_l_card_auth(l_card_auth_id: int, l_card_auth: l_card_authInfoUpdate, db: Session = Depends(get_db)):
    db_l_card_auth = db.query(a.l_card_authInfo).filter(a.l_card_authInfo.col_f1 == l_card_auth_id).first()
    if db_l_card_auth is None:
        raise HTTPException(status_code=404, detail="l_card_auth info not found")
    for key, value in l_card_auth.dict().items():
        setattr(db_l_card_auth, key, value)
    db.commit()
    db.refresh(db_l_card_auth)
    return db_l_card_auth

# Delete a record
@app.delete("/l_card_auth/l_card_auth_id", response_model=l_card_authInfo)
def delete_l_card_auth(l_card_auth_id: int, db: Session = Depends(get_db)):
    db_l_card_auth = db.query(a.l_card_authInfo).filter(a.l_card_authInfo.col_f1 == l_card_auth_id).first()
    if db_l_card_auth is None:
        raise HTTPException(status_code=404, detail="l_card_auth info not found")
    db.delete(db_l_card_auth)
    db.commit()
    return db_l_card_auth

