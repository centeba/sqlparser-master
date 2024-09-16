
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_f_security_master.f_security_master as a
from  db.models.F_f_security_master.f_security_master_pyd import f_security_masterInfoBase, f_security_masterInfoCreate, f_security_masterInfoUpdate,f_security_masterInfoInDBBase, f_security_masterInfo
#import db.models.f_security_master_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/f_security_master/", response_model=f_security_masterInfo)
def create_f_security_master(f_security_master: f_security_masterInfoCreate, db: Session = Depends(get_db)):
    db_f_security_master = a.f_security_master(**f_security_master.dict())
    db.add(db_f_security_master)
    db.commit()
    db.refresh(db_f_security_master)
    return db_f_security_master

# Get all records
@app.get("/f_security_master/", response_model=List[f_security_masterInfo])
def read__f_security_master_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.f_security_master).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/f_security_master/f_security_master_id", response_model=f_security_masterInfo)
def read_f_security_master(f_security_master_id: int, db: Session = Depends(get_db)):
    db_f_security_master = db.query(db.models.f_security_masterInfo).filter(db.models.f_security_masterInfo.col_f1 == f_security_master_id).first()
    if db_f_security_master is None:
        raise HTTPException(status_code=404, detail="f_security_master info not found")
    return db_f_security_master

# Update a record
@app.put("/f_security_master/f_security_master_id", response_model=f_security_masterInfo)
def update_f_security_master(f_security_master_id: int, f_security_master: f_security_masterInfoUpdate, db: Session = Depends(get_db)):
    db_f_security_master = db.query(a.f_security_masterInfo).filter(a.f_security_masterInfo.col_f1 == f_security_master_id).first()
    if db_f_security_master is None:
        raise HTTPException(status_code=404, detail="f_security_master info not found")
    for key, value in f_security_master.dict().items():
        setattr(db_f_security_master, key, value)
    db.commit()
    db.refresh(db_f_security_master)
    return db_f_security_master

# Delete a record
@app.delete("/f_security_master/f_security_master_id", response_model=f_security_masterInfo)
def delete_f_security_master(f_security_master_id: int, db: Session = Depends(get_db)):
    db_f_security_master = db.query(a.f_security_masterInfo).filter(a.f_security_masterInfo.col_f1 == f_security_master_id).first()
    if db_f_security_master is None:
        raise HTTPException(status_code=404, detail="f_security_master info not found")
    db.delete(db_f_security_master)
    db.commit()
    return db_f_security_master

