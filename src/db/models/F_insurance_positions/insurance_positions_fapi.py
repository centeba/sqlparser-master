
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_insurance_positions.insurance_positions as a
from  db.models.F_insurance_positions.insurance_positions_pyd import insurance_positionsInfoBase, insurance_positionsInfoCreate, insurance_positionsInfoUpdate,insurance_positionsInfoInDBBase, insurance_positionsInfo
#import db.models.insurance_positions_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/insurance_positions/", response_model=insurance_positionsInfo)
def create_insurance_positions(insurance_positions: insurance_positionsInfoCreate, db: Session = Depends(get_db)):
    db_insurance_positions = a.insurance_positions(**insurance_positions.dict())
    db.add(db_insurance_positions)
    db.commit()
    db.refresh(db_insurance_positions)
    return db_insurance_positions

# Get all records
@app.get("/insurance_positions/", response_model=List[insurance_positionsInfo])
def read__insurance_positions_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.insurance_positions).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/insurance_positions/insurance_positions_id", response_model=insurance_positionsInfo)
def read_insurance_positions(insurance_positions_id: int, db: Session = Depends(get_db)):
    db_insurance_positions = db.query(db.models.insurance_positionsInfo).filter(db.models.insurance_positionsInfo.col_f1 == insurance_positions_id).first()
    if db_insurance_positions is None:
        raise HTTPException(status_code=404, detail="insurance_positions info not found")
    return db_insurance_positions

# Update a record
@app.put("/insurance_positions/insurance_positions_id", response_model=insurance_positionsInfo)
def update_insurance_positions(insurance_positions_id: int, insurance_positions: insurance_positionsInfoUpdate, db: Session = Depends(get_db)):
    db_insurance_positions = db.query(a.insurance_positionsInfo).filter(a.insurance_positionsInfo.col_f1 == insurance_positions_id).first()
    if db_insurance_positions is None:
        raise HTTPException(status_code=404, detail="insurance_positions info not found")
    for key, value in insurance_positions.dict().items():
        setattr(db_insurance_positions, key, value)
    db.commit()
    db.refresh(db_insurance_positions)
    return db_insurance_positions

# Delete a record
@app.delete("/insurance_positions/insurance_positions_id", response_model=insurance_positionsInfo)
def delete_insurance_positions(insurance_positions_id: int, db: Session = Depends(get_db)):
    db_insurance_positions = db.query(a.insurance_positionsInfo).filter(a.insurance_positionsInfo.col_f1 == insurance_positions_id).first()
    if db_insurance_positions is None:
        raise HTTPException(status_code=404, detail="insurance_positions info not found")
    db.delete(db_insurance_positions)
    db.commit()
    return db_insurance_positions

