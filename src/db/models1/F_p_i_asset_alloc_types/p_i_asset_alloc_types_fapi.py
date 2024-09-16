
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_p_i_asset_alloc_types.p_i_asset_alloc_types as a
from  db.models.F_p_i_asset_alloc_types.p_i_asset_alloc_types_pyd import p_i_asset_alloc_typesInfoBase, p_i_asset_alloc_typesInfoCreate, p_i_asset_alloc_typesInfoUpdate,p_i_asset_alloc_typesInfoInDBBase, p_i_asset_alloc_typesInfo
#import db.models.p_i_asset_alloc_types_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/p_i_asset_alloc_types/", response_model=p_i_asset_alloc_typesInfo)
def create_p_i_asset_alloc_types(p_i_asset_alloc_types: p_i_asset_alloc_typesInfoCreate, db: Session = Depends(get_db)):
    db_p_i_asset_alloc_types = a.p_i_asset_alloc_types(**p_i_asset_alloc_types.dict())
    db.add(db_p_i_asset_alloc_types)
    db.commit()
    db.refresh(db_p_i_asset_alloc_types)
    return db_p_i_asset_alloc_types

# Get all records
@app.get("/p_i_asset_alloc_types/", response_model=List[p_i_asset_alloc_typesInfo])
def read__p_i_asset_alloc_types_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.p_i_asset_alloc_types).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/p_i_asset_alloc_types/p_i_asset_alloc_types_id", response_model=p_i_asset_alloc_typesInfo)
def read_p_i_asset_alloc_types(p_i_asset_alloc_types_id: int, db: Session = Depends(get_db)):
    db_p_i_asset_alloc_types = db.query(db.models.p_i_asset_alloc_typesInfo).filter(db.models.p_i_asset_alloc_typesInfo.col_f1 == p_i_asset_alloc_types_id).first()
    if db_p_i_asset_alloc_types is None:
        raise HTTPException(status_code=404, detail="p_i_asset_alloc_types info not found")
    return db_p_i_asset_alloc_types

# Update a record
@app.put("/p_i_asset_alloc_types/p_i_asset_alloc_types_id", response_model=p_i_asset_alloc_typesInfo)
def update_p_i_asset_alloc_types(p_i_asset_alloc_types_id: int, p_i_asset_alloc_types: p_i_asset_alloc_typesInfoUpdate, db: Session = Depends(get_db)):
    db_p_i_asset_alloc_types = db.query(a.p_i_asset_alloc_typesInfo).filter(a.p_i_asset_alloc_typesInfo.col_f1 == p_i_asset_alloc_types_id).first()
    if db_p_i_asset_alloc_types is None:
        raise HTTPException(status_code=404, detail="p_i_asset_alloc_types info not found")
    for key, value in p_i_asset_alloc_types.dict().items():
        setattr(db_p_i_asset_alloc_types, key, value)
    db.commit()
    db.refresh(db_p_i_asset_alloc_types)
    return db_p_i_asset_alloc_types

# Delete a record
@app.delete("/p_i_asset_alloc_types/p_i_asset_alloc_types_id", response_model=p_i_asset_alloc_typesInfo)
def delete_p_i_asset_alloc_types(p_i_asset_alloc_types_id: int, db: Session = Depends(get_db)):
    db_p_i_asset_alloc_types = db.query(a.p_i_asset_alloc_typesInfo).filter(a.p_i_asset_alloc_typesInfo.col_f1 == p_i_asset_alloc_types_id).first()
    if db_p_i_asset_alloc_types is None:
        raise HTTPException(status_code=404, detail="p_i_asset_alloc_types info not found")
    db.delete(db_p_i_asset_alloc_types)
    db.commit()
    return db_p_i_asset_alloc_types

