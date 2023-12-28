from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
import database
import schemas
import models
from sqlalchemy.orm import Session

router=APIRouter(
    tags=["Customer"],
    prefix="/customer",
    responses={404:{"description":"Not Found"}}
)

#for create customer

@router.post("/")
def create_customer(customer:schemas.Customer1,db:Session=Depends(database.get_db)):
    db_customer=models.Customer(name=customer.name,phone=customer.phone,gmail=customer.gmail,referal_code=customer.referal_code)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer



#get customer by id

@router.get("/{id}",response_model=schemas.Customer_out)
def get_customer(id:int,db:Session=Depends(database.get_db)):
    db_customer=db.query(models.Customer).filter(models.Customer.id==id).first()
    if db_customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Customer Not Found")
    return db_customer

