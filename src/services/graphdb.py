import neo4j


def create_customer(driver, customer):
    try:
        with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
            query = """
                    MERGE (customer:Customer {id:$id, full_name:$full_name, customer_id_value:$customer_id_value})
                    """
            result = session.run(query, id=customer[0], full_name=customer[1], customer_id_value=customer[2])
    except Exception as e:
        print(e)
        


def create_voucher(driver, voucher):
    try:
        with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
            # create voucher
            query = """
                    MERGE (voucher:Voucher {id:$id, name:$name})
                    """
            result = session.run(query, id=voucher[0], name=voucher[1])
    except Exception as e:
        print(f"create_voucher {e}")
    
        
def create_purchase_relationship(driver, purchase):
    try:
        with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
            query = """
                    MATCH (customer:Customer {id:$customer_id})
                    MATCH (voucher:Voucher {id:$voucher_id})
                    MERGE (customer)-[:PURCHASE]->(voucher)
                    """
            result = session.run(query, customer_id=purchase[0], voucher_id=purchase[1])
    except Exception as e:
        print(e)
        

def create_customer_and_voucher_relationship(driver, order):
    try:
        with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
            query = """
                    MATCH (customer:Customer {customer_id_value:$customer_id_value})
                    MATCH (voucher:Voucher {id:$voucher_id})
                    MERGE (customer)-[:PURCHASE]->(voucher)
                    """
            result = session.run(query, customer_id_value=order[2], voucher_id=order[0])
    except Exception as e:
        print(e)
    
        