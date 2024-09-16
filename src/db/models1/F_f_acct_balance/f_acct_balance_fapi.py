
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_f_acct_balance.f_acct_balance as a
from  db.models.F_f_acct_balance.f_acct_balance_pyd import f_acct_balanceInfoBase, f_acct_balanceInfoCreate, f_acct_balanceInfoUpdate,f_acct_balanceInfoInDBBase, f_acct_balanceInfo
#import db.models.f_acct_balance_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/f_acct_balance/", response_model=f_acct_balanceInfo)
def create_f_acct_balance(f_acct_balance: f_acct_balanceInfoCreate, db: Session = Depends(get_db)):
    db_f_acct_balance = a.f_acct_balance(**f_acct_balance.dict())
    db.add(db_f_acct_balance)
    db.commit()
    db.refresh(db_f_acct_balance)
    return db_f_acct_balance

# Get all records
@app.get("/f_acct_balance/", response_model=List[f_acct_balanceInfo])
def read__f_acct_balance_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.f_acct_balance).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/f_acct_balance/f_acct_balance_id", response_model=f_acct_balanceInfo)
def read_f_acct_balance(f_acct_balance_id: int, db: Session = Depends(get_db)):
    db_f_acct_balance = db.query(db.models.f_acct_balanceInfo).filter(db.models.f_acct_balanceInfo.col_f1 == f_acct_balance_id).first()
    if db_f_acct_balance is None:
        raise HTTPException(status_code=404, detail="f_acct_balance info not found")
    return db_f_acct_balance

# Update a record
@app.put("/f_acct_balance/f_acct_balance_id", response_model=f_acct_balanceInfo)
def update_f_acct_balance(f_acct_balance_id: int, f_acct_balance: f_acct_balanceInfoUpdate, db: Session = Depends(get_db)):
    db_f_acct_balance = db.query(a.f_acct_balanceInfo).filter(a.f_acct_balanceInfo.col_f1 == f_acct_balance_id).first()
    if db_f_acct_balance is None:
        raise HTTPException(status_code=404, detail="f_acct_balance info not found")
    for key, value in f_acct_balance.dict().items():
        setattr(db_f_acct_balance, key, value)
    db.commit()
    db.refresh(db_f_acct_balance)
    return db_f_acct_balance

# Delete a record
@app.delete("/f_acct_balance/f_acct_balance_id", response_model=f_acct_balanceInfo)
def delete_f_acct_balance(f_acct_balance_id: int, db: Session = Depends(get_db)):
    db_f_acct_balance = db.query(a.f_acct_balanceInfo).filter(a.f_acct_balanceInfo.col_f1 == f_acct_balance_id).first()
    if db_f_acct_balance is None:
        raise HTTPException(status_code=404, detail="f_acct_balance info not found")
    db.delete(db_f_acct_balance)
    db.commit()
    return db_f_acct_balance

