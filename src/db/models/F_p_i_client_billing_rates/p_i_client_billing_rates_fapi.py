
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_p_i_client_billing_rates.p_i_client_billing_rates as a
from  db.models.F_p_i_client_billing_rates.p_i_client_billing_rates_pyd import p_i_client_billing_ratesInfoBase, p_i_client_billing_ratesInfoCreate, p_i_client_billing_ratesInfoUpdate,p_i_client_billing_ratesInfoInDBBase, p_i_client_billing_ratesInfo
#import db.models.p_i_client_billing_rates_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/p_i_client_billing_rates/", response_model=p_i_client_billing_ratesInfo)
def create_p_i_client_billing_rates(p_i_client_billing_rates: p_i_client_billing_ratesInfoCreate, db: Session = Depends(get_db)):
    db_p_i_client_billing_rates = a.p_i_client_billing_rates(**p_i_client_billing_rates.dict())
    db.add(db_p_i_client_billing_rates)
    db.commit()
    db.refresh(db_p_i_client_billing_rates)
    return db_p_i_client_billing_rates

# Get all records
@app.get("/p_i_client_billing_rates/", response_model=List[p_i_client_billing_ratesInfo])
def read__p_i_client_billing_rates_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.p_i_client_billing_rates).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/p_i_client_billing_rates/p_i_client_billing_rates_id", response_model=p_i_client_billing_ratesInfo)
def read_p_i_client_billing_rates(p_i_client_billing_rates_id: int, db: Session = Depends(get_db)):
    db_p_i_client_billing_rates = db.query(db.models.p_i_client_billing_ratesInfo).filter(db.models.p_i_client_billing_ratesInfo.col_f1 == p_i_client_billing_rates_id).first()
    if db_p_i_client_billing_rates is None:
        raise HTTPException(status_code=404, detail="p_i_client_billing_rates info not found")
    return db_p_i_client_billing_rates

# Update a record
@app.put("/p_i_client_billing_rates/p_i_client_billing_rates_id", response_model=p_i_client_billing_ratesInfo)
def update_p_i_client_billing_rates(p_i_client_billing_rates_id: int, p_i_client_billing_rates: p_i_client_billing_ratesInfoUpdate, db: Session = Depends(get_db)):
    db_p_i_client_billing_rates = db.query(a.p_i_client_billing_ratesInfo).filter(a.p_i_client_billing_ratesInfo.col_f1 == p_i_client_billing_rates_id).first()
    if db_p_i_client_billing_rates is None:
        raise HTTPException(status_code=404, detail="p_i_client_billing_rates info not found")
    for key, value in p_i_client_billing_rates.dict().items():
        setattr(db_p_i_client_billing_rates, key, value)
    db.commit()
    db.refresh(db_p_i_client_billing_rates)
    return db_p_i_client_billing_rates

# Delete a record
@app.delete("/p_i_client_billing_rates/p_i_client_billing_rates_id", response_model=p_i_client_billing_ratesInfo)
def delete_p_i_client_billing_rates(p_i_client_billing_rates_id: int, db: Session = Depends(get_db)):
    db_p_i_client_billing_rates = db.query(a.p_i_client_billing_ratesInfo).filter(a.p_i_client_billing_ratesInfo.col_f1 == p_i_client_billing_rates_id).first()
    if db_p_i_client_billing_rates is None:
        raise HTTPException(status_code=404, detail="p_i_client_billing_rates info not found")
    db.delete(db_p_i_client_billing_rates)
    db.commit()
    return db_p_i_client_billing_rates

