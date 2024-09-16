
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_c_client_info.c_client_info as a
from  db.models.F_c_client_info.c_client_info_pyd import c_client_infoInfoBase, c_client_infoInfoCreate, c_client_infoInfoUpdate,c_client_infoInfoInDBBase, c_client_infoInfo
#import db.models.c_client_info_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/c_client_info/", response_model=c_client_infoInfo)
def create_c_client_info(c_client_info: c_client_infoInfoCreate, db: Session = Depends(get_db)):
    db_c_client_info = a.c_client_info(**c_client_info.dict())
    db.add(db_c_client_info)
    db.commit()
    db.refresh(db_c_client_info)
    return db_c_client_info

# Get all records
@app.get("/c_client_info/", response_model=List[c_client_infoInfo])
def read__c_client_info_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.c_client_info).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/c_client_info/c_client_info_id", response_model=c_client_infoInfo)
def read_c_client_info(c_client_info_id: int, db: Session = Depends(get_db)):
    db_c_client_info = db.query(db.models.c_client_infoInfo).filter(db.models.c_client_infoInfo.col_f1 == c_client_info_id).first()
    if db_c_client_info is None:
        raise HTTPException(status_code=404, detail="c_client_info info not found")
    return db_c_client_info

# Update a record
@app.put("/c_client_info/c_client_info_id", response_model=c_client_infoInfo)
def update_c_client_info(c_client_info_id: int, c_client_info: c_client_infoInfoUpdate, db: Session = Depends(get_db)):
    db_c_client_info = db.query(a.c_client_infoInfo).filter(a.c_client_infoInfo.col_f1 == c_client_info_id).first()
    if db_c_client_info is None:
        raise HTTPException(status_code=404, detail="c_client_info info not found")
    for key, value in c_client_info.dict().items():
        setattr(db_c_client_info, key, value)
    db.commit()
    db.refresh(db_c_client_info)
    return db_c_client_info

# Delete a record
@app.delete("/c_client_info/c_client_info_id", response_model=c_client_infoInfo)
def delete_c_client_info(c_client_info_id: int, db: Session = Depends(get_db)):
    db_c_client_info = db.query(a.c_client_infoInfo).filter(a.c_client_infoInfo.col_f1 == c_client_info_id).first()
    if db_c_client_info is None:
        raise HTTPException(status_code=404, detail="c_client_info info not found")
    db.delete(db_c_client_info)
    db.commit()
    return db_c_client_info

