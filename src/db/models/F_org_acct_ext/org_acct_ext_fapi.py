
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_org_acct_ext.org_acct_ext as a
from  db.models.F_org_acct_ext.org_acct_ext_pyd import org_acct_extInfoBase, org_acct_extInfoCreate, org_acct_extInfoUpdate,org_acct_extInfoInDBBase, org_acct_extInfo
#import db.models.org_acct_ext_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/org_acct_ext/", response_model=org_acct_extInfo)
def create_org_acct_ext(org_acct_ext: org_acct_extInfoCreate, db: Session = Depends(get_db)):
    db_org_acct_ext = a.org_acct_ext(**org_acct_ext.dict())
    db.add(db_org_acct_ext)
    db.commit()
    db.refresh(db_org_acct_ext)
    return db_org_acct_ext

# Get all records
@app.get("/org_acct_ext/", response_model=List[org_acct_extInfo])
def read__org_acct_ext_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.org_acct_ext).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/org_acct_ext/org_acct_ext_id", response_model=org_acct_extInfo)
def read_org_acct_ext(org_acct_ext_id: int, db: Session = Depends(get_db)):
    db_org_acct_ext = db.query(db.models.org_acct_extInfo).filter(db.models.org_acct_extInfo.col_f1 == org_acct_ext_id).first()
    if db_org_acct_ext is None:
        raise HTTPException(status_code=404, detail="org_acct_ext info not found")
    return db_org_acct_ext

# Update a record
@app.put("/org_acct_ext/org_acct_ext_id", response_model=org_acct_extInfo)
def update_org_acct_ext(org_acct_ext_id: int, org_acct_ext: org_acct_extInfoUpdate, db: Session = Depends(get_db)):
    db_org_acct_ext = db.query(a.org_acct_extInfo).filter(a.org_acct_extInfo.col_f1 == org_acct_ext_id).first()
    if db_org_acct_ext is None:
        raise HTTPException(status_code=404, detail="org_acct_ext info not found")
    for key, value in org_acct_ext.dict().items():
        setattr(db_org_acct_ext, key, value)
    db.commit()
    db.refresh(db_org_acct_ext)
    return db_org_acct_ext

# Delete a record
@app.delete("/org_acct_ext/org_acct_ext_id", response_model=org_acct_extInfo)
def delete_org_acct_ext(org_acct_ext_id: int, db: Session = Depends(get_db)):
    db_org_acct_ext = db.query(a.org_acct_extInfo).filter(a.org_acct_extInfo.col_f1 == org_acct_ext_id).first()
    if db_org_acct_ext is None:
        raise HTTPException(status_code=404, detail="org_acct_ext info not found")
    db.delete(db_org_acct_ext)
    db.commit()
    return db_org_acct_ext

