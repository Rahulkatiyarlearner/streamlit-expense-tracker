import streamlit as st
from Expenses_User_Interface.Expenses_login_page import login_page
from Expenses_User_Interface.Expenses_Main_Page import main_page


def main():
    
    if "str_usr_name" not in st.session_state:
        st.session_state["str_usr_name"] = None
        
    if st.session_state["str_usr_name"] is not None:
        main_page(st.session_state["str_usr_name"])
    else:
        login_page()


if __name__ == "__main__":
    main()