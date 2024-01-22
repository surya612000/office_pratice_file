from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.encoders import jsonable_encoder
from typing import List,Union
import database
import schemas
import models,oauth2
from sqlalchemy.orm import Session,joinedload

router=APIRouter(
    tags=["Order"],
    prefix="/Order",
    responses={404:{"description":"Not Found"}}
)

#Inserting the order information


@router.post("/",response_model=schemas.order_out)
def create_order(order:schemas.Order,db:Session=Depends(database.get_db),get_current_user:schemas.Customer1=Depends(oauth2.get_current_user)):
    db_order=models.Order(customer_id=order.customer_id,Totalprice=order.Totalprice,address=order.address)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

#Getting all order informations

@router.get("/")
def get_order(db:Session=Depends(database.get_db),get_current_user:schemas.Customer1=Depends(oauth2.get_current_user))-> Union[schemas.order_out,List[schemas.order_out], None]:
    if get_current_user.role=="admin":
        return db.query(models.Order).all()
    else:
        current_user_gmail = get_current_user.gmail
    
        orders_for_current_user = (
            db.query(models.Order)
            .join(models.Customer,models.Order.customer_id==models.Customer.id)
            .options(joinedload(models.Order.order_customer))
            .filter(models.Customer.gmail==current_user_gmail)
            .all()
        )
        return orders_for_current_user
        # return db.query(models.Order).options(joinedload(models.Order.order_customer)).filter(models.Customer.gmail==get_current_user.name).all()

#to get specific order information

@router.get("/{id}",response_model=schemas.order_out)
def get_order(id:int,db:Session=Depends(database.get_db),get_current_user:schemas.Customer1=Depends(oauth2.get_current_user)):
    db_order=db.query(models.Order).filter(models.Order.id==id).first()
    if db_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Order is not Found")
    orderItems=db_order.order_contain_items
    total_price=0
    individualprice=0
    #calculating the total price based on the quantity of the indivifual price
    for orderitem in orderItems:
        individualprice=orderitem.noofproducts.price*orderitem.quantity
        total_price+=individualprice
#updating the Totalprice in order table by total sum of items to the
    db_order.Totalprice=total_price
    db.commit()
    return db_order

