
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_f_transaction_info.f_transaction_info as a
from  db.models.F_f_transaction_info.f_transaction_info_pyd import f_transaction_infoInfoBase, f_transaction_infoInfoCreate, f_transaction_infoInfoUpdate,f_transaction_infoInfoInDBBase, f_transaction_infoInfo
#import db.models.f_transaction_info_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/f_transaction_info/", response_model=f_transaction_infoInfo)
def create_f_transaction_info(f_transaction_info: f_transaction_infoInfoCreate, db: Session = Depends(get_db)):
    db_f_transaction_info = a.f_transaction_info(**f_transaction_info.dict())
    db.add(db_f_transaction_info)
    db.commit()
    db.refresh(db_f_transaction_info)
    return db_f_transaction_info

# Get all records
@app.get("/f_transaction_info/", response_model=List[f_transaction_infoInfo])
def read__f_transaction_info_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.f_transaction_info).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/f_transaction_info/f_transaction_info_id", response_model=f_transaction_infoInfo)
def read_f_transaction_info(f_transaction_info_id: int, db: Session = Depends(get_db)):
    db_f_transaction_info = db.query(db.models.f_transaction_infoInfo).filter(db.models.f_transaction_infoInfo.col_f1 == f_transaction_info_id).first()
    if db_f_transaction_info is None:
        raise HTTPException(status_code=404, detail="f_transaction_info info not found")
    return db_f_transaction_info

# Update a record
@app.put("/f_transaction_info/f_transaction_info_id", response_model=f_transaction_infoInfo)
def update_f_transaction_info(f_transaction_info_id: int, f_transaction_info: f_transaction_infoInfoUpdate, db: Session = Depends(get_db)):
    db_f_transaction_info = db.query(a.f_transaction_infoInfo).filter(a.f_transaction_infoInfo.col_f1 == f_transaction_info_id).first()
    if db_f_transaction_info is None:
        raise HTTPException(status_code=404, detail="f_transaction_info info not found")
    for key, value in f_transaction_info.dict().items():
        setattr(db_f_transaction_info, key, value)
    db.commit()
    db.refresh(db_f_transaction_info)
    return db_f_transaction_info

# Delete a record
@app.delete("/f_transaction_info/f_transaction_info_id", response_model=f_transaction_infoInfo)
def delete_f_transaction_info(f_transaction_info_id: int, db: Session = Depends(get_db)):
    db_f_transaction_info = db.query(a.f_transaction_infoInfo).filter(a.f_transaction_infoInfo.col_f1 == f_transaction_info_id).first()
    if db_f_transaction_info is None:
        raise HTTPException(status_code=404, detail="f_transaction_info info not found")
    db.delete(db_f_transaction_info)
    db.commit()
    return db_f_transaction_info

