from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.encoders import jsonable_encoder
from typing import List
import database
import schemas
import models
from sqlalchemy.orm import Session

router=APIRouter(
    tags=["Order"],
    prefix="/Order",
    responses={404:{"description":"Not Found"}}
)

#Inserting the order information


@router.post("/",response_model=schemas.order_out)
def create_order(order:schemas.Order,db:Session=Depends(database.get_db)):
    db_order=models.Order(customer_id=order.customer_id,Totalprice=order.Totalprice,address=order.address)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

#Getting all order informations

@router.get("/",response_model=List[schemas.order_out])
def get_order(db:Session=Depends(database.get_db)):
    return db.query(models.Order).all()

#to get specific order information

@router.get("/{id}",response_model=schemas.order_out)
def get_order(id:int,db:Session=Depends(database.get_db)):
    db_order=db.query(models.Order).filter(models.Order.id==id).first()
    if db_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Order is not Found")
    orderItems=db_order.order_contain_items
    priceslist=[]#price of individual order items
    quantitylist=[]#Quantity of individual order items
    #get the price of individual order items
    for orderitem in orderItems:
        priceslist.append(jsonable_encoder(orderitem.noofproducts.price))
        quantitylist.append(jsonable_encoder(orderitem.quantity))
    total_price=0
    for a in range(len(priceslist)):
        individualprice=priceslist[a]*quantitylist[a]
        total_price+=individualprice
    db_order_iditem=db.query(models.Order).filter(models.Order.id==id).first()
    #updating the Totalprice in order table by total sum of items to the
    db_order_iditem.Totalprice=total_price
    db.commit()
    return db_order

