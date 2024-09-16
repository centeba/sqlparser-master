
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_m_asset_taxonomy.m_asset_taxonomy as a
from  db.models.F_m_asset_taxonomy.m_asset_taxonomy_pyd import m_asset_taxonomyInfoBase, m_asset_taxonomyInfoCreate, m_asset_taxonomyInfoUpdate,m_asset_taxonomyInfoInDBBase, m_asset_taxonomyInfo
#import db.models.m_asset_taxonomy_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/m_asset_taxonomy/", response_model=m_asset_taxonomyInfo)
def create_m_asset_taxonomy(m_asset_taxonomy: m_asset_taxonomyInfoCreate, db: Session = Depends(get_db)):
    db_m_asset_taxonomy = a.m_asset_taxonomy(**m_asset_taxonomy.dict())
    db.add(db_m_asset_taxonomy)
    db.commit()
    db.refresh(db_m_asset_taxonomy)
    return db_m_asset_taxonomy

# Get all records
@app.get("/m_asset_taxonomy/", response_model=List[m_asset_taxonomyInfo])
def read__m_asset_taxonomy_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.m_asset_taxonomy).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/m_asset_taxonomy/m_asset_taxonomy_id", response_model=m_asset_taxonomyInfo)
def read_m_asset_taxonomy(m_asset_taxonomy_id: int, db: Session = Depends(get_db)):
    db_m_asset_taxonomy = db.query(db.models.m_asset_taxonomyInfo).filter(db.models.m_asset_taxonomyInfo.col_f1 == m_asset_taxonomy_id).first()
    if db_m_asset_taxonomy is None:
        raise HTTPException(status_code=404, detail="m_asset_taxonomy info not found")
    return db_m_asset_taxonomy

# Update a record
@app.put("/m_asset_taxonomy/m_asset_taxonomy_id", response_model=m_asset_taxonomyInfo)
def update_m_asset_taxonomy(m_asset_taxonomy_id: int, m_asset_taxonomy: m_asset_taxonomyInfoUpdate, db: Session = Depends(get_db)):
    db_m_asset_taxonomy = db.query(a.m_asset_taxonomyInfo).filter(a.m_asset_taxonomyInfo.col_f1 == m_asset_taxonomy_id).first()
    if db_m_asset_taxonomy is None:
        raise HTTPException(status_code=404, detail="m_asset_taxonomy info not found")
    for key, value in m_asset_taxonomy.dict().items():
        setattr(db_m_asset_taxonomy, key, value)
    db.commit()
    db.refresh(db_m_asset_taxonomy)
    return db_m_asset_taxonomy

# Delete a record
@app.delete("/m_asset_taxonomy/m_asset_taxonomy_id", response_model=m_asset_taxonomyInfo)
def delete_m_asset_taxonomy(m_asset_taxonomy_id: int, db: Session = Depends(get_db)):
    db_m_asset_taxonomy = db.query(a.m_asset_taxonomyInfo).filter(a.m_asset_taxonomyInfo.col_f1 == m_asset_taxonomy_id).first()
    if db_m_asset_taxonomy is None:
        raise HTTPException(status_code=404, detail="m_asset_taxonomy info not found")
    db.delete(db_m_asset_taxonomy)
    db.commit()
    return db_m_asset_taxonomy

