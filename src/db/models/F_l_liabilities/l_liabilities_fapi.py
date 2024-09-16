
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_l_liabilities.l_liabilities as a
from  db.models.F_l_liabilities.l_liabilities_pyd import l_liabilitiesInfoBase, l_liabilitiesInfoCreate, l_liabilitiesInfoUpdate,l_liabilitiesInfoInDBBase, l_liabilitiesInfo
#import db.models.l_liabilities_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/l_liabilities/", response_model=l_liabilitiesInfo)
def create_l_liabilities(l_liabilities: l_liabilitiesInfoCreate, db: Session = Depends(get_db)):
    db_l_liabilities = a.l_liabilities(**l_liabilities.dict())
    db.add(db_l_liabilities)
    db.commit()
    db.refresh(db_l_liabilities)
    return db_l_liabilities

# Get all records
@app.get("/l_liabilities/", response_model=List[l_liabilitiesInfo])
def read__l_liabilities_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.l_liabilities).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/l_liabilities/l_liabilities_id", response_model=l_liabilitiesInfo)
def read_l_liabilities(l_liabilities_id: int, db: Session = Depends(get_db)):
    db_l_liabilities = db.query(db.models.l_liabilitiesInfo).filter(db.models.l_liabilitiesInfo.col_f1 == l_liabilities_id).first()
    if db_l_liabilities is None:
        raise HTTPException(status_code=404, detail="l_liabilities info not found")
    return db_l_liabilities

# Update a record
@app.put("/l_liabilities/l_liabilities_id", response_model=l_liabilitiesInfo)
def update_l_liabilities(l_liabilities_id: int, l_liabilities: l_liabilitiesInfoUpdate, db: Session = Depends(get_db)):
    db_l_liabilities = db.query(a.l_liabilitiesInfo).filter(a.l_liabilitiesInfo.col_f1 == l_liabilities_id).first()
    if db_l_liabilities is None:
        raise HTTPException(status_code=404, detail="l_liabilities info not found")
    for key, value in l_liabilities.dict().items():
        setattr(db_l_liabilities, key, value)
    db.commit()
    db.refresh(db_l_liabilities)
    return db_l_liabilities

# Delete a record
@app.delete("/l_liabilities/l_liabilities_id", response_model=l_liabilitiesInfo)
def delete_l_liabilities(l_liabilities_id: int, db: Session = Depends(get_db)):
    db_l_liabilities = db.query(a.l_liabilitiesInfo).filter(a.l_liabilitiesInfo.col_f1 == l_liabilities_id).first()
    if db_l_liabilities is None:
        raise HTTPException(status_code=404, detail="l_liabilities info not found")
    db.delete(db_l_liabilities)
    db.commit()
    return db_l_liabilities

