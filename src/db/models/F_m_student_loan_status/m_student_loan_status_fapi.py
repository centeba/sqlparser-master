
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_m_student_loan_status.m_student_loan_status as a
from  db.models.F_m_student_loan_status.m_student_loan_status_pyd import m_student_loan_statusInfoBase, m_student_loan_statusInfoCreate, m_student_loan_statusInfoUpdate,m_student_loan_statusInfoInDBBase, m_student_loan_statusInfo
#import db.models.m_student_loan_status_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/m_student_loan_status/", response_model=m_student_loan_statusInfo)
def create_m_student_loan_status(m_student_loan_status: m_student_loan_statusInfoCreate, db: Session = Depends(get_db)):
    db_m_student_loan_status = a.m_student_loan_status(**m_student_loan_status.dict())
    db.add(db_m_student_loan_status)
    db.commit()
    db.refresh(db_m_student_loan_status)
    return db_m_student_loan_status

# Get all records
@app.get("/m_student_loan_status/", response_model=List[m_student_loan_statusInfo])
def read__m_student_loan_status_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.m_student_loan_status).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/m_student_loan_status/m_student_loan_status_id", response_model=m_student_loan_statusInfo)
def read_m_student_loan_status(m_student_loan_status_id: int, db: Session = Depends(get_db)):
    db_m_student_loan_status = db.query(db.models.m_student_loan_statusInfo).filter(db.models.m_student_loan_statusInfo.col_f1 == m_student_loan_status_id).first()
    if db_m_student_loan_status is None:
        raise HTTPException(status_code=404, detail="m_student_loan_status info not found")
    return db_m_student_loan_status

# Update a record
@app.put("/m_student_loan_status/m_student_loan_status_id", response_model=m_student_loan_statusInfo)
def update_m_student_loan_status(m_student_loan_status_id: int, m_student_loan_status: m_student_loan_statusInfoUpdate, db: Session = Depends(get_db)):
    db_m_student_loan_status = db.query(a.m_student_loan_statusInfo).filter(a.m_student_loan_statusInfo.col_f1 == m_student_loan_status_id).first()
    if db_m_student_loan_status is None:
        raise HTTPException(status_code=404, detail="m_student_loan_status info not found")
    for key, value in m_student_loan_status.dict().items():
        setattr(db_m_student_loan_status, key, value)
    db.commit()
    db.refresh(db_m_student_loan_status)
    return db_m_student_loan_status

# Delete a record
@app.delete("/m_student_loan_status/m_student_loan_status_id", response_model=m_student_loan_statusInfo)
def delete_m_student_loan_status(m_student_loan_status_id: int, db: Session = Depends(get_db)):
    db_m_student_loan_status = db.query(a.m_student_loan_statusInfo).filter(a.m_student_loan_statusInfo.col_f1 == m_student_loan_status_id).first()
    if db_m_student_loan_status is None:
        raise HTTPException(status_code=404, detail="m_student_loan_status info not found")
    db.delete(db_m_student_loan_status)
    db.commit()
    return db_m_student_loan_status

