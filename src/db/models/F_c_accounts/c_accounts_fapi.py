
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_c_accounts.c_accounts as a
from  db.models.F_c_accounts.c_accounts_pyd import c_accountsInfoBase, c_accountsInfoCreate, c_accountsInfoUpdate,c_accountsInfoInDBBase, c_accountsInfo
#import db.models.c_accounts_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/c_accounts/", response_model=c_accountsInfo)
def create_c_accounts(c_accounts: c_accountsInfoCreate, db: Session = Depends(get_db)):
    db_c_accounts = a.c_accounts(**c_accounts.dict())
    db.add(db_c_accounts)
    db.commit()
    db.refresh(db_c_accounts)
    return db_c_accounts

# Get all records
@app.get("/c_accounts/", response_model=List[c_accountsInfo])
def read__c_accounts_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.c_accounts).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/c_accounts/c_accounts_id", response_model=c_accountsInfo)
def read_c_accounts(c_accounts_id: int, db: Session = Depends(get_db)):
    db_c_accounts = db.query(db.models.c_accountsInfo).filter(db.models.c_accountsInfo.col_f1 == c_accounts_id).first()
    if db_c_accounts is None:
        raise HTTPException(status_code=404, detail="c_accounts info not found")
    return db_c_accounts

# Update a record
@app.put("/c_accounts/c_accounts_id", response_model=c_accountsInfo)
def update_c_accounts(c_accounts_id: int, c_accounts: c_accountsInfoUpdate, db: Session = Depends(get_db)):
    db_c_accounts = db.query(a.c_accountsInfo).filter(a.c_accountsInfo.col_f1 == c_accounts_id).first()
    if db_c_accounts is None:
        raise HTTPException(status_code=404, detail="c_accounts info not found")
    for key, value in c_accounts.dict().items():
        setattr(db_c_accounts, key, value)
    db.commit()
    db.refresh(db_c_accounts)
    return db_c_accounts

# Delete a record
@app.delete("/c_accounts/c_accounts_id", response_model=c_accountsInfo)
def delete_c_accounts(c_accounts_id: int, db: Session = Depends(get_db)):
    db_c_accounts = db.query(a.c_accountsInfo).filter(a.c_accountsInfo.col_f1 == c_accounts_id).first()
    if db_c_accounts is None:
        raise HTTPException(status_code=404, detail="c_accounts info not found")
    db.delete(db_c_accounts)
    db.commit()
    return db_c_accounts

