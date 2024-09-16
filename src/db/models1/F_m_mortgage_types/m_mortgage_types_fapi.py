
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_m_mortgage_types.m_mortgage_types as a
from  db.models.F_m_mortgage_types.m_mortgage_types_pyd import m_mortgage_typesInfoBase, m_mortgage_typesInfoCreate, m_mortgage_typesInfoUpdate,m_mortgage_typesInfoInDBBase, m_mortgage_typesInfo
#import db.models.m_mortgage_types_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/m_mortgage_types/", response_model=m_mortgage_typesInfo)
def create_m_mortgage_types(m_mortgage_types: m_mortgage_typesInfoCreate, db: Session = Depends(get_db)):
    db_m_mortgage_types = a.m_mortgage_types(**m_mortgage_types.dict())
    db.add(db_m_mortgage_types)
    db.commit()
    db.refresh(db_m_mortgage_types)
    return db_m_mortgage_types

# Get all records
@app.get("/m_mortgage_types/", response_model=List[m_mortgage_typesInfo])
def read__m_mortgage_types_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.m_mortgage_types).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/m_mortgage_types/m_mortgage_types_id", response_model=m_mortgage_typesInfo)
def read_m_mortgage_types(m_mortgage_types_id: int, db: Session = Depends(get_db)):
    db_m_mortgage_types = db.query(db.models.m_mortgage_typesInfo).filter(db.models.m_mortgage_typesInfo.col_f1 == m_mortgage_types_id).first()
    if db_m_mortgage_types is None:
        raise HTTPException(status_code=404, detail="m_mortgage_types info not found")
    return db_m_mortgage_types

# Update a record
@app.put("/m_mortgage_types/m_mortgage_types_id", response_model=m_mortgage_typesInfo)
def update_m_mortgage_types(m_mortgage_types_id: int, m_mortgage_types: m_mortgage_typesInfoUpdate, db: Session = Depends(get_db)):
    db_m_mortgage_types = db.query(a.m_mortgage_typesInfo).filter(a.m_mortgage_typesInfo.col_f1 == m_mortgage_types_id).first()
    if db_m_mortgage_types is None:
        raise HTTPException(status_code=404, detail="m_mortgage_types info not found")
    for key, value in m_mortgage_types.dict().items():
        setattr(db_m_mortgage_types, key, value)
    db.commit()
    db.refresh(db_m_mortgage_types)
    return db_m_mortgage_types

# Delete a record
@app.delete("/m_mortgage_types/m_mortgage_types_id", response_model=m_mortgage_typesInfo)
def delete_m_mortgage_types(m_mortgage_types_id: int, db: Session = Depends(get_db)):
    db_m_mortgage_types = db.query(a.m_mortgage_typesInfo).filter(a.m_mortgage_typesInfo.col_f1 == m_mortgage_types_id).first()
    if db_m_mortgage_types is None:
        raise HTTPException(status_code=404, detail="m_mortgage_types info not found")
    db.delete(db_m_mortgage_types)
    db.commit()
    return db_m_mortgage_types

