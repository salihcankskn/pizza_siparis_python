import streamlit as st
import sqlite3

st.header("Katalog")

conn= sqlite3.connect("pizzadb.sqlite3")

c=conn.cursor()

c.execute("SELECT * FROM pizzalar")
pizzalar = c.fetchall()



for pizza in pizzalar:
    col1,col2,col3 = st.columns(3)
    with col1:
        st.image(pizza[5])

    with col2:
        st.subheader(pizza[0])
        st.write(pizza[4])

    with col3:
        st.write("Küçük",pizza[1],"₺")
        st.write("Orta",pizza[2],"₺")
        st.write("Büyük",pizza[3],"₺")

