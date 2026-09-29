from Expense_DB.expense_database_manager import expense_database_manager

class expense_table_services:

    def __init__(self):
        self.db = expense_database_manager("expenses_tables.db")

    #creating table
    def usr_create_table(self,user_name):
        in_table_name = f"{user_name}_table"
     
    
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            CREATE TABLE if not exists {in_table_name}(
            date_tb                DATE,
            categories_tb          CHAR(40) NOT NULL,
            sub_categories_tb      CHAR(40) NOT NULL,
            spend_tb               DOUBLE   NOT NULL
            )
            """)


    #delete table 
    def usr_delete_table(self,user_name):
        in_table_name = f"{user_name}_table"

        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            DROP TABLE IF EXISTS {in_table_name}
            """)


    #insert table
    def usr_insert_table(self,user_name,in_date,in_cat,in_sub_cat,in_spend):
        in_table_name = f"{user_name}_table"

        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            INSERT INTO {in_table_name}
            (date_tb,categories_tb,sub_categories_tb,spend_tb)
            VALUES
            (?,?,?,?)
            """,(in_date,in_cat,in_sub_cat,in_spend))

    #empty table
    def usr_empty_table(self,user_name):
        in_table_name = f"{user_name}_table"


        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            DELETE FROM {in_table_name}
            """)


    #getting data for this Month
    def get_month_feed(self,user_name,in_month,in_year):
        in_table_name = f"{user_name}_table"

        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            SELECT * FROM {in_table_name}
            WHERE strftime('%m', date_tb) = ?
              AND strftime('%Y', date_tb) = ?
            """,(in_month,in_year))
            return cursor.fetchall()


    #get monthly spend till date
    def get_month_total_spend(self,user_name,in_month,in_year):
        in_table_name = f"{user_name}_table"


        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            SELECT SUM(spend_tb) FROM {in_table_name}
            WHERE strftime('%m', date_tb) = ?
              AND strftime('%Y', date_tb) = ?
            """,(in_month,in_year))
            return cursor.fetchone()

    
    #get total_sum by main
    def get_month_total_spend_categories(self,user_name,in_month,in_year):
        in_table_name = f"{user_name}_table"


        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            SELECT categories_tb,SUM(spend_tb) FROM {in_table_name}            
            WHERE strftime('%m', date_tb) = ?
              AND strftime('%Y', date_tb) = ?
              GROUP BY(categories_tb)
            """,(in_month,in_year))
            return cursor.fetchall()








