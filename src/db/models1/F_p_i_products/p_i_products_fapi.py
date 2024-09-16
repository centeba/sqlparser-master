
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_p_i_products.p_i_products as a
from  db.models.F_p_i_products.p_i_products_pyd import p_i_productsInfoBase, p_i_productsInfoCreate, p_i_productsInfoUpdate,p_i_productsInfoInDBBase, p_i_productsInfo
#import db.models.p_i_products_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/p_i_products/", response_model=p_i_productsInfo)
def create_p_i_products(p_i_products: p_i_productsInfoCreate, db: Session = Depends(get_db)):
    db_p_i_products = a.p_i_products(**p_i_products.dict())
    db.add(db_p_i_products)
    db.commit()
    db.refresh(db_p_i_products)
    return db_p_i_products

# Get all records
@app.get("/p_i_products/", response_model=List[p_i_productsInfo])
def read__p_i_products_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.p_i_products).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/p_i_products/p_i_products_id", response_model=p_i_productsInfo)
def read_p_i_products(p_i_products_id: int, db: Session = Depends(get_db)):
    db_p_i_products = db.query(db.models.p_i_productsInfo).filter(db.models.p_i_productsInfo.col_f1 == p_i_products_id).first()
    if db_p_i_products is None:
        raise HTTPException(status_code=404, detail="p_i_products info not found")
    return db_p_i_products

# Update a record
@app.put("/p_i_products/p_i_products_id", response_model=p_i_productsInfo)
def update_p_i_products(p_i_products_id: int, p_i_products: p_i_productsInfoUpdate, db: Session = Depends(get_db)):
    db_p_i_products = db.query(a.p_i_productsInfo).filter(a.p_i_productsInfo.col_f1 == p_i_products_id).first()
    if db_p_i_products is None:
        raise HTTPException(status_code=404, detail="p_i_products info not found")
    for key, value in p_i_products.dict().items():
        setattr(db_p_i_products, key, value)
    db.commit()
    db.refresh(db_p_i_products)
    return db_p_i_products

# Delete a record
@app.delete("/p_i_products/p_i_products_id", response_model=p_i_productsInfo)
def delete_p_i_products(p_i_products_id: int, db: Session = Depends(get_db)):
    db_p_i_products = db.query(a.p_i_productsInfo).filter(a.p_i_productsInfo.col_f1 == p_i_products_id).first()
    if db_p_i_products is None:
        raise HTTPException(status_code=404, detail="p_i_products info not found")
    db.delete(db_p_i_products)
    db.commit()
    return db_p_i_products

