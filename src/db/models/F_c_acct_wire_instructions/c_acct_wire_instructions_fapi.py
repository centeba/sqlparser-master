
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_c_acct_wire_instructions.c_acct_wire_instructions as a
from  db.models.F_c_acct_wire_instructions.c_acct_wire_instructions_pyd import c_acct_wire_instructionsInfoBase, c_acct_wire_instructionsInfoCreate, c_acct_wire_instructionsInfoUpdate,c_acct_wire_instructionsInfoInDBBase, c_acct_wire_instructionsInfo
#import db.models.c_acct_wire_instructions_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/c_acct_wire_instructions/", response_model=c_acct_wire_instructionsInfo)
def create_c_acct_wire_instructions(c_acct_wire_instructions: c_acct_wire_instructionsInfoCreate, db: Session = Depends(get_db)):
    db_c_acct_wire_instructions = a.c_acct_wire_instructions(**c_acct_wire_instructions.dict())
    db.add(db_c_acct_wire_instructions)
    db.commit()
    db.refresh(db_c_acct_wire_instructions)
    return db_c_acct_wire_instructions

# Get all records
@app.get("/c_acct_wire_instructions/", response_model=List[c_acct_wire_instructionsInfo])
def read__c_acct_wire_instructions_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.c_acct_wire_instructions).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/c_acct_wire_instructions/c_acct_wire_instructions_id", response_model=c_acct_wire_instructionsInfo)
def read_c_acct_wire_instructions(c_acct_wire_instructions_id: int, db: Session = Depends(get_db)):
    db_c_acct_wire_instructions = db.query(db.models.c_acct_wire_instructionsInfo).filter(db.models.c_acct_wire_instructionsInfo.col_f1 == c_acct_wire_instructions_id).first()
    if db_c_acct_wire_instructions is None:
        raise HTTPException(status_code=404, detail="c_acct_wire_instructions info not found")
    return db_c_acct_wire_instructions

# Update a record
@app.put("/c_acct_wire_instructions/c_acct_wire_instructions_id", response_model=c_acct_wire_instructionsInfo)
def update_c_acct_wire_instructions(c_acct_wire_instructions_id: int, c_acct_wire_instructions: c_acct_wire_instructionsInfoUpdate, db: Session = Depends(get_db)):
    db_c_acct_wire_instructions = db.query(a.c_acct_wire_instructionsInfo).filter(a.c_acct_wire_instructionsInfo.col_f1 == c_acct_wire_instructions_id).first()
    if db_c_acct_wire_instructions is None:
        raise HTTPException(status_code=404, detail="c_acct_wire_instructions info not found")
    for key, value in c_acct_wire_instructions.dict().items():
        setattr(db_c_acct_wire_instructions, key, value)
    db.commit()
    db.refresh(db_c_acct_wire_instructions)
    return db_c_acct_wire_instructions

# Delete a record
@app.delete("/c_acct_wire_instructions/c_acct_wire_instructions_id", response_model=c_acct_wire_instructionsInfo)
def delete_c_acct_wire_instructions(c_acct_wire_instructions_id: int, db: Session = Depends(get_db)):
    db_c_acct_wire_instructions = db.query(a.c_acct_wire_instructionsInfo).filter(a.c_acct_wire_instructionsInfo.col_f1 == c_acct_wire_instructions_id).first()
    if db_c_acct_wire_instructions is None:
        raise HTTPException(status_code=404, detail="c_acct_wire_instructions info not found")
    db.delete(db_c_acct_wire_instructions)
    db.commit()
    return db_c_acct_wire_instructions

