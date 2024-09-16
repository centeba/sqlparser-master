
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_c_user_profile.c_user_profile as a
from  db.models.F_c_user_profile.c_user_profile_pyd import c_user_profileInfoBase, c_user_profileInfoCreate, c_user_profileInfoUpdate,c_user_profileInfoInDBBase, c_user_profileInfo
#import db.models.c_user_profile_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/c_user_profile/", response_model=c_user_profileInfo)
def create_c_user_profile(c_user_profile: c_user_profileInfoCreate, db: Session = Depends(get_db)):
    db_c_user_profile = a.c_user_profile(**c_user_profile.dict())
    db.add(db_c_user_profile)
    db.commit()
    db.refresh(db_c_user_profile)
    return db_c_user_profile

# Get all records
@app.get("/c_user_profile/", response_model=List[c_user_profileInfo])
def read__c_user_profile_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.c_user_profile).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/c_user_profile/c_user_profile_id", response_model=c_user_profileInfo)
def read_c_user_profile(c_user_profile_id: int, db: Session = Depends(get_db)):
    db_c_user_profile = db.query(db.models.c_user_profileInfo).filter(db.models.c_user_profileInfo.col_f1 == c_user_profile_id).first()
    if db_c_user_profile is None:
        raise HTTPException(status_code=404, detail="c_user_profile info not found")
    return db_c_user_profile

# Update a record
@app.put("/c_user_profile/c_user_profile_id", response_model=c_user_profileInfo)
def update_c_user_profile(c_user_profile_id: int, c_user_profile: c_user_profileInfoUpdate, db: Session = Depends(get_db)):
    db_c_user_profile = db.query(a.c_user_profileInfo).filter(a.c_user_profileInfo.col_f1 == c_user_profile_id).first()
    if db_c_user_profile is None:
        raise HTTPException(status_code=404, detail="c_user_profile info not found")
    for key, value in c_user_profile.dict().items():
        setattr(db_c_user_profile, key, value)
    db.commit()
    db.refresh(db_c_user_profile)
    return db_c_user_profile

# Delete a record
@app.delete("/c_user_profile/c_user_profile_id", response_model=c_user_profileInfo)
def delete_c_user_profile(c_user_profile_id: int, db: Session = Depends(get_db)):
    db_c_user_profile = db.query(a.c_user_profileInfo).filter(a.c_user_profileInfo.col_f1 == c_user_profile_id).first()
    if db_c_user_profile is None:
        raise HTTPException(status_code=404, detail="c_user_profile info not found")
    db.delete(db_c_user_profile)
    db.commit()
    return db_c_user_profile

