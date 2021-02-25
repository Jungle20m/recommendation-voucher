from src.database.database import engine



class CRUDGup2Product():
    
    @staticmethod
    def get_records():
        try:
            with engine.connect() as connection:
                query = """
                        SELECT id, name, category_id
                        FROM gup2_product
                        WHERE name IS NOT NULL AND name != ''
                        """
                records = connection.execute(query)
                return records
        except Exception as e:
            print(e)
            return []