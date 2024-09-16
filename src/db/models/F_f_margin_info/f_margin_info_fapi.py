
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_f_margin_info.f_margin_info as a
from  db.models.F_f_margin_info.f_margin_info_pyd import f_margin_infoInfoBase, f_margin_infoInfoCreate, f_margin_infoInfoUpdate,f_margin_infoInfoInDBBase, f_margin_infoInfo
#import db.models.f_margin_info_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/f_margin_info/", response_model=f_margin_infoInfo)
def create_f_margin_info(f_margin_info: f_margin_infoInfoCreate, db: Session = Depends(get_db)):
    db_f_margin_info = a.f_margin_info(**f_margin_info.dict())
    db.add(db_f_margin_info)
    db.commit()
    db.refresh(db_f_margin_info)
    return db_f_margin_info

# Get all records
@app.get("/f_margin_info/", response_model=List[f_margin_infoInfo])
def read__f_margin_info_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.f_margin_info).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/f_margin_info/f_margin_info_id", response_model=f_margin_infoInfo)
def read_f_margin_info(f_margin_info_id: int, db: Session = Depends(get_db)):
    db_f_margin_info = db.query(db.models.f_margin_infoInfo).filter(db.models.f_margin_infoInfo.col_f1 == f_margin_info_id).first()
    if db_f_margin_info is None:
        raise HTTPException(status_code=404, detail="f_margin_info info not found")
    return db_f_margin_info

# Update a record
@app.put("/f_margin_info/f_margin_info_id", response_model=f_margin_infoInfo)
def update_f_margin_info(f_margin_info_id: int, f_margin_info: f_margin_infoInfoUpdate, db: Session = Depends(get_db)):
    db_f_margin_info = db.query(a.f_margin_infoInfo).filter(a.f_margin_infoInfo.col_f1 == f_margin_info_id).first()
    if db_f_margin_info is None:
        raise HTTPException(status_code=404, detail="f_margin_info info not found")
    for key, value in f_margin_info.dict().items():
        setattr(db_f_margin_info, key, value)
    db.commit()
    db.refresh(db_f_margin_info)
    return db_f_margin_info

# Delete a record
@app.delete("/f_margin_info/f_margin_info_id", response_model=f_margin_infoInfo)
def delete_f_margin_info(f_margin_info_id: int, db: Session = Depends(get_db)):
    db_f_margin_info = db.query(a.f_margin_infoInfo).filter(a.f_margin_infoInfo.col_f1 == f_margin_info_id).first()
    if db_f_margin_info is None:
        raise HTTPException(status_code=404, detail="f_margin_info info not found")
    db.delete(db_f_margin_info)
    db.commit()
    return db_f_margin_info

