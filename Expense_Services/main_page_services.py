from datetime import datetime
from Expense_DB.expense_table_services import expense_table_services
from Expenses_User_Dictionary.expenses_user_dictionary import expenses_user_dictionary
import pandas as pd


class main_page_services:

    #entering the data
    @staticmethod
    def data_entry(user_name,data_fr_entry):
        ets = expense_table_services()
        dt = datetime.now().date()
        ets.usr_insert_table(user_name,dt,data_fr_entry[0],data_fr_entry[1],data_fr_entry[2])

    #emptying the table
    @staticmethod
    def empty_tbl(user_name):
        ets = expense_table_services()
        ets.usr_empty_table(user_name)

    #deleting the table
    def delete_tbl(user_name):
        ets = expense_table_services()
        ets.usr_delete_table(user_name)

    #get_monthly_feed
    @staticmethod
    def monthly_feed(user_name,in_month,in_year):
        ets = expense_table_services()
        return pd.DataFrame(ets.get_month_feed(user_name,in_month,str(in_year)),columns=['Date','Mjr Category','Sub Category','Amount'])

    #get remaining balance
    @staticmethod
    def remaining_balance(user_name,in_month,in_year):
        ets = expense_table_services()
        total_spent = ets.get_month_total_spend(user_name,in_month,in_year) 
        in_dict = expenses_user_dictionary._load_data()
        total_spend_final = 0 if total_spent[0] == None else total_spent[0]
        remaining_bal = int(in_dict[user_name][2]) - total_spend_final
        return in_dict[user_name][1],remaining_bal

    #get data by main categories
    @staticmethod
    def get_data_by_main_categories(user_name,in_month,in_year):
        ets = expense_table_services()
        print(in_month)
        print(type(in_month))
        new_pd = pd.DataFrame(ets.get_month_total_spend_categories(user_name,f"{in_month:02d}",str(in_year)),
                                            columns=['Category','Amount'])
        new_pd['Amount'] = pd.to_numeric(new_pd['Amount'])
        new_pd = new_pd.set_index('Category')
        return new_pd

    @staticmethod
    def update_user_limit_dict(user_name,new_limit):
        expenses_user_dictionary._update_montly_limit(user_name,new_limit)


    @staticmethod
    def del_account_json(user_name):
        expenses_user_dictionary._delete_account(user_name)





























































