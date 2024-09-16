
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_m_acct_types.m_acct_types as a
from  db.models.F_m_acct_types.m_acct_types_pyd import m_acct_typesInfoBase, m_acct_typesInfoCreate, m_acct_typesInfoUpdate,m_acct_typesInfoInDBBase, m_acct_typesInfo
#import db.models.m_acct_types_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/m_acct_types/", response_model=m_acct_typesInfo)
def create_m_acct_types(m_acct_types: m_acct_typesInfoCreate, db: Session = Depends(get_db)):
    db_m_acct_types = a.m_acct_types(**m_acct_types.dict())
    db.add(db_m_acct_types)
    db.commit()
    db.refresh(db_m_acct_types)
    return db_m_acct_types

# Get all records
@app.get("/m_acct_types/", response_model=List[m_acct_typesInfo])
def read__m_acct_types_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.m_acct_types).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/m_acct_types/m_acct_types_id", response_model=m_acct_typesInfo)
def read_m_acct_types(m_acct_types_id: int, db: Session = Depends(get_db)):
    db_m_acct_types = db.query(db.models.m_acct_typesInfo).filter(db.models.m_acct_typesInfo.col_f1 == m_acct_types_id).first()
    if db_m_acct_types is None:
        raise HTTPException(status_code=404, detail="m_acct_types info not found")
    return db_m_acct_types

# Update a record
@app.put("/m_acct_types/m_acct_types_id", response_model=m_acct_typesInfo)
def update_m_acct_types(m_acct_types_id: int, m_acct_types: m_acct_typesInfoUpdate, db: Session = Depends(get_db)):
    db_m_acct_types = db.query(a.m_acct_typesInfo).filter(a.m_acct_typesInfo.col_f1 == m_acct_types_id).first()
    if db_m_acct_types is None:
        raise HTTPException(status_code=404, detail="m_acct_types info not found")
    for key, value in m_acct_types.dict().items():
        setattr(db_m_acct_types, key, value)
    db.commit()
    db.refresh(db_m_acct_types)
    return db_m_acct_types

# Delete a record
@app.delete("/m_acct_types/m_acct_types_id", response_model=m_acct_typesInfo)
def delete_m_acct_types(m_acct_types_id: int, db: Session = Depends(get_db)):
    db_m_acct_types = db.query(a.m_acct_typesInfo).filter(a.m_acct_typesInfo.col_f1 == m_acct_types_id).first()
    if db_m_acct_types is None:
        raise HTTPException(status_code=404, detail="m_acct_types info not found")
    db.delete(db_m_acct_types)
    db.commit()
    return db_m_acct_types

