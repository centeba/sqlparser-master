
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_custodian_wf_accounts_ext.custodian_wf_accounts_ext as a
from  db.models.F_custodian_wf_accounts_ext.custodian_wf_accounts_ext_pyd import custodian_wf_accounts_extInfoBase, custodian_wf_accounts_extInfoCreate, custodian_wf_accounts_extInfoUpdate,custodian_wf_accounts_extInfoInDBBase, custodian_wf_accounts_extInfo
#import db.models.custodian_wf_accounts_ext_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/custodian_wf_accounts_ext/", response_model=custodian_wf_accounts_extInfo)
def create_custodian_wf_accounts_ext(custodian_wf_accounts_ext: custodian_wf_accounts_extInfoCreate, db: Session = Depends(get_db)):
    db_custodian_wf_accounts_ext = a.custodian_wf_accounts_ext(**custodian_wf_accounts_ext.dict())
    db.add(db_custodian_wf_accounts_ext)
    db.commit()
    db.refresh(db_custodian_wf_accounts_ext)
    return db_custodian_wf_accounts_ext

# Get all records
@app.get("/custodian_wf_accounts_ext/", response_model=List[custodian_wf_accounts_extInfo])
def read__custodian_wf_accounts_ext_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.custodian_wf_accounts_ext).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/custodian_wf_accounts_ext/custodian_wf_accounts_ext_id", response_model=custodian_wf_accounts_extInfo)
def read_custodian_wf_accounts_ext(custodian_wf_accounts_ext_id: int, db: Session = Depends(get_db)):
    db_custodian_wf_accounts_ext = db.query(db.models.custodian_wf_accounts_extInfo).filter(db.models.custodian_wf_accounts_extInfo.col_f1 == custodian_wf_accounts_ext_id).first()
    if db_custodian_wf_accounts_ext is None:
        raise HTTPException(status_code=404, detail="custodian_wf_accounts_ext info not found")
    return db_custodian_wf_accounts_ext

# Update a record
@app.put("/custodian_wf_accounts_ext/custodian_wf_accounts_ext_id", response_model=custodian_wf_accounts_extInfo)
def update_custodian_wf_accounts_ext(custodian_wf_accounts_ext_id: int, custodian_wf_accounts_ext: custodian_wf_accounts_extInfoUpdate, db: Session = Depends(get_db)):
    db_custodian_wf_accounts_ext = db.query(a.custodian_wf_accounts_extInfo).filter(a.custodian_wf_accounts_extInfo.col_f1 == custodian_wf_accounts_ext_id).first()
    if db_custodian_wf_accounts_ext is None:
        raise HTTPException(status_code=404, detail="custodian_wf_accounts_ext info not found")
    for key, value in custodian_wf_accounts_ext.dict().items():
        setattr(db_custodian_wf_accounts_ext, key, value)
    db.commit()
    db.refresh(db_custodian_wf_accounts_ext)
    return db_custodian_wf_accounts_ext

# Delete a record
@app.delete("/custodian_wf_accounts_ext/custodian_wf_accounts_ext_id", response_model=custodian_wf_accounts_extInfo)
def delete_custodian_wf_accounts_ext(custodian_wf_accounts_ext_id: int, db: Session = Depends(get_db)):
    db_custodian_wf_accounts_ext = db.query(a.custodian_wf_accounts_extInfo).filter(a.custodian_wf_accounts_extInfo.col_f1 == custodian_wf_accounts_ext_id).first()
    if db_custodian_wf_accounts_ext is None:
        raise HTTPException(status_code=404, detail="custodian_wf_accounts_ext info not found")
    db.delete(db_custodian_wf_accounts_ext)
    db.commit()
    return db_custodian_wf_accounts_ext

