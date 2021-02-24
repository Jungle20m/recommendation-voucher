import neo4j


def create_user(driver, user):
    try:
        with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
            query = """
                    MERGE (user:User {id: $id, account_name: $account_name, age: $age})
                    """
            result = session.run(query, id=user.id, account_name=user.name, age=user.age)
    except Exception as e:
        print(e)
        

def create_voucher(driver, voucher):
    try:
        with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
            query = """
                    MERGE (user:Voucher {id: $id, voucher_name: $voucher_name})
                    """
            result = session.run(query, id=voucher.id, voucher_name=voucher.name)
    except Exception as e:
        print(e)
    
        
def create_user_voucher_relationship(driver, user_id, voucher_id):
    try:
        with driver.session(default_access_mode=neo4j.WRITE_ACCESS) as session:
            query = """
                    MATCH (user:User {id: $user_id})
                    MATCH (voucher:Voucher {id: $voucher_id})
                    MERGE (user)-[:PURCHASE]->(voucher)
                    """
            result = session.run(query, user_id=user_id, voucher_id=voucher_id)
    except Exception as e:
        print(e)