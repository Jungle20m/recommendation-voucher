import neo4j
from neo4j import GraphDatabase

from src.entities.user import User
from src.entities.voucher import Voucher
from src.services import files
from src.services import graphdb
from src.database.crud.gup2_customer import CRUDGup2Customer
from src.database.crud.gup2_product import CRUDGup2Product
from src.database.crud.gup2_category import CRUDGup2Category


def run():
    try:
        uri = "bolt://localhost:7687"
        driver = GraphDatabase.driver(uri, auth=("neo4j", "Vietanh96"), max_connection_lifetime=1000)
        # some comment
        customers = files.load_csv("/home/anhnv/Research/graphdb/voucher/src/resources/customer.csv")
        vouchers = files.load_csv("/home/anhnv/Research/graphdb/voucher/src/resources/voucher.csv")
        purchase = files.load_csv("/home/anhnv/Research/graphdb/voucher/src/resources/purchase.csv")
                    
        for customer in customers:
            graphdb.create_customer(driver=driver, customer=customer)
    
        for voucher in vouchers:
            graphdb.create_voucher(driver=driver, voucher=voucher)
    
        for purchase_relationship in purchase:
            graphdb.create_purchase_relationship(driver=driver, purchase=purchase_relationship)
    
    except Exception as e:
        print(e)




# def run():
#     try:
#         uri = "bolt://localhost:7687"
#         driver = GraphDatabase.driver(uri, auth=("neo4j", "Vietanh96"), max_connection_lifetime=1000)
#         # some comment
#         # customers = CRUDGup2Customer.get_records()
        
#         # vouchers = CRUDGup2Product.get_records()
        
#         # categories = CRUDGup2Category.get_records()
        
#         # orders = CRUDGup2Customer.get_oders()
        
#         # create category
#         # for category in categories:
#         #     graphdb.create_category(driver=driver, category=category)
        
#         # create voucher    
#         # for voucher in vouchers:
#         #     graphdb.create_voucher(driver=driver, voucher=voucher)
        
#         # # create customer
#         # for customer in customers:
#         #     graphdb.create_customer(driver=driver, customer=customer)
        
#         # # create relationship customer and voucher    
#         # for order in orders:
#         #     graphdb.create_customer_and_voucher_relationship(driver=driver, order=order)
            
#     except Exception as e:
#         print(e)