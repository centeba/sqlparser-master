
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_m_accrued_interest_types.m_accrued_interest_types as a
from  db.models.F_m_accrued_interest_types.m_accrued_interest_types_pyd import m_accrued_interest_typesInfoBase, m_accrued_interest_typesInfoCreate, m_accrued_interest_typesInfoUpdate,m_accrued_interest_typesInfoInDBBase, m_accrued_interest_typesInfo
#import db.models.m_accrued_interest_types_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/m_accrued_interest_types/", response_model=m_accrued_interest_typesInfo)
def create_m_accrued_interest_types(m_accrued_interest_types: m_accrued_interest_typesInfoCreate, db: Session = Depends(get_db)):
    db_m_accrued_interest_types = a.m_accrued_interest_types(**m_accrued_interest_types.dict())
    db.add(db_m_accrued_interest_types)
    db.commit()
    db.refresh(db_m_accrued_interest_types)
    return db_m_accrued_interest_types

# Get all records
@app.get("/m_accrued_interest_types/", response_model=List[m_accrued_interest_typesInfo])
def read__m_accrued_interest_types_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.m_accrued_interest_types).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/m_accrued_interest_types/m_accrued_interest_types_id", response_model=m_accrued_interest_typesInfo)
def read_m_accrued_interest_types(m_accrued_interest_types_id: int, db: Session = Depends(get_db)):
    db_m_accrued_interest_types = db.query(db.models.m_accrued_interest_typesInfo).filter(db.models.m_accrued_interest_typesInfo.col_f1 == m_accrued_interest_types_id).first()
    if db_m_accrued_interest_types is None:
        raise HTTPException(status_code=404, detail="m_accrued_interest_types info not found")
    return db_m_accrued_interest_types

# Update a record
@app.put("/m_accrued_interest_types/m_accrued_interest_types_id", response_model=m_accrued_interest_typesInfo)
def update_m_accrued_interest_types(m_accrued_interest_types_id: int, m_accrued_interest_types: m_accrued_interest_typesInfoUpdate, db: Session = Depends(get_db)):
    db_m_accrued_interest_types = db.query(a.m_accrued_interest_typesInfo).filter(a.m_accrued_interest_typesInfo.col_f1 == m_accrued_interest_types_id).first()
    if db_m_accrued_interest_types is None:
        raise HTTPException(status_code=404, detail="m_accrued_interest_types info not found")
    for key, value in m_accrued_interest_types.dict().items():
        setattr(db_m_accrued_interest_types, key, value)
    db.commit()
    db.refresh(db_m_accrued_interest_types)
    return db_m_accrued_interest_types

# Delete a record
@app.delete("/m_accrued_interest_types/m_accrued_interest_types_id", response_model=m_accrued_interest_typesInfo)
def delete_m_accrued_interest_types(m_accrued_interest_types_id: int, db: Session = Depends(get_db)):
    db_m_accrued_interest_types = db.query(a.m_accrued_interest_typesInfo).filter(a.m_accrued_interest_typesInfo.col_f1 == m_accrued_interest_types_id).first()
    if db_m_accrued_interest_types is None:
        raise HTTPException(status_code=404, detail="m_accrued_interest_types info not found")
    db.delete(db_m_accrued_interest_types)
    db.commit()
    return db_m_accrued_interest_types

