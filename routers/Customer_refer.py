from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
import database
import schemas
import models
from sqlalchemy.orm import Session

router=APIRouter(
    tags=["Customer_refer"],
    prefix="/customer_refer",
    responses={404:{"description":"Not Found"}}
)


#To specify referral

@router.post("/")
def referal(customer:schemas.Refer,db:Session=Depends(database.get_db)):
    db_refer=models.Customer_refer(referalId=customer.referalId,referedId=customer.referedId)
    db.add(db_refer)
    db.commit()
    db.refresh(db_refer)
    return db_refer


#get all refer information

@router.get("/",response_model=List[schemas.referout])
def get_all(db:Session=Depends(database.get_db)):
    db_r=db.query(models.Customer_refer).all()
    return db_r

#get the specific referal information

@router.get("/{id}",response_model=schemas.referout)
def get_refer(id:int,db:Session=Depends(database.get_db)):
    db_re=db.query(models.Customer_refer).filter(models.Customer_refer.id==id).first()
   
    if db_re is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Refer Information is not Found")
    return db_re
