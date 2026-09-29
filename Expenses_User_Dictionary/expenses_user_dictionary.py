import os
import json

#This dictionary is accessible by all classes 

class expenses_user_dictionary:

    

    @staticmethod
    def _load_data():

        File_path  = r"Expenses_User_Dictionary\user_dictionary.json"

        if os.path.exists(File_path):
            with open(File_path,'r') as File:
                user_in_dictionary = json.load(File)
                return user_in_dictionary
        else:
            return "Issue in File"


    @staticmethod
    def _write_data(user_in_dictionary):
        File_path  = r"Expenses_User_Dictionary\user_dictionary.json"

        if os.path.exists(File_path):
            with open(File_path,'w') as File:
                user_in_dictionary = json.dump(user_in_dictionary,File,indent=4)
        else:
            return "Issue in File"

    @staticmethod
    def _update_montly_limit(user_name,in_new_limit):
        File_path  = r"Expenses_User_Dictionary\user_dictionary.json"

        
        if os.path.exists(File_path):
            #reading file
            with open(File_path,'r') as File:
                user_in_dictionary = json.load(File)
                #update data
                user_in_dictionary[user_name][2] = in_new_limit
                
            #writing again
            with open(File_path, "w") as file:
                json.dump(user_in_dictionary, file, indent=4)


    
    @staticmethod
    def _delete_account(user_name):
        File_path  = r"Expenses_User_Dictionary\user_dictionary.json"

        
        if os.path.exists(File_path):
            #reading file
            with open(File_path,'r') as File:
                user_in_dictionary = json.load(File)
                #update data
                user_in_dictionary.pop(user_name)
                
            #writing again
            with open(File_path, "w") as file:
                json.dump(user_in_dictionary, file, indent=4)




    def _enter_user(usr_name, usr_pass):
        File_path  = r"Expenses_User_Dictionary\user_dictionary.json"

        
        if os.path.exists(File_path):
            #reading file
            with open(File_path,'r') as File:
                user_in_dictionary = json.load(File)

        # Simplified dictionary lookup (in operator works directly on dicts)
        if usr_name in user_in_dictionary and user_in_dictionary[usr_name][0] == usr_pass:
            return True
        return False

   

    


    




