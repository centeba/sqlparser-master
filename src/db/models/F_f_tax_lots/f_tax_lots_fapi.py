
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_f_tax_lots.f_tax_lots as a
from  db.models.F_f_tax_lots.f_tax_lots_pyd import f_tax_lotsInfoBase, f_tax_lotsInfoCreate, f_tax_lotsInfoUpdate,f_tax_lotsInfoInDBBase, f_tax_lotsInfo
#import db.models.f_tax_lots_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/f_tax_lots/", response_model=f_tax_lotsInfo)
def create_f_tax_lots(f_tax_lots: f_tax_lotsInfoCreate, db: Session = Depends(get_db)):
    db_f_tax_lots = a.f_tax_lots(**f_tax_lots.dict())
    db.add(db_f_tax_lots)
    db.commit()
    db.refresh(db_f_tax_lots)
    return db_f_tax_lots

# Get all records
@app.get("/f_tax_lots/", response_model=List[f_tax_lotsInfo])
def read__f_tax_lots_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.f_tax_lots).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/f_tax_lots/f_tax_lots_id", response_model=f_tax_lotsInfo)
def read_f_tax_lots(f_tax_lots_id: int, db: Session = Depends(get_db)):
    db_f_tax_lots = db.query(db.models.f_tax_lotsInfo).filter(db.models.f_tax_lotsInfo.col_f1 == f_tax_lots_id).first()
    if db_f_tax_lots is None:
        raise HTTPException(status_code=404, detail="f_tax_lots info not found")
    return db_f_tax_lots

# Update a record
@app.put("/f_tax_lots/f_tax_lots_id", response_model=f_tax_lotsInfo)
def update_f_tax_lots(f_tax_lots_id: int, f_tax_lots: f_tax_lotsInfoUpdate, db: Session = Depends(get_db)):
    db_f_tax_lots = db.query(a.f_tax_lotsInfo).filter(a.f_tax_lotsInfo.col_f1 == f_tax_lots_id).first()
    if db_f_tax_lots is None:
        raise HTTPException(status_code=404, detail="f_tax_lots info not found")
    for key, value in f_tax_lots.dict().items():
        setattr(db_f_tax_lots, key, value)
    db.commit()
    db.refresh(db_f_tax_lots)
    return db_f_tax_lots

# Delete a record
@app.delete("/f_tax_lots/f_tax_lots_id", response_model=f_tax_lotsInfo)
def delete_f_tax_lots(f_tax_lots_id: int, db: Session = Depends(get_db)):
    db_f_tax_lots = db.query(a.f_tax_lotsInfo).filter(a.f_tax_lotsInfo.col_f1 == f_tax_lots_id).first()
    if db_f_tax_lots is None:
        raise HTTPException(status_code=404, detail="f_tax_lots info not found")
    db.delete(db_f_tax_lots)
    db.commit()
    return db_f_tax_lots

