
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_c_user_communications.c_user_communications as a
from  db.models.F_c_user_communications.c_user_communications_pyd import c_user_communicationsInfoBase, c_user_communicationsInfoCreate, c_user_communicationsInfoUpdate,c_user_communicationsInfoInDBBase, c_user_communicationsInfo
#import db.models.c_user_communications_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/c_user_communications/", response_model=c_user_communicationsInfo)
def create_c_user_communications(c_user_communications: c_user_communicationsInfoCreate, db: Session = Depends(get_db)):
    db_c_user_communications = a.c_user_communications(**c_user_communications.dict())
    db.add(db_c_user_communications)
    db.commit()
    db.refresh(db_c_user_communications)
    return db_c_user_communications

# Get all records
@app.get("/c_user_communications/", response_model=List[c_user_communicationsInfo])
def read__c_user_communications_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.c_user_communications).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/c_user_communications/c_user_communications_id", response_model=c_user_communicationsInfo)
def read_c_user_communications(c_user_communications_id: int, db: Session = Depends(get_db)):
    db_c_user_communications = db.query(db.models.c_user_communicationsInfo).filter(db.models.c_user_communicationsInfo.col_f1 == c_user_communications_id).first()
    if db_c_user_communications is None:
        raise HTTPException(status_code=404, detail="c_user_communications info not found")
    return db_c_user_communications

# Update a record
@app.put("/c_user_communications/c_user_communications_id", response_model=c_user_communicationsInfo)
def update_c_user_communications(c_user_communications_id: int, c_user_communications: c_user_communicationsInfoUpdate, db: Session = Depends(get_db)):
    db_c_user_communications = db.query(a.c_user_communicationsInfo).filter(a.c_user_communicationsInfo.col_f1 == c_user_communications_id).first()
    if db_c_user_communications is None:
        raise HTTPException(status_code=404, detail="c_user_communications info not found")
    for key, value in c_user_communications.dict().items():
        setattr(db_c_user_communications, key, value)
    db.commit()
    db.refresh(db_c_user_communications)
    return db_c_user_communications

# Delete a record
@app.delete("/c_user_communications/c_user_communications_id", response_model=c_user_communicationsInfo)
def delete_c_user_communications(c_user_communications_id: int, db: Session = Depends(get_db)):
    db_c_user_communications = db.query(a.c_user_communicationsInfo).filter(a.c_user_communicationsInfo.col_f1 == c_user_communications_id).first()
    if db_c_user_communications is None:
        raise HTTPException(status_code=404, detail="c_user_communications info not found")
    db.delete(db_c_user_communications)
    db.commit()
    return db_c_user_communications

