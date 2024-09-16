
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_p_i_asset_alloc_model_0.p_i_asset_alloc_model_0 as a
from  db.models.F_p_i_asset_alloc_model_0.p_i_asset_alloc_model_0_pyd import p_i_asset_alloc_model_0InfoBase, p_i_asset_alloc_model_0InfoCreate, p_i_asset_alloc_model_0InfoUpdate,p_i_asset_alloc_model_0InfoInDBBase, p_i_asset_alloc_model_0Info
#import db.models.p_i_asset_alloc_model_0_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/p_i_asset_alloc_model_0/", response_model=p_i_asset_alloc_model_0Info)
def create_p_i_asset_alloc_model_0(p_i_asset_alloc_model_0: p_i_asset_alloc_model_0InfoCreate, db: Session = Depends(get_db)):
    db_p_i_asset_alloc_model_0 = a.p_i_asset_alloc_model_0(**p_i_asset_alloc_model_0.dict())
    db.add(db_p_i_asset_alloc_model_0)
    db.commit()
    db.refresh(db_p_i_asset_alloc_model_0)
    return db_p_i_asset_alloc_model_0

# Get all records
@app.get("/p_i_asset_alloc_model_0/", response_model=List[p_i_asset_alloc_model_0Info])
def read__p_i_asset_alloc_model_0_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.p_i_asset_alloc_model_0).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/p_i_asset_alloc_model_0/p_i_asset_alloc_model_0_id", response_model=p_i_asset_alloc_model_0Info)
def read_p_i_asset_alloc_model_0(p_i_asset_alloc_model_0_id: int, db: Session = Depends(get_db)):
    db_p_i_asset_alloc_model_0 = db.query(db.models.p_i_asset_alloc_model_0Info).filter(db.models.p_i_asset_alloc_model_0Info.col_f1 == p_i_asset_alloc_model_0_id).first()
    if db_p_i_asset_alloc_model_0 is None:
        raise HTTPException(status_code=404, detail="p_i_asset_alloc_model_0 info not found")
    return db_p_i_asset_alloc_model_0

# Update a record
@app.put("/p_i_asset_alloc_model_0/p_i_asset_alloc_model_0_id", response_model=p_i_asset_alloc_model_0Info)
def update_p_i_asset_alloc_model_0(p_i_asset_alloc_model_0_id: int, p_i_asset_alloc_model_0: p_i_asset_alloc_model_0InfoUpdate, db: Session = Depends(get_db)):
    db_p_i_asset_alloc_model_0 = db.query(a.p_i_asset_alloc_model_0Info).filter(a.p_i_asset_alloc_model_0Info.col_f1 == p_i_asset_alloc_model_0_id).first()
    if db_p_i_asset_alloc_model_0 is None:
        raise HTTPException(status_code=404, detail="p_i_asset_alloc_model_0 info not found")
    for key, value in p_i_asset_alloc_model_0.dict().items():
        setattr(db_p_i_asset_alloc_model_0, key, value)
    db.commit()
    db.refresh(db_p_i_asset_alloc_model_0)
    return db_p_i_asset_alloc_model_0

# Delete a record
@app.delete("/p_i_asset_alloc_model_0/p_i_asset_alloc_model_0_id", response_model=p_i_asset_alloc_model_0Info)
def delete_p_i_asset_alloc_model_0(p_i_asset_alloc_model_0_id: int, db: Session = Depends(get_db)):
    db_p_i_asset_alloc_model_0 = db.query(a.p_i_asset_alloc_model_0Info).filter(a.p_i_asset_alloc_model_0Info.col_f1 == p_i_asset_alloc_model_0_id).first()
    if db_p_i_asset_alloc_model_0 is None:
        raise HTTPException(status_code=404, detail="p_i_asset_alloc_model_0 info not found")
    db.delete(db_p_i_asset_alloc_model_0)
    db.commit()
    return db_p_i_asset_alloc_model_0

