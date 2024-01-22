from datetime import datetime,timedelta
from jose import JWTError,jwt
import schemas

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Extract 'sub' (subject) and 'role' claims from the payload
        gmail: str = payload.get("sub")
        role: str = payload.get("role")

        # If 'sub' or 'role' is None, raise an exception
        if gmail is None or role is None:
            raise credentials_exception

        # Create a TokenData instance with the decoded name and role
        token_data = schemas.TokenData(gmail=gmail, role=role)
        return token_data

    # except jwt.ExpiredSignatureError:
    #     # Handle expired token error if needed
    #     raise credentials_exception

    except jwt.JWTError as e:
        print(f"Error decoding token: {e}")
        raise credentials_exception
