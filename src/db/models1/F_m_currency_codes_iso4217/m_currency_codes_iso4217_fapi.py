
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_m_currency_codes_iso4217.m_currency_codes_iso4217 as a
from  db.models.F_m_currency_codes_iso4217.m_currency_codes_iso4217_pyd import m_currency_codes_iso4217InfoBase, m_currency_codes_iso4217InfoCreate, m_currency_codes_iso4217InfoUpdate,m_currency_codes_iso4217InfoInDBBase, m_currency_codes_iso4217Info
#import db.models.m_currency_codes_iso4217_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/m_currency_codes_iso4217/", response_model=m_currency_codes_iso4217Info)
def create_m_currency_codes_iso4217(m_currency_codes_iso4217: m_currency_codes_iso4217InfoCreate, db: Session = Depends(get_db)):
    db_m_currency_codes_iso4217 = a.m_currency_codes_iso4217(**m_currency_codes_iso4217.dict())
    db.add(db_m_currency_codes_iso4217)
    db.commit()
    db.refresh(db_m_currency_codes_iso4217)
    return db_m_currency_codes_iso4217

# Get all records
@app.get("/m_currency_codes_iso4217/", response_model=List[m_currency_codes_iso4217Info])
def read__m_currency_codes_iso4217_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.m_currency_codes_iso4217).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/m_currency_codes_iso4217/m_currency_codes_iso4217_id", response_model=m_currency_codes_iso4217Info)
def read_m_currency_codes_iso4217(m_currency_codes_iso4217_id: int, db: Session = Depends(get_db)):
    db_m_currency_codes_iso4217 = db.query(db.models.m_currency_codes_iso4217Info).filter(db.models.m_currency_codes_iso4217Info.col_f1 == m_currency_codes_iso4217_id).first()
    if db_m_currency_codes_iso4217 is None:
        raise HTTPException(status_code=404, detail="m_currency_codes_iso4217 info not found")
    return db_m_currency_codes_iso4217

# Update a record
@app.put("/m_currency_codes_iso4217/m_currency_codes_iso4217_id", response_model=m_currency_codes_iso4217Info)
def update_m_currency_codes_iso4217(m_currency_codes_iso4217_id: int, m_currency_codes_iso4217: m_currency_codes_iso4217InfoUpdate, db: Session = Depends(get_db)):
    db_m_currency_codes_iso4217 = db.query(a.m_currency_codes_iso4217Info).filter(a.m_currency_codes_iso4217Info.col_f1 == m_currency_codes_iso4217_id).first()
    if db_m_currency_codes_iso4217 is None:
        raise HTTPException(status_code=404, detail="m_currency_codes_iso4217 info not found")
    for key, value in m_currency_codes_iso4217.dict().items():
        setattr(db_m_currency_codes_iso4217, key, value)
    db.commit()
    db.refresh(db_m_currency_codes_iso4217)
    return db_m_currency_codes_iso4217

# Delete a record
@app.delete("/m_currency_codes_iso4217/m_currency_codes_iso4217_id", response_model=m_currency_codes_iso4217Info)
def delete_m_currency_codes_iso4217(m_currency_codes_iso4217_id: int, db: Session = Depends(get_db)):
    db_m_currency_codes_iso4217 = db.query(a.m_currency_codes_iso4217Info).filter(a.m_currency_codes_iso4217Info.col_f1 == m_currency_codes_iso4217_id).first()
    if db_m_currency_codes_iso4217 is None:
        raise HTTPException(status_code=404, detail="m_currency_codes_iso4217 info not found")
    db.delete(db_m_currency_codes_iso4217)
    db.commit()
    return db_m_currency_codes_iso4217

