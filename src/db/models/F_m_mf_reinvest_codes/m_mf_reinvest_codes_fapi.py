
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_m_mf_reinvest_codes.m_mf_reinvest_codes as a
from  db.models.F_m_mf_reinvest_codes.m_mf_reinvest_codes_pyd import m_mf_reinvest_codesInfoBase, m_mf_reinvest_codesInfoCreate, m_mf_reinvest_codesInfoUpdate,m_mf_reinvest_codesInfoInDBBase, m_mf_reinvest_codesInfo
#import db.models.m_mf_reinvest_codes_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/m_mf_reinvest_codes/", response_model=m_mf_reinvest_codesInfo)
def create_m_mf_reinvest_codes(m_mf_reinvest_codes: m_mf_reinvest_codesInfoCreate, db: Session = Depends(get_db)):
    db_m_mf_reinvest_codes = a.m_mf_reinvest_codes(**m_mf_reinvest_codes.dict())
    db.add(db_m_mf_reinvest_codes)
    db.commit()
    db.refresh(db_m_mf_reinvest_codes)
    return db_m_mf_reinvest_codes

# Get all records
@app.get("/m_mf_reinvest_codes/", response_model=List[m_mf_reinvest_codesInfo])
def read__m_mf_reinvest_codes_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.m_mf_reinvest_codes).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/m_mf_reinvest_codes/m_mf_reinvest_codes_id", response_model=m_mf_reinvest_codesInfo)
def read_m_mf_reinvest_codes(m_mf_reinvest_codes_id: int, db: Session = Depends(get_db)):
    db_m_mf_reinvest_codes = db.query(db.models.m_mf_reinvest_codesInfo).filter(db.models.m_mf_reinvest_codesInfo.col_f1 == m_mf_reinvest_codes_id).first()
    if db_m_mf_reinvest_codes is None:
        raise HTTPException(status_code=404, detail="m_mf_reinvest_codes info not found")
    return db_m_mf_reinvest_codes

# Update a record
@app.put("/m_mf_reinvest_codes/m_mf_reinvest_codes_id", response_model=m_mf_reinvest_codesInfo)
def update_m_mf_reinvest_codes(m_mf_reinvest_codes_id: int, m_mf_reinvest_codes: m_mf_reinvest_codesInfoUpdate, db: Session = Depends(get_db)):
    db_m_mf_reinvest_codes = db.query(a.m_mf_reinvest_codesInfo).filter(a.m_mf_reinvest_codesInfo.col_f1 == m_mf_reinvest_codes_id).first()
    if db_m_mf_reinvest_codes is None:
        raise HTTPException(status_code=404, detail="m_mf_reinvest_codes info not found")
    for key, value in m_mf_reinvest_codes.dict().items():
        setattr(db_m_mf_reinvest_codes, key, value)
    db.commit()
    db.refresh(db_m_mf_reinvest_codes)
    return db_m_mf_reinvest_codes

# Delete a record
@app.delete("/m_mf_reinvest_codes/m_mf_reinvest_codes_id", response_model=m_mf_reinvest_codesInfo)
def delete_m_mf_reinvest_codes(m_mf_reinvest_codes_id: int, db: Session = Depends(get_db)):
    db_m_mf_reinvest_codes = db.query(a.m_mf_reinvest_codesInfo).filter(a.m_mf_reinvest_codesInfo.col_f1 == m_mf_reinvest_codes_id).first()
    if db_m_mf_reinvest_codes is None:
        raise HTTPException(status_code=404, detail="m_mf_reinvest_codes info not found")
    db.delete(db_m_mf_reinvest_codes)
    db.commit()
    return db_m_mf_reinvest_codes

