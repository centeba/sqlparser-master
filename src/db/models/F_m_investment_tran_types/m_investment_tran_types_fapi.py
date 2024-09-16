
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_m_investment_tran_types.m_investment_tran_types as a
from  db.models.F_m_investment_tran_types.m_investment_tran_types_pyd import m_investment_tran_typesInfoBase, m_investment_tran_typesInfoCreate, m_investment_tran_typesInfoUpdate,m_investment_tran_typesInfoInDBBase, m_investment_tran_typesInfo
#import db.models.m_investment_tran_types_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/m_investment_tran_types/", response_model=m_investment_tran_typesInfo)
def create_m_investment_tran_types(m_investment_tran_types: m_investment_tran_typesInfoCreate, db: Session = Depends(get_db)):
    db_m_investment_tran_types = a.m_investment_tran_types(**m_investment_tran_types.dict())
    db.add(db_m_investment_tran_types)
    db.commit()
    db.refresh(db_m_investment_tran_types)
    return db_m_investment_tran_types

# Get all records
@app.get("/m_investment_tran_types/", response_model=List[m_investment_tran_typesInfo])
def read__m_investment_tran_types_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.m_investment_tran_types).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/m_investment_tran_types/m_investment_tran_types_id", response_model=m_investment_tran_typesInfo)
def read_m_investment_tran_types(m_investment_tran_types_id: int, db: Session = Depends(get_db)):
    db_m_investment_tran_types = db.query(db.models.m_investment_tran_typesInfo).filter(db.models.m_investment_tran_typesInfo.col_f1 == m_investment_tran_types_id).first()
    if db_m_investment_tran_types is None:
        raise HTTPException(status_code=404, detail="m_investment_tran_types info not found")
    return db_m_investment_tran_types

# Update a record
@app.put("/m_investment_tran_types/m_investment_tran_types_id", response_model=m_investment_tran_typesInfo)
def update_m_investment_tran_types(m_investment_tran_types_id: int, m_investment_tran_types: m_investment_tran_typesInfoUpdate, db: Session = Depends(get_db)):
    db_m_investment_tran_types = db.query(a.m_investment_tran_typesInfo).filter(a.m_investment_tran_typesInfo.col_f1 == m_investment_tran_types_id).first()
    if db_m_investment_tran_types is None:
        raise HTTPException(status_code=404, detail="m_investment_tran_types info not found")
    for key, value in m_investment_tran_types.dict().items():
        setattr(db_m_investment_tran_types, key, value)
    db.commit()
    db.refresh(db_m_investment_tran_types)
    return db_m_investment_tran_types

# Delete a record
@app.delete("/m_investment_tran_types/m_investment_tran_types_id", response_model=m_investment_tran_typesInfo)
def delete_m_investment_tran_types(m_investment_tran_types_id: int, db: Session = Depends(get_db)):
    db_m_investment_tran_types = db.query(a.m_investment_tran_typesInfo).filter(a.m_investment_tran_typesInfo.col_f1 == m_investment_tran_types_id).first()
    if db_m_investment_tran_types is None:
        raise HTTPException(status_code=404, detail="m_investment_tran_types info not found")
    db.delete(db_m_investment_tran_types)
    db.commit()
    return db_m_investment_tran_types

