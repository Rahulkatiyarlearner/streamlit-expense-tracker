from Expense_Services.validation_services import validation_services
from Expenses_User_Dictionary.expenses_user_dictionary import expenses_user_dictionary
from Expense_DB.expense_table_services import expense_table_services


class login_page_Services:

    @staticmethod
    def add_user(usr_name,usr_pass,usr_mname,usr_mlimit):
        usr_name_validate = validation_services._in_user_name_validation(usr_name)
        usr_pass_validate = validation_services._in_password_validation(usr_pass)
        usr_mname_validate = validation_services._in_name_validation(usr_mname)
        usr_mlimit_validate = validation_services._in_amount_validation(usr_mlimit)
        if usr_name_validate == "Success" and usr_pass_validate == "Success" and \
            usr_mname_validate == "Success" and usr_mlimit_validate == "Success"   :
            get_dictionary = expenses_user_dictionary._load_data()
            if usr_name in get_dictionary.keys():
                return f"{usr_name} Already available. Please enter another one"               
            else:
                get_dictionary[usr_name] = [usr_pass,usr_mname,usr_mlimit]
                expenses_user_dictionary._write_data(get_dictionary)
                exp_tb = expense_table_services()
                exp_tb.usr_create_table(usr_name)
                return f"{usr_name} added. Please login to continue"
        else:
            if usr_name_validate == "Failure":
                return "Provide UserName in Correct Format"
            elif usr_pass_validate == "Failure":
                return "Provide Password in Correct Format"
            elif usr_mname_validate == "Failure":
                return "Provide Name in Correct Format"
            elif usr_mlimit_validate == "Failure":
                return "Provide Amount in Correct Format"

    @staticmethod
    def enter_user(usr_name,usr_pass):
        usr_name_validate = validation_services._in_user_name_validation(usr_name)
        usr_pass_validate = validation_services._in_password_validation(usr_pass)
        if usr_name_validate == "Success" and usr_pass_validate == "Success":
            get_dictionary = expenses_user_dictionary._load_data()
            login_suc = expenses_user_dictionary._enter_user(usr_name,usr_pass)
            if login_suc:
                return "Success"             
            else:
                if usr_name not in get_dictionary.keys():
                    return "Incorrect Username"
                else:
                    return "Incorrect Password"
        else:
            if usr_name_validate == "Failure":
                return "Provide UserName in Correct Format"
            elif usr_pass_validate == "Failure":
                return "Provide Password in Correct Format"
            






    



    

