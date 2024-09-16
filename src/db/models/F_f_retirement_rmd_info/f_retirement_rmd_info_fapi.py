
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_f_retirement_rmd_info.f_retirement_rmd_info as a
from  db.models.F_f_retirement_rmd_info.f_retirement_rmd_info_pyd import f_retirement_rmd_infoInfoBase, f_retirement_rmd_infoInfoCreate, f_retirement_rmd_infoInfoUpdate,f_retirement_rmd_infoInfoInDBBase, f_retirement_rmd_infoInfo
#import db.models.f_retirement_rmd_info_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/f_retirement_rmd_info/", response_model=f_retirement_rmd_infoInfo)
def create_f_retirement_rmd_info(f_retirement_rmd_info: f_retirement_rmd_infoInfoCreate, db: Session = Depends(get_db)):
    db_f_retirement_rmd_info = a.f_retirement_rmd_info(**f_retirement_rmd_info.dict())
    db.add(db_f_retirement_rmd_info)
    db.commit()
    db.refresh(db_f_retirement_rmd_info)
    return db_f_retirement_rmd_info

# Get all records
@app.get("/f_retirement_rmd_info/", response_model=List[f_retirement_rmd_infoInfo])
def read__f_retirement_rmd_info_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.f_retirement_rmd_info).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/f_retirement_rmd_info/f_retirement_rmd_info_id", response_model=f_retirement_rmd_infoInfo)
def read_f_retirement_rmd_info(f_retirement_rmd_info_id: int, db: Session = Depends(get_db)):
    db_f_retirement_rmd_info = db.query(db.models.f_retirement_rmd_infoInfo).filter(db.models.f_retirement_rmd_infoInfo.col_f1 == f_retirement_rmd_info_id).first()
    if db_f_retirement_rmd_info is None:
        raise HTTPException(status_code=404, detail="f_retirement_rmd_info info not found")
    return db_f_retirement_rmd_info

# Update a record
@app.put("/f_retirement_rmd_info/f_retirement_rmd_info_id", response_model=f_retirement_rmd_infoInfo)
def update_f_retirement_rmd_info(f_retirement_rmd_info_id: int, f_retirement_rmd_info: f_retirement_rmd_infoInfoUpdate, db: Session = Depends(get_db)):
    db_f_retirement_rmd_info = db.query(a.f_retirement_rmd_infoInfo).filter(a.f_retirement_rmd_infoInfo.col_f1 == f_retirement_rmd_info_id).first()
    if db_f_retirement_rmd_info is None:
        raise HTTPException(status_code=404, detail="f_retirement_rmd_info info not found")
    for key, value in f_retirement_rmd_info.dict().items():
        setattr(db_f_retirement_rmd_info, key, value)
    db.commit()
    db.refresh(db_f_retirement_rmd_info)
    return db_f_retirement_rmd_info

# Delete a record
@app.delete("/f_retirement_rmd_info/f_retirement_rmd_info_id", response_model=f_retirement_rmd_infoInfo)
def delete_f_retirement_rmd_info(f_retirement_rmd_info_id: int, db: Session = Depends(get_db)):
    db_f_retirement_rmd_info = db.query(a.f_retirement_rmd_infoInfo).filter(a.f_retirement_rmd_infoInfo.col_f1 == f_retirement_rmd_info_id).first()
    if db_f_retirement_rmd_info is None:
        raise HTTPException(status_code=404, detail="f_retirement_rmd_info info not found")
    db.delete(db_f_retirement_rmd_info)
    db.commit()
    return db_f_retirement_rmd_info

