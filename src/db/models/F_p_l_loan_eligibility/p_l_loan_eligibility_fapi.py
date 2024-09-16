
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_p_l_loan_eligibility.p_l_loan_eligibility as a
from  db.models.F_p_l_loan_eligibility.p_l_loan_eligibility_pyd import p_l_loan_eligibilityInfoBase, p_l_loan_eligibilityInfoCreate, p_l_loan_eligibilityInfoUpdate,p_l_loan_eligibilityInfoInDBBase, p_l_loan_eligibilityInfo
#import db.models.p_l_loan_eligibility_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/p_l_loan_eligibility/", response_model=p_l_loan_eligibilityInfo)
def create_p_l_loan_eligibility(p_l_loan_eligibility: p_l_loan_eligibilityInfoCreate, db: Session = Depends(get_db)):
    db_p_l_loan_eligibility = a.p_l_loan_eligibility(**p_l_loan_eligibility.dict())
    db.add(db_p_l_loan_eligibility)
    db.commit()
    db.refresh(db_p_l_loan_eligibility)
    return db_p_l_loan_eligibility

# Get all records
@app.get("/p_l_loan_eligibility/", response_model=List[p_l_loan_eligibilityInfo])
def read__p_l_loan_eligibility_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.p_l_loan_eligibility).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/p_l_loan_eligibility/p_l_loan_eligibility_id", response_model=p_l_loan_eligibilityInfo)
def read_p_l_loan_eligibility(p_l_loan_eligibility_id: int, db: Session = Depends(get_db)):
    db_p_l_loan_eligibility = db.query(db.models.p_l_loan_eligibilityInfo).filter(db.models.p_l_loan_eligibilityInfo.col_f1 == p_l_loan_eligibility_id).first()
    if db_p_l_loan_eligibility is None:
        raise HTTPException(status_code=404, detail="p_l_loan_eligibility info not found")
    return db_p_l_loan_eligibility

# Update a record
@app.put("/p_l_loan_eligibility/p_l_loan_eligibility_id", response_model=p_l_loan_eligibilityInfo)
def update_p_l_loan_eligibility(p_l_loan_eligibility_id: int, p_l_loan_eligibility: p_l_loan_eligibilityInfoUpdate, db: Session = Depends(get_db)):
    db_p_l_loan_eligibility = db.query(a.p_l_loan_eligibilityInfo).filter(a.p_l_loan_eligibilityInfo.col_f1 == p_l_loan_eligibility_id).first()
    if db_p_l_loan_eligibility is None:
        raise HTTPException(status_code=404, detail="p_l_loan_eligibility info not found")
    for key, value in p_l_loan_eligibility.dict().items():
        setattr(db_p_l_loan_eligibility, key, value)
    db.commit()
    db.refresh(db_p_l_loan_eligibility)
    return db_p_l_loan_eligibility

# Delete a record
@app.delete("/p_l_loan_eligibility/p_l_loan_eligibility_id", response_model=p_l_loan_eligibilityInfo)
def delete_p_l_loan_eligibility(p_l_loan_eligibility_id: int, db: Session = Depends(get_db)):
    db_p_l_loan_eligibility = db.query(a.p_l_loan_eligibilityInfo).filter(a.p_l_loan_eligibilityInfo.col_f1 == p_l_loan_eligibility_id).first()
    if db_p_l_loan_eligibility is None:
        raise HTTPException(status_code=404, detail="p_l_loan_eligibility info not found")
    db.delete(db_p_l_loan_eligibility)
    db.commit()
    return db_p_l_loan_eligibility

