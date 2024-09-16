
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_f_acct_positions.f_acct_positions as a
from  db.models.F_f_acct_positions.f_acct_positions_pyd import f_acct_positionsInfoBase, f_acct_positionsInfoCreate, f_acct_positionsInfoUpdate,f_acct_positionsInfoInDBBase, f_acct_positionsInfo
#import db.models.f_acct_positions_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/f_acct_positions/", response_model=f_acct_positionsInfo)
def create_f_acct_positions(f_acct_positions: f_acct_positionsInfoCreate, db: Session = Depends(get_db)):
    db_f_acct_positions = a.f_acct_positions(**f_acct_positions.dict())
    db.add(db_f_acct_positions)
    db.commit()
    db.refresh(db_f_acct_positions)
    return db_f_acct_positions

# Get all records
@app.get("/f_acct_positions/", response_model=List[f_acct_positionsInfo])
def read__f_acct_positions_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.f_acct_positions).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/f_acct_positions/f_acct_positions_id", response_model=f_acct_positionsInfo)
def read_f_acct_positions(f_acct_positions_id: int, db: Session = Depends(get_db)):
    db_f_acct_positions = db.query(db.models.f_acct_positionsInfo).filter(db.models.f_acct_positionsInfo.col_f1 == f_acct_positions_id).first()
    if db_f_acct_positions is None:
        raise HTTPException(status_code=404, detail="f_acct_positions info not found")
    return db_f_acct_positions

# Update a record
@app.put("/f_acct_positions/f_acct_positions_id", response_model=f_acct_positionsInfo)
def update_f_acct_positions(f_acct_positions_id: int, f_acct_positions: f_acct_positionsInfoUpdate, db: Session = Depends(get_db)):
    db_f_acct_positions = db.query(a.f_acct_positionsInfo).filter(a.f_acct_positionsInfo.col_f1 == f_acct_positions_id).first()
    if db_f_acct_positions is None:
        raise HTTPException(status_code=404, detail="f_acct_positions info not found")
    for key, value in f_acct_positions.dict().items():
        setattr(db_f_acct_positions, key, value)
    db.commit()
    db.refresh(db_f_acct_positions)
    return db_f_acct_positions

# Delete a record
@app.delete("/f_acct_positions/f_acct_positions_id", response_model=f_acct_positionsInfo)
def delete_f_acct_positions(f_acct_positions_id: int, db: Session = Depends(get_db)):
    db_f_acct_positions = db.query(a.f_acct_positionsInfo).filter(a.f_acct_positionsInfo.col_f1 == f_acct_positions_id).first()
    if db_f_acct_positions is None:
        raise HTTPException(status_code=404, detail="f_acct_positions info not found")
    db.delete(db_f_acct_positions)
    db.commit()
    return db_f_acct_positions

