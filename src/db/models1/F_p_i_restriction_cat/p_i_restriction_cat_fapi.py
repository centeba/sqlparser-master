
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_p_i_restriction_cat.p_i_restriction_cat as a
from  db.models.F_p_i_restriction_cat.p_i_restriction_cat_pyd import p_i_restriction_catInfoBase, p_i_restriction_catInfoCreate, p_i_restriction_catInfoUpdate,p_i_restriction_catInfoInDBBase, p_i_restriction_catInfo
#import db.models.p_i_restriction_cat_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/p_i_restriction_cat/", response_model=p_i_restriction_catInfo)
def create_p_i_restriction_cat(p_i_restriction_cat: p_i_restriction_catInfoCreate, db: Session = Depends(get_db)):
    db_p_i_restriction_cat = a.p_i_restriction_cat(**p_i_restriction_cat.dict())
    db.add(db_p_i_restriction_cat)
    db.commit()
    db.refresh(db_p_i_restriction_cat)
    return db_p_i_restriction_cat

# Get all records
@app.get("/p_i_restriction_cat/", response_model=List[p_i_restriction_catInfo])
def read__p_i_restriction_cat_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.p_i_restriction_cat).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/p_i_restriction_cat/p_i_restriction_cat_id", response_model=p_i_restriction_catInfo)
def read_p_i_restriction_cat(p_i_restriction_cat_id: int, db: Session = Depends(get_db)):
    db_p_i_restriction_cat = db.query(db.models.p_i_restriction_catInfo).filter(db.models.p_i_restriction_catInfo.col_f1 == p_i_restriction_cat_id).first()
    if db_p_i_restriction_cat is None:
        raise HTTPException(status_code=404, detail="p_i_restriction_cat info not found")
    return db_p_i_restriction_cat

# Update a record
@app.put("/p_i_restriction_cat/p_i_restriction_cat_id", response_model=p_i_restriction_catInfo)
def update_p_i_restriction_cat(p_i_restriction_cat_id: int, p_i_restriction_cat: p_i_restriction_catInfoUpdate, db: Session = Depends(get_db)):
    db_p_i_restriction_cat = db.query(a.p_i_restriction_catInfo).filter(a.p_i_restriction_catInfo.col_f1 == p_i_restriction_cat_id).first()
    if db_p_i_restriction_cat is None:
        raise HTTPException(status_code=404, detail="p_i_restriction_cat info not found")
    for key, value in p_i_restriction_cat.dict().items():
        setattr(db_p_i_restriction_cat, key, value)
    db.commit()
    db.refresh(db_p_i_restriction_cat)
    return db_p_i_restriction_cat

# Delete a record
@app.delete("/p_i_restriction_cat/p_i_restriction_cat_id", response_model=p_i_restriction_catInfo)
def delete_p_i_restriction_cat(p_i_restriction_cat_id: int, db: Session = Depends(get_db)):
    db_p_i_restriction_cat = db.query(a.p_i_restriction_catInfo).filter(a.p_i_restriction_catInfo.col_f1 == p_i_restriction_cat_id).first()
    if db_p_i_restriction_cat is None:
        raise HTTPException(status_code=404, detail="p_i_restriction_cat info not found")
    db.delete(db_p_i_restriction_cat)
    db.commit()
    return db_p_i_restriction_cat

