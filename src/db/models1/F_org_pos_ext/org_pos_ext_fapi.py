
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_org_pos_ext.org_pos_ext as a
from  db.models.F_org_pos_ext.org_pos_ext_pyd import org_pos_extInfoBase, org_pos_extInfoCreate, org_pos_extInfoUpdate,org_pos_extInfoInDBBase, org_pos_extInfo
#import db.models.org_pos_ext_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/org_pos_ext/", response_model=org_pos_extInfo)
def create_org_pos_ext(org_pos_ext: org_pos_extInfoCreate, db: Session = Depends(get_db)):
    db_org_pos_ext = a.org_pos_ext(**org_pos_ext.dict())
    db.add(db_org_pos_ext)
    db.commit()
    db.refresh(db_org_pos_ext)
    return db_org_pos_ext

# Get all records
@app.get("/org_pos_ext/", response_model=List[org_pos_extInfo])
def read__org_pos_ext_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.org_pos_ext).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/org_pos_ext/org_pos_ext_id", response_model=org_pos_extInfo)
def read_org_pos_ext(org_pos_ext_id: int, db: Session = Depends(get_db)):
    db_org_pos_ext = db.query(db.models.org_pos_extInfo).filter(db.models.org_pos_extInfo.col_f1 == org_pos_ext_id).first()
    if db_org_pos_ext is None:
        raise HTTPException(status_code=404, detail="org_pos_ext info not found")
    return db_org_pos_ext

# Update a record
@app.put("/org_pos_ext/org_pos_ext_id", response_model=org_pos_extInfo)
def update_org_pos_ext(org_pos_ext_id: int, org_pos_ext: org_pos_extInfoUpdate, db: Session = Depends(get_db)):
    db_org_pos_ext = db.query(a.org_pos_extInfo).filter(a.org_pos_extInfo.col_f1 == org_pos_ext_id).first()
    if db_org_pos_ext is None:
        raise HTTPException(status_code=404, detail="org_pos_ext info not found")
    for key, value in org_pos_ext.dict().items():
        setattr(db_org_pos_ext, key, value)
    db.commit()
    db.refresh(db_org_pos_ext)
    return db_org_pos_ext

# Delete a record
@app.delete("/org_pos_ext/org_pos_ext_id", response_model=org_pos_extInfo)
def delete_org_pos_ext(org_pos_ext_id: int, db: Session = Depends(get_db)):
    db_org_pos_ext = db.query(a.org_pos_extInfo).filter(a.org_pos_extInfo.col_f1 == org_pos_ext_id).first()
    if db_org_pos_ext is None:
        raise HTTPException(status_code=404, detail="org_pos_ext info not found")
    db.delete(db_org_pos_ext)
    db.commit()
    return db_org_pos_ext

