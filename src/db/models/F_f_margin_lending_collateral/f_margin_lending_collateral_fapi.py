
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_f_margin_lending_collateral.f_margin_lending_collateral as a
from  db.models.F_f_margin_lending_collateral.f_margin_lending_collateral_pyd import f_margin_lending_collateralInfoBase, f_margin_lending_collateralInfoCreate, f_margin_lending_collateralInfoUpdate,f_margin_lending_collateralInfoInDBBase, f_margin_lending_collateralInfo
#import db.models.f_margin_lending_collateral_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/f_margin_lending_collateral/", response_model=f_margin_lending_collateralInfo)
def create_f_margin_lending_collateral(f_margin_lending_collateral: f_margin_lending_collateralInfoCreate, db: Session = Depends(get_db)):
    db_f_margin_lending_collateral = a.f_margin_lending_collateral(**f_margin_lending_collateral.dict())
    db.add(db_f_margin_lending_collateral)
    db.commit()
    db.refresh(db_f_margin_lending_collateral)
    return db_f_margin_lending_collateral

# Get all records
@app.get("/f_margin_lending_collateral/", response_model=List[f_margin_lending_collateralInfo])
def read__f_margin_lending_collateral_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.f_margin_lending_collateral).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/f_margin_lending_collateral/f_margin_lending_collateral_id", response_model=f_margin_lending_collateralInfo)
def read_f_margin_lending_collateral(f_margin_lending_collateral_id: int, db: Session = Depends(get_db)):
    db_f_margin_lending_collateral = db.query(db.models.f_margin_lending_collateralInfo).filter(db.models.f_margin_lending_collateralInfo.col_f1 == f_margin_lending_collateral_id).first()
    if db_f_margin_lending_collateral is None:
        raise HTTPException(status_code=404, detail="f_margin_lending_collateral info not found")
    return db_f_margin_lending_collateral

# Update a record
@app.put("/f_margin_lending_collateral/f_margin_lending_collateral_id", response_model=f_margin_lending_collateralInfo)
def update_f_margin_lending_collateral(f_margin_lending_collateral_id: int, f_margin_lending_collateral: f_margin_lending_collateralInfoUpdate, db: Session = Depends(get_db)):
    db_f_margin_lending_collateral = db.query(a.f_margin_lending_collateralInfo).filter(a.f_margin_lending_collateralInfo.col_f1 == f_margin_lending_collateral_id).first()
    if db_f_margin_lending_collateral is None:
        raise HTTPException(status_code=404, detail="f_margin_lending_collateral info not found")
    for key, value in f_margin_lending_collateral.dict().items():
        setattr(db_f_margin_lending_collateral, key, value)
    db.commit()
    db.refresh(db_f_margin_lending_collateral)
    return db_f_margin_lending_collateral

# Delete a record
@app.delete("/f_margin_lending_collateral/f_margin_lending_collateral_id", response_model=f_margin_lending_collateralInfo)
def delete_f_margin_lending_collateral(f_margin_lending_collateral_id: int, db: Session = Depends(get_db)):
    db_f_margin_lending_collateral = db.query(a.f_margin_lending_collateralInfo).filter(a.f_margin_lending_collateralInfo.col_f1 == f_margin_lending_collateral_id).first()
    if db_f_margin_lending_collateral is None:
        raise HTTPException(status_code=404, detail="f_margin_lending_collateral info not found")
    db.delete(db_f_margin_lending_collateral)
    db.commit()
    return db_f_margin_lending_collateral

