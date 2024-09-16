
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_managed_futures.managed_futures as a
from  db.models.F_managed_futures.managed_futures_pyd import managed_futuresInfoBase, managed_futuresInfoCreate, managed_futuresInfoUpdate,managed_futuresInfoInDBBase, managed_futuresInfo
#import db.models.managed_futures_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/managed_futures/", response_model=managed_futuresInfo)
def create_managed_futures(managed_futures: managed_futuresInfoCreate, db: Session = Depends(get_db)):
    db_managed_futures = a.managed_futures(**managed_futures.dict())
    db.add(db_managed_futures)
    db.commit()
    db.refresh(db_managed_futures)
    return db_managed_futures

# Get all records
@app.get("/managed_futures/", response_model=List[managed_futuresInfo])
def read__managed_futures_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.managed_futures).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/managed_futures/managed_futures_id", response_model=managed_futuresInfo)
def read_managed_futures(managed_futures_id: int, db: Session = Depends(get_db)):
    db_managed_futures = db.query(db.models.managed_futuresInfo).filter(db.models.managed_futuresInfo.col_f1 == managed_futures_id).first()
    if db_managed_futures is None:
        raise HTTPException(status_code=404, detail="managed_futures info not found")
    return db_managed_futures

# Update a record
@app.put("/managed_futures/managed_futures_id", response_model=managed_futuresInfo)
def update_managed_futures(managed_futures_id: int, managed_futures: managed_futuresInfoUpdate, db: Session = Depends(get_db)):
    db_managed_futures = db.query(a.managed_futuresInfo).filter(a.managed_futuresInfo.col_f1 == managed_futures_id).first()
    if db_managed_futures is None:
        raise HTTPException(status_code=404, detail="managed_futures info not found")
    for key, value in managed_futures.dict().items():
        setattr(db_managed_futures, key, value)
    db.commit()
    db.refresh(db_managed_futures)
    return db_managed_futures

# Delete a record
@app.delete("/managed_futures/managed_futures_id", response_model=managed_futuresInfo)
def delete_managed_futures(managed_futures_id: int, db: Session = Depends(get_db)):
    db_managed_futures = db.query(a.managed_futuresInfo).filter(a.managed_futuresInfo.col_f1 == managed_futures_id).first()
    if db_managed_futures is None:
        raise HTTPException(status_code=404, detail="managed_futures info not found")
    db.delete(db_managed_futures)
    db.commit()
    return db_managed_futures

