from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
import database
import schemas
import models,oauth2,jwt_token
from sqlalchemy.orm import Session

router=APIRouter(
    tags=["Customer"],
    prefix="/customer",
    responses={404:{"description":"Not Found"}}
)



#for create customer

@router.post("/")
def create_customer(customer:schemas.Customer1,db:Session=Depends(database.get_db)):
    db_customer=models.Customer(name=customer.name,password=customer.password,phone=customer.phone,gmail=customer.gmail,referal_code=customer.referal_code)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


#Get all customers

@router.get("/", response_model=List[schemas.Customer_out])
def get_all_customers(
    db: Session = Depends(database.get_db),
    get_current_user:schemas.Customer1=Depends(oauth2.get_current_user)
):
    if (get_current_user.role=="admin"):
    
        db_customers = db.query(models.Customer).all()
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have access to this resource",
        )
    return db_customers



#get customer by id

@router.get("/{id}",response_model=schemas.Customer_out)
def get_customer(id:int,db:Session=Depends(database.get_db),get_current_user:schemas.Customer1=Depends(oauth2.get_current_user)):
    db_customer=db.query(models.Customer).filter(models.Customer.id==id).first()
    if db_customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Customer Not Found")
    return db_customer

@router.post("/role/")
def get_customer(customer:schemas.Role,db:Session=Depends(database.get_db)):
    db_customer=models.Roles(role=customer.role,customer_id=customer.customer_id)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)


