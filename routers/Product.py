from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
import database
import schemas
import models
from sqlalchemy.orm import Session

router=APIRouter(
    tags=["Product"],
    prefix="/product",
    responses={404:{"description":"Not Found"}}
)

#Insert the product information

@router.post("/")
def create_product(product:schemas.Product,db:Session=Depends(database.get_db)):
    db_product=models.Product(name=product.name,description=product.description,warrenty=product.warrenty,guaranty=product.guaranty)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

#get the specific product information

@router.get("/{id}",response_model=schemas.Product_out)
def get_product(id:int,db:Session=Depends(database.get_db)):
    db_product=db.query(models.Product).filter(models.Product.id==id).first()
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product Not Found")
    return db_product

#get all products information

@router.get("/",response_model=List[schemas.Product_out])
def get_customer(db:Session=Depends(database.get_db)):
    db_customers=db.query(models.Product).all()
    return db_customers

