
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_m_cash_tran_codes.m_cash_tran_codes as a
from  db.models.F_m_cash_tran_codes.m_cash_tran_codes_pyd import m_cash_tran_codesInfoBase, m_cash_tran_codesInfoCreate, m_cash_tran_codesInfoUpdate,m_cash_tran_codesInfoInDBBase, m_cash_tran_codesInfo
#import db.models.m_cash_tran_codes_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/m_cash_tran_codes/", response_model=m_cash_tran_codesInfo)
def create_m_cash_tran_codes(m_cash_tran_codes: m_cash_tran_codesInfoCreate, db: Session = Depends(get_db)):
    db_m_cash_tran_codes = a.m_cash_tran_codes(**m_cash_tran_codes.dict())
    db.add(db_m_cash_tran_codes)
    db.commit()
    db.refresh(db_m_cash_tran_codes)
    return db_m_cash_tran_codes

# Get all records
@app.get("/m_cash_tran_codes/", response_model=List[m_cash_tran_codesInfo])
def read__m_cash_tran_codes_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.m_cash_tran_codes).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/m_cash_tran_codes/m_cash_tran_codes_id", response_model=m_cash_tran_codesInfo)
def read_m_cash_tran_codes(m_cash_tran_codes_id: int, db: Session = Depends(get_db)):
    db_m_cash_tran_codes = db.query(db.models.m_cash_tran_codesInfo).filter(db.models.m_cash_tran_codesInfo.col_f1 == m_cash_tran_codes_id).first()
    if db_m_cash_tran_codes is None:
        raise HTTPException(status_code=404, detail="m_cash_tran_codes info not found")
    return db_m_cash_tran_codes

# Update a record
@app.put("/m_cash_tran_codes/m_cash_tran_codes_id", response_model=m_cash_tran_codesInfo)
def update_m_cash_tran_codes(m_cash_tran_codes_id: int, m_cash_tran_codes: m_cash_tran_codesInfoUpdate, db: Session = Depends(get_db)):
    db_m_cash_tran_codes = db.query(a.m_cash_tran_codesInfo).filter(a.m_cash_tran_codesInfo.col_f1 == m_cash_tran_codes_id).first()
    if db_m_cash_tran_codes is None:
        raise HTTPException(status_code=404, detail="m_cash_tran_codes info not found")
    for key, value in m_cash_tran_codes.dict().items():
        setattr(db_m_cash_tran_codes, key, value)
    db.commit()
    db.refresh(db_m_cash_tran_codes)
    return db_m_cash_tran_codes

# Delete a record
@app.delete("/m_cash_tran_codes/m_cash_tran_codes_id", response_model=m_cash_tran_codesInfo)
def delete_m_cash_tran_codes(m_cash_tran_codes_id: int, db: Session = Depends(get_db)):
    db_m_cash_tran_codes = db.query(a.m_cash_tran_codesInfo).filter(a.m_cash_tran_codesInfo.col_f1 == m_cash_tran_codes_id).first()
    if db_m_cash_tran_codes is None:
        raise HTTPException(status_code=404, detail="m_cash_tran_codes info not found")
    db.delete(db_m_cash_tran_codes)
    db.commit()
    return db_m_cash_tran_codes

