
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_c_user_info.c_user_info as a
from  db.models.F_c_user_info.c_user_info_pyd import c_user_infoInfoBase, c_user_infoInfoCreate, c_user_infoInfoUpdate,c_user_infoInfoInDBBase, c_user_infoInfo
#import db.models.c_user_info_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/c_user_info/", response_model=c_user_infoInfo)
def create_c_user_info(c_user_info: c_user_infoInfoCreate, db: Session = Depends(get_db)):
    db_c_user_info = a.c_user_info(**c_user_info.dict())
    db.add(db_c_user_info)
    db.commit()
    db.refresh(db_c_user_info)
    return db_c_user_info

# Get all records
@app.get("/c_user_info/", response_model=List[c_user_infoInfo])
def read__c_user_info_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.c_user_info).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/c_user_info/c_user_info_id", response_model=c_user_infoInfo)
def read_c_user_info(c_user_info_id: int, db: Session = Depends(get_db)):
    db_c_user_info = db.query(db.models.c_user_infoInfo).filter(db.models.c_user_infoInfo.col_f1 == c_user_info_id).first()
    if db_c_user_info is None:
        raise HTTPException(status_code=404, detail="c_user_info info not found")
    return db_c_user_info

# Update a record
@app.put("/c_user_info/c_user_info_id", response_model=c_user_infoInfo)
def update_c_user_info(c_user_info_id: int, c_user_info: c_user_infoInfoUpdate, db: Session = Depends(get_db)):
    db_c_user_info = db.query(a.c_user_infoInfo).filter(a.c_user_infoInfo.col_f1 == c_user_info_id).first()
    if db_c_user_info is None:
        raise HTTPException(status_code=404, detail="c_user_info info not found")
    for key, value in c_user_info.dict().items():
        setattr(db_c_user_info, key, value)
    db.commit()
    db.refresh(db_c_user_info)
    return db_c_user_info

# Delete a record
@app.delete("/c_user_info/c_user_info_id", response_model=c_user_infoInfo)
def delete_c_user_info(c_user_info_id: int, db: Session = Depends(get_db)):
    db_c_user_info = db.query(a.c_user_infoInfo).filter(a.c_user_infoInfo.col_f1 == c_user_info_id).first()
    if db_c_user_info is None:
        raise HTTPException(status_code=404, detail="c_user_info info not found")
    db.delete(db_c_user_info)
    db.commit()
    return db_c_user_info

