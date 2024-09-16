
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import db.models.F_l_property.l_property as a
from  db.models.F_l_property.l_property_pyd import l_propertyInfoBase, l_propertyInfoCreate, l_propertyInfoUpdate,l_propertyInfoInDBBase, l_propertyInfo
#import db.models.l_property_sqla
import db_conn
from db_conn import get_db, engine
from main import app

# Routes

# Insert new record
@app.post("/l_property/", response_model=l_propertyInfo)
def create_l_property(l_property: l_propertyInfoCreate, db: Session = Depends(get_db)):
    db_l_property = a.l_property(**l_property.dict())
    db.add(db_l_property)
    db.commit()
    db.refresh(db_l_property)
    return db_l_property

# Get all records
@app.get("/l_property/", response_model=List[l_propertyInfo])
def read__l_property_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(a.l_property).offset(skip).limit(limit).all()

# Get single record matching item_id
@app.get("/l_property/l_property_id", response_model=l_propertyInfo)
def read_l_property(l_property_id: int, db: Session = Depends(get_db)):
    db_l_property = db.query(db.models.l_propertyInfo).filter(db.models.l_propertyInfo.col_f1 == l_property_id).first()
    if db_l_property is None:
        raise HTTPException(status_code=404, detail="l_property info not found")
    return db_l_property

# Update a record
@app.put("/l_property/l_property_id", response_model=l_propertyInfo)
def update_l_property(l_property_id: int, l_property: l_propertyInfoUpdate, db: Session = Depends(get_db)):
    db_l_property = db.query(a.l_propertyInfo).filter(a.l_propertyInfo.col_f1 == l_property_id).first()
    if db_l_property is None:
        raise HTTPException(status_code=404, detail="l_property info not found")
    for key, value in l_property.dict().items():
        setattr(db_l_property, key, value)
    db.commit()
    db.refresh(db_l_property)
    return db_l_property

# Delete a record
@app.delete("/l_property/l_property_id", response_model=l_propertyInfo)
def delete_l_property(l_property_id: int, db: Session = Depends(get_db)):
    db_l_property = db.query(a.l_propertyInfo).filter(a.l_propertyInfo.col_f1 == l_property_id).first()
    if db_l_property is None:
        raise HTTPException(status_code=404, detail="l_property info not found")
    db.delete(db_l_property)
    db.commit()
    return db_l_property

