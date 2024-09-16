
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_p_i_product_prog.p_i_product_prog as a
from  db.models.F_p_i_product_prog.p_i_product_prog_pyd import p_i_product_progInfoBase, p_i_product_progInfoCreate, p_i_product_progInfoUpdate,p_i_product_progInfoInDBBase, p_i_product_progInfo
#import db.models.p_i_product_prog_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/p_i_product_prog/", response_model=p_i_product_progInfo)
def create_p_i_product_prog(p_i_product_prog: p_i_product_progInfoCreate, db: Session = Depends(get_db)):
    db_p_i_product_prog = a.p_i_product_prog(**p_i_product_prog.dict())
    db.add(db_p_i_product_prog)
    db.commit()
    db.refresh(db_p_i_product_prog)
    return db_p_i_product_prog

# Get all records
@app.get("/p_i_product_prog/", response_model=List[p_i_product_progInfo])
def read__p_i_product_prog_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.p_i_product_prog).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/p_i_product_prog/p_i_product_prog_id", response_model=p_i_product_progInfo)
def read_p_i_product_prog(p_i_product_prog_id: int, db: Session = Depends(get_db)):
    db_p_i_product_prog = db.query(db.models.p_i_product_progInfo).filter(db.models.p_i_product_progInfo.col_f1 == p_i_product_prog_id).first()
    if db_p_i_product_prog is None:
        raise HTTPException(status_code=404, detail="p_i_product_prog info not found")
    return db_p_i_product_prog

# Update a record
@app.put("/p_i_product_prog/p_i_product_prog_id", response_model=p_i_product_progInfo)
def update_p_i_product_prog(p_i_product_prog_id: int, p_i_product_prog: p_i_product_progInfoUpdate, db: Session = Depends(get_db)):
    db_p_i_product_prog = db.query(a.p_i_product_progInfo).filter(a.p_i_product_progInfo.col_f1 == p_i_product_prog_id).first()
    if db_p_i_product_prog is None:
        raise HTTPException(status_code=404, detail="p_i_product_prog info not found")
    for key, value in p_i_product_prog.dict().items():
        setattr(db_p_i_product_prog, key, value)
    db.commit()
    db.refresh(db_p_i_product_prog)
    return db_p_i_product_prog

# Delete a record
@app.delete("/p_i_product_prog/p_i_product_prog_id", response_model=p_i_product_progInfo)
def delete_p_i_product_prog(p_i_product_prog_id: int, db: Session = Depends(get_db)):
    db_p_i_product_prog = db.query(a.p_i_product_progInfo).filter(a.p_i_product_progInfo.col_f1 == p_i_product_prog_id).first()
    if db_p_i_product_prog is None:
        raise HTTPException(status_code=404, detail="p_i_product_prog info not found")
    db.delete(db_p_i_product_prog)
    db.commit()
    return db_p_i_product_prog

