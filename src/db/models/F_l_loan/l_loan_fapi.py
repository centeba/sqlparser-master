
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_l_loan.l_loan as a
from  db.models.F_l_loan.l_loan_pyd import l_loanInfoBase, l_loanInfoCreate, l_loanInfoUpdate,l_loanInfoInDBBase, l_loanInfo
#import db.models.l_loan_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/l_loan/", response_model=l_loanInfo)
def create_l_loan(l_loan: l_loanInfoCreate, db: Session = Depends(get_db)):
    db_l_loan = a.l_loan(**l_loan.dict())
    db.add(db_l_loan)
    db.commit()
    db.refresh(db_l_loan)
    return db_l_loan

# Get all records
@app.get("/l_loan/", response_model=List[l_loanInfo])
def read__l_loan_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.l_loan).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/l_loan/l_loan_id", response_model=l_loanInfo)
def read_l_loan(l_loan_id: int, db: Session = Depends(get_db)):
    db_l_loan = db.query(db.models.l_loanInfo).filter(db.models.l_loanInfo.col_f1 == l_loan_id).first()
    if db_l_loan is None:
        raise HTTPException(status_code=404, detail="l_loan info not found")
    return db_l_loan

# Update a record
@app.put("/l_loan/l_loan_id", response_model=l_loanInfo)
def update_l_loan(l_loan_id: int, l_loan: l_loanInfoUpdate, db: Session = Depends(get_db)):
    db_l_loan = db.query(a.l_loanInfo).filter(a.l_loanInfo.col_f1 == l_loan_id).first()
    if db_l_loan is None:
        raise HTTPException(status_code=404, detail="l_loan info not found")
    for key, value in l_loan.dict().items():
        setattr(db_l_loan, key, value)
    db.commit()
    db.refresh(db_l_loan)
    return db_l_loan

# Delete a record
@app.delete("/l_loan/l_loan_id", response_model=l_loanInfo)
def delete_l_loan(l_loan_id: int, db: Session = Depends(get_db)):
    db_l_loan = db.query(a.l_loanInfo).filter(a.l_loanInfo.col_f1 == l_loan_id).first()
    if db_l_loan is None:
        raise HTTPException(status_code=404, detail="l_loan info not found")
    db.delete(db_l_loan)
    db.commit()
    return db_l_loan

