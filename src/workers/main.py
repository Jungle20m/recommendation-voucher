import neo4j
from neo4j import GraphDatabase

from src.entities.user import User
from src.entities.voucher import Voucher
from src.services import files
from src.services import graphdb


def run():
    try:
        uri = "bolt://localhost:7687"
        driver = GraphDatabase.driver(uri, auth=("neo4j", "Vietanh96"), max_connection_lifetime=1000)
        # some comment
        users = files.read_lines("/home/anhnv/Research/graphdb/voucher/src/resources/users.txt")
        vouchers = files.read_lines("/home/anhnv/Research/graphdb/voucher/src/resources/vouchers.txt")
        relationships = files.read_lines("/home/anhnv/Research/graphdb/voucher/src/resources/user_voucher_relationship.txt")
        for user_text in users:
            user = User.load_from_string(user_text)
            graphdb.create_user(driver=driver, user=user)
        
        for voucher_text in vouchers:
            voucher = Voucher.load_from_string(voucher_text)
            graphdb.create_voucher(driver=driver, voucher=voucher)
        
        for relationship_text in relationships:
            user_id, voucher_ids = relationship_text.split(" ")
            voucher_ids = voucher_ids.split(",")            
            for voucher_id in voucher_ids:
                graphdb.create_user_voucher_relationship(driver=driver, user_id=user_id, voucher_id=voucher_id)
        
        
    except Exception as e:
        print(e)