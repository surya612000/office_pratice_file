from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import schemas,database,models,jwt_token,oauth2



router=APIRouter(
    tags=["login"]
)

@router.post("/login/")
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.Customer).filter(models.Customer.gmail==request.username).first()
    user1=db.query(models.Roles).filter(models.Roles.customer_id==user.id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid credentials")
    if not user.password == request.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid password")
    #generate jwt token and return 
    access_token = jwt_token.create_access_token(data={"sub": user.gmail,"role":user1.role})
    return {"access_token":access_token, "token_type":"bearer"}


# @router.get("/protected-resource/")
# def protected_resource(current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
#     # Only users with the role "admin" can access this resource
#     return {"message": "This is a protected resource", "user_role": current_user.role}