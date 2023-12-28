from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.encoders import jsonable_encoder
from typing import List
import database
import schemas
import models
from sqlalchemy.orm import Session

router=APIRouter(
    tags=["Orderitems"],
    prefix="/Orderitems",
    responses={404:{"description":"Not Found"}}
)

#To insert the various items in the order

@router.post("/")
def create_order_item(item:schemas.Orderitem1,db:Session=Depends(database.get_db)):
    db_order=models.Orderitem(order_id=item.order_id,product_variation_id=item.product_variation_id,quantity=item.quantity)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

#To get orderitem information

@router.get("/",response_model=List[schemas.orderItem])
def get_order_all(db:Session=Depends(database.get_db)):
    return db.query(models.Orderitem).all()

#To get specific orderitem informations

@router.get("/{id}",response_model=schemas.orderItem)
def get_orderitem(id:int,db:Session=Depends(database.get_db)):
    db_item=db.query(models.Orderitem).filter(models.Orderitem.id==id).first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Order Item Not Found")
    return db_item

