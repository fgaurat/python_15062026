import streamlit as st
from pathlib import Path
from customer_dao import CustomerDAO

# streamlit run main_streamlit.py
def main():
    st.set_page_config(layout="wide")

    st.write("# Bonjour ! 👋")
    name =  st.text_input("Nom", "")
    button = st.button('Submit')
    if button and name:
        st.write(f"Bonjour {name} ")

    p = Path("db") / "customers_db.db"
    dao = CustomerDAO(p)
    all_customers = list(dao.find_all())
    st.image("chat.gif", caption="Chat")


    st.table(all_customers)



if __name__=='__main__':
    main()
