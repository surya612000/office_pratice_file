# authentication.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt_token  

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

   
    token_data = jwt_token.verify_token(token, credentials_exception)

    # if required_role and getattr(token_data, "role") != required_role:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail="You do not have access to this resource",
    #     )

    return token_data
