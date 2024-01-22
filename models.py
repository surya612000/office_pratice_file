from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref

from database import Base


class Customer_refer(Base):
    __tablename__="referals"
    id=Column(Integer,primary_key=True,index=True)
    referalId=Column(Integer,ForeignKey("customers.id"))
    referedId=Column(Integer,ForeignKey("customers.id"))
    
    referrer = relationship("Customer", foreign_keys=[referalId], backref=backref("referrals_made"))
    referred = relationship("Customer", foreign_keys=[referedId], backref=backref("referrals_received"))


class Customer(Base):
    __tablename__="customers"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    password=Column(String)
    phone=Column(Integer)
    gmail=Column(String,unique=True)
    referal_code=Column(String,unique=True)
    # referrals_made = relationship("Customer_refer",foreign_keys=[Customer_refer.referalId],back_populates=("referrer"))
    # referrals_received = relationship("Customer_refer", foreign_keys=[Customer_refer.referedId],back_populates=("referred"))
    # customerorder=relationship("Order",back_populates=("orderrela"))



class Product(Base):

    __tablename__="products"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    description=Column(String)
    warrenty=Column(Integer)
    guaranty=Column(Integer)
    # variations=relationship("Productvariations", cascade="all,delete",back_populates=("items"))


class Productvariations(Base):

    __tablename__="productsvariations"

    id=Column(Integer,primary_key=True,index=True)
    colour=Column(String)
    size=Column(String)
    price=Column(Integer)
    
    # types=relationship("Product",back_populates=("productsrela"))
    # product_variation=relationship("Orderitem",back_populates=("noofproducts"))

    product_id=Column(Integer,ForeignKey("products.id"))
    product = relationship("Product", backref=backref("product_variations"), foreign_keys=[product_id])


class Order(Base):

    __tablename__="orders"

    id=Column(Integer,primary_key=True,index=True)
    customer_id=Column(Integer,ForeignKey("customers.id"))
    address=Column(String)
    Totalprice=Column(Integer)

    order_customer=relationship("Customer",backref=backref("customerorder"),foreign_keys=[customer_id])
    # orderitemsrel=relationship("Orderitem",back_populates=("order"))


class Orderitem(Base):

    __tablename__="orderitem"

    id=Column(Integer,primary_key=True,index=True)
    order_id=Column(Integer,ForeignKey("orders.id"))
    product_variation_id=Column(Integer,ForeignKey("productsvariations.id"))
    quantity=Column(Integer)

    order=relationship("Order",backref=backref("order_contain_items"),foreign_keys=[order_id])
    noofproducts=relationship("Productvariations",backref=backref("product_variation"),foreign_keys=[product_variation_id])

class Roles(Base):
    __tablename__="roles"

    id=Column(Integer,primary_key=True,index=True)
    role=Column(String)
    customer_id=Column(Integer,ForeignKey("customers.id"))
    customer_details=relationship("Customer",backref=backref("roles"),foreign_keys=[customer_id])

