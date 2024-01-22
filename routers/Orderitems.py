from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.encoders import jsonable_encoder
from typing import List,Union
import database
import schemas
import models,oauth2
from sqlalchemy.orm import Session,joinedload

router=APIRouter(
    tags=["Orderitems"],
    prefix="/Orderitems",
    responses={404:{"description":"Not Found"}}
)

#To insert the various items in the order

@router.post("/")
def create_order_item(item:schemas.Orderitem1,db:Session=Depends(database.get_db),get_current_user:schemas.Customer1=Depends(oauth2.get_current_user)):
    db_order=models.Orderitem(order_id=item.order_id,product_variation_id=item.product_variation_id,quantity=item.quantity)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

#To get orderitem information

@router.get("/")
def get_order_all(db:Session=Depends(database.get_db),get_current_user:schemas.Customer1=Depends(oauth2.get_current_user))->Union[schemas.orderItem,List[schemas.orderItem],None]:
    if get_current_user.role=="admin":
        return db.query(models.Orderitem).all()
    else:
        current_user_gmail=get_current_user.gmail

        # customers_for_current_user = (
        # db.query(models.Customer)
        # .filter(models.Customer.gmail == current_user_gmail)
        # .all()
        # )

        # orders_for_current_user = (
        # db.query(models.Order)
        # .join(models.Customer)
        # .filter(models.Customer.id.in_([customer.id for customer in customers_for_current_user]))
        # .options(joinedload(models.Order.order_customer))
        # .all()
        # )

        # order_item_of_current_customer=(
        #     db.query(models.Orderitem)
        #     .join(models.Order)
        #     .filter(models.Order.id.in_([order.id for order in orders_for_current_user]))
        #     .options(joinedload(models.Orderitem.order))
        #     .all()
        # )
        orders_for_current_user = (
            db.query(models.Orderitem)
            .join(models.Order,models.Orderitem.order_id==models.Order.id)
            .join(models.Customer,models.Order.customer_id==models.Customer.id)
            
            .options(
              joinedload(models.Orderitem.order)
             .joinedload(models.Order.order_customer))
            .filter(models.Customer.gmail==current_user_gmail)
            .all()
        )
        return  orders_for_current_user

#To get specific orderitem informations

@router.get("/{id}",response_model=schemas.orderItem)
def get_orderitem(id:int,db:Session=Depends(database.get_db),get_current_user:schemas.Customer1=Depends(oauth2.get_current_user)):
    db_item=db.query(models.Orderitem).filter(models.Orderitem.id==id).first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Order Item Not Found")
    return db_item

