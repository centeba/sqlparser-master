
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_p_i_programs_inv.p_i_programs_inv as a
from  db.models.F_p_i_programs_inv.p_i_programs_inv_pyd import p_i_programs_invInfoBase, p_i_programs_invInfoCreate, p_i_programs_invInfoUpdate,p_i_programs_invInfoInDBBase, p_i_programs_invInfo
#import db.models.p_i_programs_inv_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/p_i_programs_inv/", response_model=p_i_programs_invInfo)
def create_p_i_programs_inv(p_i_programs_inv: p_i_programs_invInfoCreate, db: Session = Depends(get_db)):
    db_p_i_programs_inv = a.p_i_programs_inv(**p_i_programs_inv.dict())
    db.add(db_p_i_programs_inv)
    db.commit()
    db.refresh(db_p_i_programs_inv)
    return db_p_i_programs_inv

# Get all records
@app.get("/p_i_programs_inv/", response_model=List[p_i_programs_invInfo])
def read__p_i_programs_inv_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.p_i_programs_inv).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/p_i_programs_inv/p_i_programs_inv_id", response_model=p_i_programs_invInfo)
def read_p_i_programs_inv(p_i_programs_inv_id: int, db: Session = Depends(get_db)):
    db_p_i_programs_inv = db.query(db.models.p_i_programs_invInfo).filter(db.models.p_i_programs_invInfo.col_f1 == p_i_programs_inv_id).first()
    if db_p_i_programs_inv is None:
        raise HTTPException(status_code=404, detail="p_i_programs_inv info not found")
    return db_p_i_programs_inv

# Update a record
@app.put("/p_i_programs_inv/p_i_programs_inv_id", response_model=p_i_programs_invInfo)
def update_p_i_programs_inv(p_i_programs_inv_id: int, p_i_programs_inv: p_i_programs_invInfoUpdate, db: Session = Depends(get_db)):
    db_p_i_programs_inv = db.query(a.p_i_programs_invInfo).filter(a.p_i_programs_invInfo.col_f1 == p_i_programs_inv_id).first()
    if db_p_i_programs_inv is None:
        raise HTTPException(status_code=404, detail="p_i_programs_inv info not found")
    for key, value in p_i_programs_inv.dict().items():
        setattr(db_p_i_programs_inv, key, value)
    db.commit()
    db.refresh(db_p_i_programs_inv)
    return db_p_i_programs_inv

# Delete a record
@app.delete("/p_i_programs_inv/p_i_programs_inv_id", response_model=p_i_programs_invInfo)
def delete_p_i_programs_inv(p_i_programs_inv_id: int, db: Session = Depends(get_db)):
    db_p_i_programs_inv = db.query(a.p_i_programs_invInfo).filter(a.p_i_programs_invInfo.col_f1 == p_i_programs_inv_id).first()
    if db_p_i_programs_inv is None:
        raise HTTPException(status_code=404, detail="p_i_programs_inv info not found")
    db.delete(db_p_i_programs_inv)
    db.commit()
    return db_p_i_programs_inv

