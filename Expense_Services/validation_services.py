import re


class validation_services:

    @staticmethod
    def _in_user_name_validation(in_user_name):
        re_user_name_pattern = r"^[A-Za-z0-9_@$#]{8}$"
        if re.match(re_user_name_pattern,in_user_name):
            return "Success"
        else:
            return "Failure"


    @staticmethod
    def _in_name_validation(in_name):
        re_name_pattern = r"^[A-Za-z\s]{1,36}$"
        if re.match(re_name_pattern,in_name):
            return "Success"
        else:
            return "Failure"

    @staticmethod
    def _in_password_validation(in_password):
        re_pass_pattern = r"^.{8}$"
        if re.match(re_pass_pattern,in_password):
            return "Success"
        else:
            return "Failure"
 
        
    @staticmethod
    def _in_amount_validation(in_amount):
        re_amount_pattern = r"^\d+(\.\d{1,2})?$"
        if re.match(re_amount_pattern,str(in_amount)):
            return "Success"
        else:
            return "Failure"


