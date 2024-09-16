
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_m_custodian_list.m_custodian_list as a
from  db.models.F_m_custodian_list.m_custodian_list_pyd import m_custodian_listInfoBase, m_custodian_listInfoCreate, m_custodian_listInfoUpdate,m_custodian_listInfoInDBBase, m_custodian_listInfo
#import db.models.m_custodian_list_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/m_custodian_list/", response_model=m_custodian_listInfo)
def create_m_custodian_list(m_custodian_list: m_custodian_listInfoCreate, db: Session = Depends(get_db)):
    db_m_custodian_list = a.m_custodian_list(**m_custodian_list.dict())
    db.add(db_m_custodian_list)
    db.commit()
    db.refresh(db_m_custodian_list)
    return db_m_custodian_list

# Get all records
@app.get("/m_custodian_list/", response_model=List[m_custodian_listInfo])
def read__m_custodian_list_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.m_custodian_list).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/m_custodian_list/m_custodian_list_id", response_model=m_custodian_listInfo)
def read_m_custodian_list(m_custodian_list_id: int, db: Session = Depends(get_db)):
    db_m_custodian_list = db.query(db.models.m_custodian_listInfo).filter(db.models.m_custodian_listInfo.col_f1 == m_custodian_list_id).first()
    if db_m_custodian_list is None:
        raise HTTPException(status_code=404, detail="m_custodian_list info not found")
    return db_m_custodian_list

# Update a record
@app.put("/m_custodian_list/m_custodian_list_id", response_model=m_custodian_listInfo)
def update_m_custodian_list(m_custodian_list_id: int, m_custodian_list: m_custodian_listInfoUpdate, db: Session = Depends(get_db)):
    db_m_custodian_list = db.query(a.m_custodian_listInfo).filter(a.m_custodian_listInfo.col_f1 == m_custodian_list_id).first()
    if db_m_custodian_list is None:
        raise HTTPException(status_code=404, detail="m_custodian_list info not found")
    for key, value in m_custodian_list.dict().items():
        setattr(db_m_custodian_list, key, value)
    db.commit()
    db.refresh(db_m_custodian_list)
    return db_m_custodian_list

# Delete a record
@app.delete("/m_custodian_list/m_custodian_list_id", response_model=m_custodian_listInfo)
def delete_m_custodian_list(m_custodian_list_id: int, db: Session = Depends(get_db)):
    db_m_custodian_list = db.query(a.m_custodian_listInfo).filter(a.m_custodian_listInfo.col_f1 == m_custodian_list_id).first()
    if db_m_custodian_list is None:
        raise HTTPException(status_code=404, detail="m_custodian_list info not found")
    db.delete(db_m_custodian_list)
    db.commit()
    return db_m_custodian_list

