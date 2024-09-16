
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_l_student_loans.l_student_loans as a
from  db.models.F_l_student_loans.l_student_loans_pyd import l_student_loansInfoBase, l_student_loansInfoCreate, l_student_loansInfoUpdate,l_student_loansInfoInDBBase, l_student_loansInfo
#import db.models.l_student_loans_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/l_student_loans/", response_model=l_student_loansInfo)
def create_l_student_loans(l_student_loans: l_student_loansInfoCreate, db: Session = Depends(get_db)):
    db_l_student_loans = a.l_student_loans(**l_student_loans.dict())
    db.add(db_l_student_loans)
    db.commit()
    db.refresh(db_l_student_loans)
    return db_l_student_loans

# Get all records
@app.get("/l_student_loans/", response_model=List[l_student_loansInfo])
def read__l_student_loans_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.l_student_loans).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/l_student_loans/l_student_loans_id", response_model=l_student_loansInfo)
def read_l_student_loans(l_student_loans_id: int, db: Session = Depends(get_db)):
    db_l_student_loans = db.query(db.models.l_student_loansInfo).filter(db.models.l_student_loansInfo.col_f1 == l_student_loans_id).first()
    if db_l_student_loans is None:
        raise HTTPException(status_code=404, detail="l_student_loans info not found")
    return db_l_student_loans

# Update a record
@app.put("/l_student_loans/l_student_loans_id", response_model=l_student_loansInfo)
def update_l_student_loans(l_student_loans_id: int, l_student_loans: l_student_loansInfoUpdate, db: Session = Depends(get_db)):
    db_l_student_loans = db.query(a.l_student_loansInfo).filter(a.l_student_loansInfo.col_f1 == l_student_loans_id).first()
    if db_l_student_loans is None:
        raise HTTPException(status_code=404, detail="l_student_loans info not found")
    for key, value in l_student_loans.dict().items():
        setattr(db_l_student_loans, key, value)
    db.commit()
    db.refresh(db_l_student_loans)
    return db_l_student_loans

# Delete a record
@app.delete("/l_student_loans/l_student_loans_id", response_model=l_student_loansInfo)
def delete_l_student_loans(l_student_loans_id: int, db: Session = Depends(get_db)):
    db_l_student_loans = db.query(a.l_student_loansInfo).filter(a.l_student_loansInfo.col_f1 == l_student_loans_id).first()
    if db_l_student_loans is None:
        raise HTTPException(status_code=404, detail="l_student_loans info not found")
    db.delete(db_l_student_loans)
    db.commit()
    return db_l_student_loans

