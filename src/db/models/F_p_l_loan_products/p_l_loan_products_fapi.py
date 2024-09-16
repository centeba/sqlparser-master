
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_p_l_loan_products.p_l_loan_products as a
from  db.models.F_p_l_loan_products.p_l_loan_products_pyd import p_l_loan_productsInfoBase, p_l_loan_productsInfoCreate, p_l_loan_productsInfoUpdate,p_l_loan_productsInfoInDBBase, p_l_loan_productsInfo
#import db.models.p_l_loan_products_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/p_l_loan_products/", response_model=p_l_loan_productsInfo)
def create_p_l_loan_products(p_l_loan_products: p_l_loan_productsInfoCreate, db: Session = Depends(get_db)):
    db_p_l_loan_products = a.p_l_loan_products(**p_l_loan_products.dict())
    db.add(db_p_l_loan_products)
    db.commit()
    db.refresh(db_p_l_loan_products)
    return db_p_l_loan_products

# Get all records
@app.get("/p_l_loan_products/", response_model=List[p_l_loan_productsInfo])
def read__p_l_loan_products_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.p_l_loan_products).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/p_l_loan_products/p_l_loan_products_id", response_model=p_l_loan_productsInfo)
def read_p_l_loan_products(p_l_loan_products_id: int, db: Session = Depends(get_db)):
    db_p_l_loan_products = db.query(db.models.p_l_loan_productsInfo).filter(db.models.p_l_loan_productsInfo.col_f1 == p_l_loan_products_id).first()
    if db_p_l_loan_products is None:
        raise HTTPException(status_code=404, detail="p_l_loan_products info not found")
    return db_p_l_loan_products

# Update a record
@app.put("/p_l_loan_products/p_l_loan_products_id", response_model=p_l_loan_productsInfo)
def update_p_l_loan_products(p_l_loan_products_id: int, p_l_loan_products: p_l_loan_productsInfoUpdate, db: Session = Depends(get_db)):
    db_p_l_loan_products = db.query(a.p_l_loan_productsInfo).filter(a.p_l_loan_productsInfo.col_f1 == p_l_loan_products_id).first()
    if db_p_l_loan_products is None:
        raise HTTPException(status_code=404, detail="p_l_loan_products info not found")
    for key, value in p_l_loan_products.dict().items():
        setattr(db_p_l_loan_products, key, value)
    db.commit()
    db.refresh(db_p_l_loan_products)
    return db_p_l_loan_products

# Delete a record
@app.delete("/p_l_loan_products/p_l_loan_products_id", response_model=p_l_loan_productsInfo)
def delete_p_l_loan_products(p_l_loan_products_id: int, db: Session = Depends(get_db)):
    db_p_l_loan_products = db.query(a.p_l_loan_productsInfo).filter(a.p_l_loan_productsInfo.col_f1 == p_l_loan_products_id).first()
    if db_p_l_loan_products is None:
        raise HTTPException(status_code=404, detail="p_l_loan_products info not found")
    db.delete(db_p_l_loan_products)
    db.commit()
    return db_p_l_loan_products

