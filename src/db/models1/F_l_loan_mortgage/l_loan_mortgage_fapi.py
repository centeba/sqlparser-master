
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_l_loan_mortgage.l_loan_mortgage as a
from  db.models.F_l_loan_mortgage.l_loan_mortgage_pyd import l_loan_mortgageInfoBase, l_loan_mortgageInfoCreate, l_loan_mortgageInfoUpdate,l_loan_mortgageInfoInDBBase, l_loan_mortgageInfo
#import db.models.l_loan_mortgage_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/l_loan_mortgage/", response_model=l_loan_mortgageInfo)
def create_l_loan_mortgage(l_loan_mortgage: l_loan_mortgageInfoCreate, db: Session = Depends(get_db)):
    db_l_loan_mortgage = a.l_loan_mortgage(**l_loan_mortgage.dict())
    db.add(db_l_loan_mortgage)
    db.commit()
    db.refresh(db_l_loan_mortgage)
    return db_l_loan_mortgage

# Get all records
@app.get("/l_loan_mortgage/", response_model=List[l_loan_mortgageInfo])
def read__l_loan_mortgage_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.l_loan_mortgage).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/l_loan_mortgage/l_loan_mortgage_id", response_model=l_loan_mortgageInfo)
def read_l_loan_mortgage(l_loan_mortgage_id: int, db: Session = Depends(get_db)):
    db_l_loan_mortgage = db.query(db.models.l_loan_mortgageInfo).filter(db.models.l_loan_mortgageInfo.col_f1 == l_loan_mortgage_id).first()
    if db_l_loan_mortgage is None:
        raise HTTPException(status_code=404, detail="l_loan_mortgage info not found")
    return db_l_loan_mortgage

# Update a record
@app.put("/l_loan_mortgage/l_loan_mortgage_id", response_model=l_loan_mortgageInfo)
def update_l_loan_mortgage(l_loan_mortgage_id: int, l_loan_mortgage: l_loan_mortgageInfoUpdate, db: Session = Depends(get_db)):
    db_l_loan_mortgage = db.query(a.l_loan_mortgageInfo).filter(a.l_loan_mortgageInfo.col_f1 == l_loan_mortgage_id).first()
    if db_l_loan_mortgage is None:
        raise HTTPException(status_code=404, detail="l_loan_mortgage info not found")
    for key, value in l_loan_mortgage.dict().items():
        setattr(db_l_loan_mortgage, key, value)
    db.commit()
    db.refresh(db_l_loan_mortgage)
    return db_l_loan_mortgage

# Delete a record
@app.delete("/l_loan_mortgage/l_loan_mortgage_id", response_model=l_loan_mortgageInfo)
def delete_l_loan_mortgage(l_loan_mortgage_id: int, db: Session = Depends(get_db)):
    db_l_loan_mortgage = db.query(a.l_loan_mortgageInfo).filter(a.l_loan_mortgageInfo.col_f1 == l_loan_mortgage_id).first()
    if db_l_loan_mortgage is None:
        raise HTTPException(status_code=404, detail="l_loan_mortgage info not found")
    db.delete(db_l_loan_mortgage)
    db.commit()
    return db_l_loan_mortgage

