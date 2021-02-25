from src.database.database import engine



class CRUDGup2Customer():
    @staticmethod
    def get_records():
        try:
            with engine.connect() as connection:
                query = """
                        SELECT id, full_name, customer_id_value
                        FROM gup2_customer
                        WHERE full_name IS NOT NULL AND customer_id_value IS NOT NULL AND full_name != ''
                        """
                records = connection.execute(query)
                return records
        except Exception as e:
            print(e)
            return []
        
    @staticmethod
    def get_oders():
        try:
            with engine.connect() as connection:
                query = """
                        SELECT B.id as voucher_id, B.name as voucher_name, D.customer_id_value 
                        FROM healthnet.gup2_product_voucher_item A 
                        JOIN healthnet.gup2_product B on A.product_voucher_id = B.id 
                        JOIN healthnet.gup2_merchant_layer_2 C on B.brand_id = C.id  
                        JOIN healthnet.gup2_customer D on D.customer_worker_site_id = A.buyer_site_id AND D.customer_id_value IS NOT NULL
                        WHERE A.buyer_site_id IS NOT NULL 
                        """
                records = connection.execute(query)
                return records
        except Exception as e:
            print(e)
            return []