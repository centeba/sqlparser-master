
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_m_security_types.m_security_types as a
from  db.models.F_m_security_types.m_security_types_pyd import m_security_typesInfoBase, m_security_typesInfoCreate, m_security_typesInfoUpdate,m_security_typesInfoInDBBase, m_security_typesInfo
#import db.models.m_security_types_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/m_security_types/", response_model=m_security_typesInfo)
def create_m_security_types(m_security_types: m_security_typesInfoCreate, db: Session = Depends(get_db)):
    db_m_security_types = a.m_security_types(**m_security_types.dict())
    db.add(db_m_security_types)
    db.commit()
    db.refresh(db_m_security_types)
    return db_m_security_types

# Get all records
@app.get("/m_security_types/", response_model=List[m_security_typesInfo])
def read__m_security_types_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.m_security_types).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/m_security_types/m_security_types_id", response_model=m_security_typesInfo)
def read_m_security_types(m_security_types_id: int, db: Session = Depends(get_db)):
    db_m_security_types = db.query(db.models.m_security_typesInfo).filter(db.models.m_security_typesInfo.col_f1 == m_security_types_id).first()
    if db_m_security_types is None:
        raise HTTPException(status_code=404, detail="m_security_types info not found")
    return db_m_security_types

# Update a record
@app.put("/m_security_types/m_security_types_id", response_model=m_security_typesInfo)
def update_m_security_types(m_security_types_id: int, m_security_types: m_security_typesInfoUpdate, db: Session = Depends(get_db)):
    db_m_security_types = db.query(a.m_security_typesInfo).filter(a.m_security_typesInfo.col_f1 == m_security_types_id).first()
    if db_m_security_types is None:
        raise HTTPException(status_code=404, detail="m_security_types info not found")
    for key, value in m_security_types.dict().items():
        setattr(db_m_security_types, key, value)
    db.commit()
    db.refresh(db_m_security_types)
    return db_m_security_types

# Delete a record
@app.delete("/m_security_types/m_security_types_id", response_model=m_security_typesInfo)
def delete_m_security_types(m_security_types_id: int, db: Session = Depends(get_db)):
    db_m_security_types = db.query(a.m_security_typesInfo).filter(a.m_security_typesInfo.col_f1 == m_security_types_id).first()
    if db_m_security_types is None:
        raise HTTPException(status_code=404, detail="m_security_types info not found")
    db.delete(db_m_security_types)
    db.commit()
    return db_m_security_types

