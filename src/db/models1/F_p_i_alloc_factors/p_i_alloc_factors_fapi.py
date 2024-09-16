
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_p_i_alloc_factors.p_i_alloc_factors as a
from  db.models.F_p_i_alloc_factors.p_i_alloc_factors_pyd import p_i_alloc_factorsInfoBase, p_i_alloc_factorsInfoCreate, p_i_alloc_factorsInfoUpdate,p_i_alloc_factorsInfoInDBBase, p_i_alloc_factorsInfo
#import db.models.p_i_alloc_factors_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/p_i_alloc_factors/", response_model=p_i_alloc_factorsInfo)
def create_p_i_alloc_factors(p_i_alloc_factors: p_i_alloc_factorsInfoCreate, db: Session = Depends(get_db)):
    db_p_i_alloc_factors = a.p_i_alloc_factors(**p_i_alloc_factors.dict())
    db.add(db_p_i_alloc_factors)
    db.commit()
    db.refresh(db_p_i_alloc_factors)
    return db_p_i_alloc_factors

# Get all records
@app.get("/p_i_alloc_factors/", response_model=List[p_i_alloc_factorsInfo])
def read__p_i_alloc_factors_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.p_i_alloc_factors).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/p_i_alloc_factors/p_i_alloc_factors_id", response_model=p_i_alloc_factorsInfo)
def read_p_i_alloc_factors(p_i_alloc_factors_id: int, db: Session = Depends(get_db)):
    db_p_i_alloc_factors = db.query(db.models.p_i_alloc_factorsInfo).filter(db.models.p_i_alloc_factorsInfo.col_f1 == p_i_alloc_factors_id).first()
    if db_p_i_alloc_factors is None:
        raise HTTPException(status_code=404, detail="p_i_alloc_factors info not found")
    return db_p_i_alloc_factors

# Update a record
@app.put("/p_i_alloc_factors/p_i_alloc_factors_id", response_model=p_i_alloc_factorsInfo)
def update_p_i_alloc_factors(p_i_alloc_factors_id: int, p_i_alloc_factors: p_i_alloc_factorsInfoUpdate, db: Session = Depends(get_db)):
    db_p_i_alloc_factors = db.query(a.p_i_alloc_factorsInfo).filter(a.p_i_alloc_factorsInfo.col_f1 == p_i_alloc_factors_id).first()
    if db_p_i_alloc_factors is None:
        raise HTTPException(status_code=404, detail="p_i_alloc_factors info not found")
    for key, value in p_i_alloc_factors.dict().items():
        setattr(db_p_i_alloc_factors, key, value)
    db.commit()
    db.refresh(db_p_i_alloc_factors)
    return db_p_i_alloc_factors

# Delete a record
@app.delete("/p_i_alloc_factors/p_i_alloc_factors_id", response_model=p_i_alloc_factorsInfo)
def delete_p_i_alloc_factors(p_i_alloc_factors_id: int, db: Session = Depends(get_db)):
    db_p_i_alloc_factors = db.query(a.p_i_alloc_factorsInfo).filter(a.p_i_alloc_factorsInfo.col_f1 == p_i_alloc_factors_id).first()
    if db_p_i_alloc_factors is None:
        raise HTTPException(status_code=404, detail="p_i_alloc_factors info not found")
    db.delete(db_p_i_alloc_factors)
    db.commit()
    return db_p_i_alloc_factors

