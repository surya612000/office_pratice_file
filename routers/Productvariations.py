from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
import database
import schemas
import models,oauth2
from sqlalchemy.orm import Session

router=APIRouter(
    tags=["Productvariations"],
    prefix="/productvariations",
    responses={404:{"description":"Not Found"}}
)


#Inserting the variations in products

@router.post("/")
def create_product(product:schemas.Productvariation,db:Session=Depends(database.get_db),get_current_user:schemas.Customer1=Depends(oauth2.get_current_user)):
    db_product=models.Productvariations(colour=product.colour,price=product.price,size=product.size,product_id=product.product_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


#Api to get all product variations of product

@router.get("/",response_model=List[schemas.ProductvariationI])
def get_item(db:Session=Depends(database.get_db),get_current_user:schemas.Customer1=Depends(oauth2.get_current_user)):
    db_product_variations=db.query(models.Productvariations).all()
    if db_product_variations is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Productvariations Not Found")
    return db_product_variations



#Api to get product variations of product

@router.get("/{id}",response_model=schemas.ProductvariationI)
def get_item(id:int,db:Session=Depends(database.get_db),get_current_user:schemas.Customer1=Depends(oauth2.get_current_user)):
    db_product_variations=db.query(models.Productvariations).filter(models.Productvariations.id==id).first()
    if db_product_variations is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Productvariations Not Found")
    return db_product_variations







