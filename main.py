from fastapi import  FastAPI
from database import  engine,get_db
from routers import Customer,Customer_refer,Product,Productvariations,Order,Orderitems
import models


models.Base.metadata.create_all(bind=engine)


app=FastAPI()

app.include_router(Customer.router)
app.include_router(Customer_refer.router)
app.include_router(Product.router)
app.include_router(Productvariations.router)
app.include_router(Order.router)
app.include_router(Orderitems.router)


#for create customer

# @app.post("/customer/",tags=["Customer"])
# def create_customer(customer:schemas.Customer1,db:Session=Depends(get_db)):
#     db_customer=models.Customer(name=customer.name,phone=customer.phone,gmail=customer.gmail,referal_code=customer.referal_code)
#     db.add(db_customer)
#     db.commit()
#     db.refresh(db_customer)
#     return db_customer

# #To specify referral

# @app.post("/refer",tags=["Customer_refer"])
# def referal(customer:schemas.Refer,db:Session=Depends(get_db)):
#     db_refer=models.Customer_refer(referalId=customer.referalId,referedId=customer.referedId)
#     db.add(db_refer)
#     db.commit()
#     db.refresh(db_refer)
#     return db_refer

# #get customer by id

# @app.get("/customer/{id}",response_model=schemas.Customer_out,tags=["Customer"])
# def get_customer(id:int,db:Session=Depends(get_db)):
#     db_customer=db.query(models.Customer).filter(models.Customer.id==id).first()
#     if db_customer is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Customer Not Found")
#     return db_customer

# #get all refer information

# @app.get("/refer/",tags=["Customer_refer"],response_model=List[schemas.referout])
# def get_all(db:Session=Depends(get_db)):
#     db_r=db.query(models.Customer_refer).all()
#     return db_r

# #get the specific referal information

# @app.get("/refer/{id}",response_model=schemas.referout,tags=["Customer_refer"])
# def get_refer(id:int,db:Session=Depends(get_db)):
#     db_re=db.query(models.Customer_refer).filter(models.Customer_refer.id==id).first()
   
#     if db_re is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Refer Information is not Found")
#     return db_re

# #Insert the product information

# @app.post("/product/",tags=["Product"])
# def create_product(product:schemas.Product,db:Session=Depends(get_db)):
#     db_product=models.Product(name=product.name,description=product.description,warrenty=product.warrenty,guaranty=product.guaranty)
#     db.add(db_product)
#     db.commit()
#     db.refresh(db_product)
#     return db_product

# #get the specific product information

# @app.get("/product/{id}",response_model=schemas.Product_out,tags=["Product"])
# def get_product(id:int,db:Session=Depends(get_db)):
#     db_product=db.query(models.Product).filter(models.Product.id==id).first()
#     if db_product is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product Not Found")
#     return db_product

# #get all products information

# @app.get("/products/",response_model=List[schemas.Product_out],tags=["Product"])
# def get_customer(db:Session=Depends(get_db)):
#     db_customers=db.query(models.Product).all()
#     return db_customers


# #Inserting the variations in products

# @app.post("/productvariation/",tags=["Product_variation"])
# def create_product(product:schemas.Productvariation,db:Session=Depends(get_db)):
#     db_product=models.Productvariations(colour=product.colour,price=product.price,size=product.size,product_id=product.product_id)
#     db.add(db_product)
#     db.commit()
#     db.refresh(db_product)
#     return db_product


# #Api to get all product variations of product

# @app.get("/productvariation/",response_model=List[schemas.ProductvariationI],tags=["Product_variation"])
# def get_item(db:Session=Depends(get_db)):
#     db_product_variations=db.query(models.Productvariations).all()
#     if db_product_variations is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Productvariations Not Found")
#     return db_product_variations



# #Api to get product variations of product

# @app.get("/productvariation/{id}",response_model=schemas.ProductvariationI,tags=["Product_variation"])
# def get_item(id:int,db:Session=Depends(get_db)):
#     db_product_variations=db.query(models.Productvariations).filter(models.Productvariations.id==id).first()
#     if db_product_variations is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Productvariations Not Found")
#     return db_product_variations




# #Inserting the order information


# @app.post("/order/",tags=["order"],response_model=schemas.order_out)
# def create_order(order:schemas.Order,db:Session=Depends(get_db)):
#     db_order=models.Order(customer_id=order.customer_id,Totalprice=order.Totalprice,address=order.address)
#     db.add(db_order)
#     db.commit()
#     db.refresh(db_order)
#     return db_order

# #Getting all order informations

# @app.get("/order/",response_model=List[schemas.order_out],tags=["order"])
# def get_order(db:Session=Depends(get_db)):
#     return db.query(models.Order).all()

# #to get specific order information

# @app.get("/order/{id}",response_model=schemas.order_out,tags=["order"])
# def get_order(id:int,db:Session=Depends(get_db)):
#     db_order=db.query(models.Order).filter(models.Order.id==id).first()
#     if db_order is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Order is not Found")
#     orderItems=db_order.order_contain_items
#     priceslist=[]#price of individual order items
#     quantitylist=[]#Quantity of individual order items
#     #get the price of individual order items
#     for orderitem in orderItems:
#         priceslist.append(jsonable_encoder(orderitem.noofproducts.price))
#         quantitylist.append(jsonable_encoder(orderitem.quantity))
#     total_price=0
#     for a in range(len(priceslist)):
#         individualprice=priceslist[a]*quantitylist[a]
#         total_price+=individualprice
#     db_order_iditem=db.query(models.Order).filter(models.Order.id==id).first()
#     #updating the Totalprice in order table by total sum of items to the
#     db_order_iditem.Totalprice=total_price
#     db.commit()
#     return db_order

# #To insert the various items in the order

# @app.post("/orderitem/",tags=["orderItem"])
# def create_order_item(item:schemas.Orderitem1,db:Session=Depends(get_db)):
#     db_order=models.Orderitem(order_id=item.order_id,product_variation_id=item.product_variation_id,quantity=item.quantity)
#     db.add(db_order)
#     db.commit()
#     db.refresh(db_order)
#     return db_order

# #To get orderitem information

# @app.get("/orderitem/",response_model=List[schemas.orderItem],tags=["orderItem"])
# def get_order_all(db:Session=Depends(get_db)):
#     return db.query(models.Orderitem).all()

# #To get specific orderitem informations

# @app.get("/orderitem/{id}",response_model=schemas.orderItem,tags=["orderItem"])
# def get_orderitem(id:int,db:Session=Depends(get_db)):
#     db_item=db.query(models.Orderitem).filter(models.Orderitem.id==id).first()
#     if db_item is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Order Item Not Found")
#     return db_item

