from typing import Union,List
from pydantic import BaseModel

class Customer1(BaseModel):
    name:str
    phone:int
    gmail:str
    referal_code:str
    

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
    Totalprice:int

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

class order_out(BaseModel):
    id:int
    address:str
    Totalprice:int
    order_customer:Customer1
    order_contain_items:List[orderinside]
    class Config:
        orm_mode=True

class Orderitem_out(BaseModel):
    id:int
    address:str
    Totalprice:int
    order_customer:Customer1

class Orderitem1(BaseModel):
    order_id:int
    product_variation_id:int
    quantity:int

class Customer_re(BaseModel):
    id:int
    referrer:Customer1
    referred:Customer1
    

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
    referal_code:str
    referrals_made:List[Customer_re]=[]
    # referrals_received:List[Customer_re]=[]
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

class orderItem(BaseModel):
    id:int
    order:Orderitem_out
    # noofproducts:ProductvariationI
    class Config:
        orm_mode=True
