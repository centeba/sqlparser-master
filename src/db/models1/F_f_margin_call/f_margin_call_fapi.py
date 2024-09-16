
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_f_margin_call.f_margin_call as a
from  db.models.F_f_margin_call.f_margin_call_pyd import f_margin_callInfoBase, f_margin_callInfoCreate, f_margin_callInfoUpdate,f_margin_callInfoInDBBase, f_margin_callInfo
#import db.models.f_margin_call_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/f_margin_call/", response_model=f_margin_callInfo)
def create_f_margin_call(f_margin_call: f_margin_callInfoCreate, db: Session = Depends(get_db)):
    db_f_margin_call = a.f_margin_call(**f_margin_call.dict())
    db.add(db_f_margin_call)
    db.commit()
    db.refresh(db_f_margin_call)
    return db_f_margin_call

# Get all records
@app.get("/f_margin_call/", response_model=List[f_margin_callInfo])
def read__f_margin_call_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.f_margin_call).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/f_margin_call/f_margin_call_id", response_model=f_margin_callInfo)
def read_f_margin_call(f_margin_call_id: int, db: Session = Depends(get_db)):
    db_f_margin_call = db.query(db.models.f_margin_callInfo).filter(db.models.f_margin_callInfo.col_f1 == f_margin_call_id).first()
    if db_f_margin_call is None:
        raise HTTPException(status_code=404, detail="f_margin_call info not found")
    return db_f_margin_call

# Update a record
@app.put("/f_margin_call/f_margin_call_id", response_model=f_margin_callInfo)
def update_f_margin_call(f_margin_call_id: int, f_margin_call: f_margin_callInfoUpdate, db: Session = Depends(get_db)):
    db_f_margin_call = db.query(a.f_margin_callInfo).filter(a.f_margin_callInfo.col_f1 == f_margin_call_id).first()
    if db_f_margin_call is None:
        raise HTTPException(status_code=404, detail="f_margin_call info not found")
    for key, value in f_margin_call.dict().items():
        setattr(db_f_margin_call, key, value)
    db.commit()
    db.refresh(db_f_margin_call)
    return db_f_margin_call

# Delete a record
@app.delete("/f_margin_call/f_margin_call_id", response_model=f_margin_callInfo)
def delete_f_margin_call(f_margin_call_id: int, db: Session = Depends(get_db)):
    db_f_margin_call = db.query(a.f_margin_callInfo).filter(a.f_margin_callInfo.col_f1 == f_margin_call_id).first()
    if db_f_margin_call is None:
        raise HTTPException(status_code=404, detail="f_margin_call info not found")
    db.delete(db_f_margin_call)
    db.commit()
    return db_f_margin_call

