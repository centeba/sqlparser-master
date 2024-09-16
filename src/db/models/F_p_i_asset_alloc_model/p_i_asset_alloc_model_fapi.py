
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_p_i_asset_alloc_model.p_i_asset_alloc_model as a
from  db.models.F_p_i_asset_alloc_model.p_i_asset_alloc_model_pyd import p_i_asset_alloc_modelInfoBase, p_i_asset_alloc_modelInfoCreate, p_i_asset_alloc_modelInfoUpdate,p_i_asset_alloc_modelInfoInDBBase, p_i_asset_alloc_modelInfo
#import db.models.p_i_asset_alloc_model_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/p_i_asset_alloc_model/", response_model=p_i_asset_alloc_modelInfo)
def create_p_i_asset_alloc_model(p_i_asset_alloc_model: p_i_asset_alloc_modelInfoCreate, db: Session = Depends(get_db)):
    db_p_i_asset_alloc_model = a.p_i_asset_alloc_model(**p_i_asset_alloc_model.dict())
    db.add(db_p_i_asset_alloc_model)
    db.commit()
    db.refresh(db_p_i_asset_alloc_model)
    return db_p_i_asset_alloc_model

# Get all records
@app.get("/p_i_asset_alloc_model/", response_model=List[p_i_asset_alloc_modelInfo])
def read__p_i_asset_alloc_model_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.p_i_asset_alloc_model).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/p_i_asset_alloc_model/p_i_asset_alloc_model_id", response_model=p_i_asset_alloc_modelInfo)
def read_p_i_asset_alloc_model(p_i_asset_alloc_model_id: int, db: Session = Depends(get_db)):
    db_p_i_asset_alloc_model = db.query(db.models.p_i_asset_alloc_modelInfo).filter(db.models.p_i_asset_alloc_modelInfo.col_f1 == p_i_asset_alloc_model_id).first()
    if db_p_i_asset_alloc_model is None:
        raise HTTPException(status_code=404, detail="p_i_asset_alloc_model info not found")
    return db_p_i_asset_alloc_model

# Update a record
@app.put("/p_i_asset_alloc_model/p_i_asset_alloc_model_id", response_model=p_i_asset_alloc_modelInfo)
def update_p_i_asset_alloc_model(p_i_asset_alloc_model_id: int, p_i_asset_alloc_model: p_i_asset_alloc_modelInfoUpdate, db: Session = Depends(get_db)):
    db_p_i_asset_alloc_model = db.query(a.p_i_asset_alloc_modelInfo).filter(a.p_i_asset_alloc_modelInfo.col_f1 == p_i_asset_alloc_model_id).first()
    if db_p_i_asset_alloc_model is None:
        raise HTTPException(status_code=404, detail="p_i_asset_alloc_model info not found")
    for key, value in p_i_asset_alloc_model.dict().items():
        setattr(db_p_i_asset_alloc_model, key, value)
    db.commit()
    db.refresh(db_p_i_asset_alloc_model)
    return db_p_i_asset_alloc_model

# Delete a record
@app.delete("/p_i_asset_alloc_model/p_i_asset_alloc_model_id", response_model=p_i_asset_alloc_modelInfo)
def delete_p_i_asset_alloc_model(p_i_asset_alloc_model_id: int, db: Session = Depends(get_db)):
    db_p_i_asset_alloc_model = db.query(a.p_i_asset_alloc_modelInfo).filter(a.p_i_asset_alloc_modelInfo.col_f1 == p_i_asset_alloc_model_id).first()
    if db_p_i_asset_alloc_model is None:
        raise HTTPException(status_code=404, detail="p_i_asset_alloc_model info not found")
    db.delete(db_p_i_asset_alloc_model)
    db.commit()
    return db_p_i_asset_alloc_model

