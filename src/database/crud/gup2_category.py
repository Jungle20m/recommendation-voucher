from src.database.database import engine



class CRUDGup2Category():
    
    @staticmethod
    def get_records():
        try:
            with engine.connect() as connection:
                query = """
                        SELECT id, category_code, category_name
                        FROM gup2_category
                        WHERE category_code IS NOT NULL and category_name IS NOT NULL
                        """
                records = connection.execute(query)
                return records
        except Exception as e:
            print(e)
            return []