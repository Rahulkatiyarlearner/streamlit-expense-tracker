import streamlit as st  
from Expense_Services.login_page_services import login_page_Services
from Expenses_User_Interface.Expenses_Main_Page import main_page
import time

def login_page():

    st.set_page_config( 
        page_title="Login Page", 
        layout="wide" 
    )

    # st.write(st.session_state)

    ecol1, ecol2, ecol3 = st.columns([35,30,35])

    with ecol2:

        if "user_form_submit_button" in st.session_state.keys():
            if st.session_state["user_form_submit_button"]:
                in_response_add = login_page_Services.add_user(
                    st.session_state["en_username"],
                    st.session_state["en_password"],
                    st.session_state["en_fname"],
                    st.session_state["en_mlimit"]
                )
                if in_response_add == "Success":
                    st.write(f"Welcome {st.session_state["en_fname"]}")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.write(in_response_add)
                    time.sleep(2)
                    st.rerun()


        if "in_login_button" in st.session_state.keys():
            if st.session_state["in_login_button"]:
                in_login_response = login_page_Services.enter_user(
                                    st.session_state["in_username"],
                                    st.session_state["in_password"])
                if in_login_response == "Success":
                    st.session_state["str_usr_name"] = st.session_state["in_username"]
                    st.success("Login Successful")
                    st.rerun()
                else:
                    st.write(in_login_response)
                    st.session_state["str_usr_name"] = None
                    time.sleep(2)
                    st.rerun()
        

    # st.write(st.session_state)
    if "in_new_User" in st.session_state.keys():
        if st.session_state["in_new_User"]:
        
            col1 , cols2, cols3 = st.columns([20,40,40])

            with cols2:

                with st.form("new_user_form"):
                    st.text_input("Username",key="en_username",max_chars=8,
                                            placeholder="Provide UserName",
                                            help="Must be exactly 8 characters long and can only contain letters, numbers, and the special characters _, @, $, or #.")
                    st.text_input("Password",key="en_password",max_chars=8,
                                            placeholder="Provide Password",
                                            type="password",
                                            help="Must be exactly 8 characters long (any characters allowed).")
                    st.text_input("Full Name",key="en_fname",max_chars=36,
                                            placeholder="Provide Full Name",
                                            help="Must contain only letters and spaces, between 1 and 36 characters long.")
                    st.text_input("Monthly Limit",key="en_mlimit",max_chars=20,
                                            placeholder="Provide Monthly Expenses Limit",
                                            help="Must be a positive number with up to 2 decimal places (e.g., 100 or 99.99).")
                    st.form_submit_button("Click to Add yourself",key="user_form_submit_button")


    else:

        col1 , cols2, cols3 = st.columns([50,10,25])

        with cols3:

            with st.form("login_form"):
                st.text_input("Username",key="in_username",max_chars=8,
                                        placeholder="Type UserName")
                st.text_input("Password",key="in_password",max_chars=8,
                                        placeholder="Type Password",
                                        type="password")
                st.form_submit_button("Login",key="in_login_button")


            st.space(20)
            
            cols11, cols12, cols13 = st.columns([30,20,50])

            with cols13:
                st.button("New User? click here",key="in_new_User")

