from typing import Union,List,Optional
from pydantic import BaseModel


class Customer1(BaseModel):
    name:str
    password:str
    phone:int
    gmail:str
    referal_code:str
    



class Role(BaseModel):
    role:str
    customer_id:int

class Role1(BaseModel):
    role:str

class Customer2(BaseModel):
    name:str
    phone:int
    gmail:str
    referal_code:str
    roles:List[Role1]

    class Config:
        orm_mode=True
    
class Login(BaseModel):
    username:str
    password:str
    role:str
class Refer(BaseModel):
    referalId:int
    referedId:int

class Product(BaseModel):
    name:str
    description:str
    warrenty:int
    guaranty:int

class Productvariation(BaseModel):
    colour:str
    size:str
    price:int
    product_id:int

class Order(BaseModel):
    customer_id:int
    address:str
    Totalprice:int=0

class ProductvariationI(BaseModel):
    id:int
    colour:str
    size:str
    price:int
    product:Product

class orderinside(BaseModel):
    id:int
    quantity:int
    noofproducts:ProductvariationI

class login(BaseModel):
    username:str
    password:str
    role:str

class order_out(BaseModel):
    id:int
    address:str
    Totalprice:int
    order_customer:Customer2
    order_contain_items:List[orderinside]
    class Config:
        orm_mode=True

class Orderitem_out(BaseModel):
    id:int
    address:str
    Totalprice:int
    order_customer:Customer2

class Orderitem1(BaseModel):
    order_id:int
    product_variation_id:int
    quantity:int

class Customer_re(BaseModel):
    id:int
    referrer:Customer2
    referred:Customer2
    

class order_out_customer(BaseModel):
    id:int
    address:str
    Totalprice:int
    #orderrela:Customer1
    order_contain_items:List[orderinside]
    class Config:
        orm_mode=True

class Customer_out(BaseModel):
    id:int
    name:str
    phone:int
    gmail:str
    roles:List[Role]
    referal_code:str
    referrals_made:List[Customer_re]=[]
    referrals_received:List[Customer_re]=[]
    customerorder:List[order_out_customer]
    class Config:
        orm_mode=True

class referout(BaseModel):
    id:int
    referalId:int
    referedId:int
    referrer:Customer1=[]
    referred:Customer1=[]
    class Config:
        orm_mode=True



class Product_out(BaseModel):
    id:int
    name:str
    description:str
    warrenty:int
    guaranty:int
    product_variations:List[ProductvariationI]=[]


class sample1(BaseModel):
    id:int
    # address:str
    
class orderItem(BaseModel):
    id:int
    order:Orderitem_out
    # order:sample1
    # noofproducts:ProductvariationI
    class Config:
        orm_mode=True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    gmail: str | None = None
    role:str
