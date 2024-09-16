
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_f_fi_interest.f_fi_interest as a
from  db.models.F_f_fi_interest.f_fi_interest_pyd import f_fi_interestInfoBase, f_fi_interestInfoCreate, f_fi_interestInfoUpdate,f_fi_interestInfoInDBBase, f_fi_interestInfo
#import db.models.f_fi_interest_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/f_fi_interest/", response_model=f_fi_interestInfo)
def create_f_fi_interest(f_fi_interest: f_fi_interestInfoCreate, db: Session = Depends(get_db)):
    db_f_fi_interest = a.f_fi_interest(**f_fi_interest.dict())
    db.add(db_f_fi_interest)
    db.commit()
    db.refresh(db_f_fi_interest)
    return db_f_fi_interest

# Get all records
@app.get("/f_fi_interest/", response_model=List[f_fi_interestInfo])
def read__f_fi_interest_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.f_fi_interest).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/f_fi_interest/f_fi_interest_id", response_model=f_fi_interestInfo)
def read_f_fi_interest(f_fi_interest_id: int, db: Session = Depends(get_db)):
    db_f_fi_interest = db.query(db.models.f_fi_interestInfo).filter(db.models.f_fi_interestInfo.col_f1 == f_fi_interest_id).first()
    if db_f_fi_interest is None:
        raise HTTPException(status_code=404, detail="f_fi_interest info not found")
    return db_f_fi_interest

# Update a record
@app.put("/f_fi_interest/f_fi_interest_id", response_model=f_fi_interestInfo)
def update_f_fi_interest(f_fi_interest_id: int, f_fi_interest: f_fi_interestInfoUpdate, db: Session = Depends(get_db)):
    db_f_fi_interest = db.query(a.f_fi_interestInfo).filter(a.f_fi_interestInfo.col_f1 == f_fi_interest_id).first()
    if db_f_fi_interest is None:
        raise HTTPException(status_code=404, detail="f_fi_interest info not found")
    for key, value in f_fi_interest.dict().items():
        setattr(db_f_fi_interest, key, value)
    db.commit()
    db.refresh(db_f_fi_interest)
    return db_f_fi_interest

# Delete a record
@app.delete("/f_fi_interest/f_fi_interest_id", response_model=f_fi_interestInfo)
def delete_f_fi_interest(f_fi_interest_id: int, db: Session = Depends(get_db)):
    db_f_fi_interest = db.query(a.f_fi_interestInfo).filter(a.f_fi_interestInfo.col_f1 == f_fi_interest_id).first()
    if db_f_fi_interest is None:
        raise HTTPException(status_code=404, detail="f_fi_interest info not found")
    db.delete(db_f_fi_interest)
    db.commit()
    return db_f_fi_interest

