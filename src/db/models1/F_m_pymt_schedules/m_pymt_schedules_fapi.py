
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_m_pymt_schedules.m_pymt_schedules as a
from  db.models.F_m_pymt_schedules.m_pymt_schedules_pyd import m_pymt_schedulesInfoBase, m_pymt_schedulesInfoCreate, m_pymt_schedulesInfoUpdate,m_pymt_schedulesInfoInDBBase, m_pymt_schedulesInfo
#import db.models.m_pymt_schedules_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/m_pymt_schedules/", response_model=m_pymt_schedulesInfo)
def create_m_pymt_schedules(m_pymt_schedules: m_pymt_schedulesInfoCreate, db: Session = Depends(get_db)):
    db_m_pymt_schedules = a.m_pymt_schedules(**m_pymt_schedules.dict())
    db.add(db_m_pymt_schedules)
    db.commit()
    db.refresh(db_m_pymt_schedules)
    return db_m_pymt_schedules

# Get all records
@app.get("/m_pymt_schedules/", response_model=List[m_pymt_schedulesInfo])
def read__m_pymt_schedules_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.m_pymt_schedules).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/m_pymt_schedules/m_pymt_schedules_id", response_model=m_pymt_schedulesInfo)
def read_m_pymt_schedules(m_pymt_schedules_id: int, db: Session = Depends(get_db)):
    db_m_pymt_schedules = db.query(db.models.m_pymt_schedulesInfo).filter(db.models.m_pymt_schedulesInfo.col_f1 == m_pymt_schedules_id).first()
    if db_m_pymt_schedules is None:
        raise HTTPException(status_code=404, detail="m_pymt_schedules info not found")
    return db_m_pymt_schedules

# Update a record
@app.put("/m_pymt_schedules/m_pymt_schedules_id", response_model=m_pymt_schedulesInfo)
def update_m_pymt_schedules(m_pymt_schedules_id: int, m_pymt_schedules: m_pymt_schedulesInfoUpdate, db: Session = Depends(get_db)):
    db_m_pymt_schedules = db.query(a.m_pymt_schedulesInfo).filter(a.m_pymt_schedulesInfo.col_f1 == m_pymt_schedules_id).first()
    if db_m_pymt_schedules is None:
        raise HTTPException(status_code=404, detail="m_pymt_schedules info not found")
    for key, value in m_pymt_schedules.dict().items():
        setattr(db_m_pymt_schedules, key, value)
    db.commit()
    db.refresh(db_m_pymt_schedules)
    return db_m_pymt_schedules

# Delete a record
@app.delete("/m_pymt_schedules/m_pymt_schedules_id", response_model=m_pymt_schedulesInfo)
def delete_m_pymt_schedules(m_pymt_schedules_id: int, db: Session = Depends(get_db)):
    db_m_pymt_schedules = db.query(a.m_pymt_schedulesInfo).filter(a.m_pymt_schedulesInfo.col_f1 == m_pymt_schedules_id).first()
    if db_m_pymt_schedules is None:
        raise HTTPException(status_code=404, detail="m_pymt_schedules info not found")
    db.delete(db_m_pymt_schedules)
    db.commit()
    return db_m_pymt_schedules

