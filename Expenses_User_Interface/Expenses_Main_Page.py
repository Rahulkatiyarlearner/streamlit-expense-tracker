import streamlit as st
from Expense_Services.main_page_services import main_page_services
from datetime import datetime
from Expenses_User_Interface.Expenses_cat_subcat import categories
from time import time





def main_page(in_user_name):

    st.set_page_config( 
        page_title="Main Page", 
        layout="wide" 
    )

    col1, col2, col3 = st.columns([20,5,75])

    with col1:
        st.space(10)
        st.button("Main Screen",                key="bt_ms", width=500)
        st.space(10)
        st.button("Track Expense",              key="bt_te", width=500)
        st.space(10)
        st.button("Monthly Report",             key="bt_mr",width=500)
        st.space(10)
        st.button("Update Monthly Limit",       key="bt_uml",width=500)
        st.space(10)
        st.button("Clear All Data",             key="bt_cad",width=500)
        st.space(10)
        st.button("Delete Account",             key="bt_da",width=500)

    with col3:

        col31,col32 = st.columns([70,30])

        with col31:


## see spending for Month
            if "bt_te" in st.session_state.keys():
                if st.session_state["bt_te"] == True:
                    years_descending = [year for year in range(datetime.now().year, 2009, -1)]
                    months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
                    with st.form(key="in_date_data_form"):
                        cols_in1, cols_in2, cols_in3 = st.columns([33,33,33])
                        with cols_in1:
                            st.selectbox("Select Year",years_descending,key="te_in_yr")
                        with cols_in2:
                            st.selectbox("Select Month",months,
                                                    key="te_in_mt",index=datetime.now().month - 1)
                        with cols_in3:  
                            st.space(10)                  
                            st.form_submit_button("Check Month",key="te_cm_bt",use_container_width=True)
                    in_month_data = main_page_services.monthly_feed(in_user_name,
                                                                    st.session_state["te_in_mt"],
                                                                    st.session_state["te_in_yr"])
                    st.write(in_month_data)
                    


            if "te_cm_bt" in st.session_state.keys():
                if st.session_state["te_cm_bt"] == True:
                    years_descending = [year for year in range(datetime.now().year, 2009, -1)]
                    months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
                    with st.form(key="in_date_data_form"):
                        cols_in1, cols_in2, cols_in3 = st.columns([33,33,33])
                        with cols_in1:
                            st.selectbox("Select Year",years_descending,key="te_in_yr")
                        with cols_in2:
                            st.selectbox("Select Month",months,
                                                    key="te_in_mt",index=datetime.now().month - 1)
                        with cols_in3: 
                            st.space(10)                     
                            st.form_submit_button("Check Month",key="te_cm_bt",use_container_width=True)
                    in_month_data = main_page_services.monthly_feed(in_user_name,
                                                                    st.session_state["te_in_mt"],
                                                                    st.session_state["te_in_yr"])
                    st.write(in_month_data)

#to show report start here

            if "bt_mr" in st.session_state.keys():
                if st.session_state["bt_mr"] == True:
                    in_m_feed = main_page_services.get_data_by_main_categories(in_user_name,
                                                                datetime.now().month,
                                                                datetime.now().year)
                    st.bar_chart(in_m_feed)
                    st.subheader("Compare with Other Month")
                    years_descending = [year for year in range(datetime.now().year, 2009, -1)]
                    months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
                    with st.form(key="in_date_data_form_comp"):
                        cols_in1, cols_in2, cols_in3 = st.columns([33,33,33])
                        with cols_in1:
                            st.selectbox("Select Year",years_descending,key="te_in_yr_c")
                        with cols_in2:
                            st.selectbox("Select Month",months,
                                                    key="te_in_mt_c",index=datetime.now().month - 1)
                        with cols_in3: 
                            st.space(10)                     
                            st.form_submit_button("Check Month",key="te_cm_bt_c",use_container_width=True)
                    

                  
            if "te_cm_bt_c" in st.session_state.keys():
                if st.session_state["te_cm_bt_c"] == True:
                    in_m_feed = main_page_services.get_data_by_main_categories(in_user_name,
                                                                datetime.now().month,
                                                                datetime.now().year)
                    st.bar_chart(in_m_feed)
                    st.subheader("Compare with Other Month")
                    years_descending = [year for year in range(datetime.now().year, 2009, -1)]
                    months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
                    with st.form(key="in_date_data_form_comp"):
                        cols_in1, cols_in2, cols_in3 = st.columns([33,33,33])
                        with cols_in1:
                            st.selectbox("Select Year",years_descending,key="te_in_yr_c")
                        with cols_in2:
                            st.selectbox("Select Month",months,
                                                    key="te_in_mt_c",index=datetime.now().month - 1)
                        with cols_in3: 
                            st.space(10)                     
                            st.form_submit_button("Check Month",key="te_cm_bt_c",use_container_width=True)
                    
                    in_month_data_df = main_page_services.get_data_by_main_categories(in_user_name,
                                                                    int(st.session_state["te_in_mt_c"]),
                                                                    st.session_state["te_in_yr_c"])

                    st.bar_chart(in_month_data_df)


#add update monthly Limit


            if "up_lim_bt" in st.session_state.keys():
                if st.session_state["up_lim_bt"] == True:
                    main_page_services.update_user_limit_dict(in_user_name,st.session_state["new_lt"])
                    st.success(f"For {in_user_name}, New Limit Updated to {st.session_state["new_lt"]}")
                    with st.form(key="update_user_limit"):
                        st.text_input("Please enter the new Limit",key="new_lt",
                               placeholder="Provide new limit here",
                               help="Must be a positive number with up to 2 decimal places (e.g., 100 or 99.99).")
                        st.form_submit_button("Click Here to Update Limit", key="up_lim_bt")



            if "bt_uml" in st.session_state.keys():
                if st.session_state["bt_uml"] == True:
                    with st.form(key="update_user_limit"):
                        st.text_input("Please enter the new Limit",key="new_lt",
                               placeholder="Provide new limit here",
                               help="Must be a positive number with up to 2 decimal places (e.g., 100 or 99.99).")
                        st.form_submit_button("Click Here to Update Limit", key="up_lim_bt")


## clearing the data
            if "clr_dt" in st.session_state.keys():
                if st.session_state["clr_dt"] == True:
                    main_page_services.empty_tbl(in_user_name)
                    st.success("All Data Delete")
                    st.write("Please made new Entries")

            if "bt_cad" in st.session_state.keys():
                if st.session_state["bt_cad"] == True:
                    st.button("Press Here to Clear all Data!!",key="clr_dt")


#delete account
            if "clr_act" in st.session_state.keys():
                if st.session_state["clr_act"] == True:
                    main_page_services.delete_tbl(in_user_name)
                    main_page_services.del_account_json(in_user_name)
                    st.session_state["str_usr_name"] = None
                    st.rerun()

            if "bt_da" in st.session_state.keys():
                if st.session_state["bt_da"] == True:

                    st.button("Beware click Here !! it will delete your account",key="clr_act")

### main add spend

            if ("bt_ms" in st.session_state.keys() and st.session_state["bt_ms"] == True) or "main_cat" in st.session_state.keys():
                st.session_state["bt_ms_new"] = True  
            else:
                st.session_state["bt_ms_new"] = False

            if (("bt_ms" in st.session_state.keys() and st.session_state["bt_ms"] == False) and "main_cat" not in st.session_state.keys()) or \
            ("bt_te" in st.session_state.keys() and st.session_state["bt_te"] == True) or \
            ("bt_mr" in st.session_state.keys() and st.session_state["bt_mr"] == True) or \
            ("bt_uml" in st.session_state.keys() and st.session_state["bt_uml"] == True) or \
            ("bt_cad" in st.session_state.keys() and st.session_state["bt_cad"] == True) or \
            ("bt_da" in st.session_state.keys() and st.session_state["bt_da"] == True):
                st.session_state["bt_ms_new"] = False
            else:
                st.session_state["bt_ms_new"] = True

            if st.session_state["bt_ms"] == False and "te_cm_bt" not in st.session_state.keys() and \
               st.session_state["bt_te"] == False and "te_cm_bt_c" not in st.session_state.keys() and \
               st.session_state["bt_mr"] == False and "up_lim_bt" not in st.session_state.keys() and \
               st.session_state["bt_uml"] == False and "clr_dt" not in st.session_state.keys() and \
               st.session_state["bt_cad"] == False and "clr_act" not in st.session_state.keys() and \
               st.session_state["bt_da"] == False:
                    st.session_state["bt_ms_new"] = True

            
            if "bt_ms_new" in st.session_state.keys():
                if st.session_state["bt_ms_new"] == True:
                    st.selectbox("Select Main Categories",list(categories.keys()),key="main_cat")
                    st.selectbox("Select Sub Categories",list(categories[st.session_state["main_cat"]]),
                                                            key="sub_cat")
                    st.session_state["bt_ms_new"] = False 
                    with st.form("add_to_spend"):
                        
                        st.text_input("Please enter the amount",max_chars=20,key="mtly_spnd",
                                    placeholder="Provide Amount Here",
                                    help="Must be a positive number with up to 2 decimal places (e.g., 100 or 99.99).")
                        st.form_submit_button("Add Spending",key="add_spending")


            if "add_spending" in st.session_state.keys() :
                if st.session_state["add_spending"] == True:
                    
                    out_data_entry_list = (st.session_state["main_cat"],st.session_state["sub_cat"],st.session_state["mtly_spnd"])
                    in_add_spending_response = main_page_services.data_entry(
                                            in_user_name,out_data_entry_list)
                    st.session_state.pop("main_cat")
                    st.success("Spending added Successfully")     

################################ - side columns - #######################################

        if "user_logout" in st.session_state.keys():
            if st.session_state["user_logout"]:
                st.session_state["str_usr_name"] = None
                st.rerun()
        
        
        with col32:
            dt = datetime.now().date()
            in_name, in_remaining_balance = main_page_services.remaining_balance(in_user_name,
                                                                                dt.strftime("%m"),
                                                                                dt.strftime("%Y"))
            st.text(f"USERNAME : {in_user_name}",text_alignment="right")
            st.text(f"NAME : {in_name}",text_alignment="right")
            st.text(f"REMAINING MONTHLY : {in_remaining_balance}",text_alignment="right")
            st.button("Logout",key="user_logout")


