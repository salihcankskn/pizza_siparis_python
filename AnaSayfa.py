import streamlit as st
import sqlite3
import pandas as pd

st.header("Ana Sayfa")


conn=sqlite3.connect("pizzadb.sqlite3")
c=conn.cursor()

c.execute("SELECT * FROM siparişler")
siparişler=c.fetchall()

df=pd.DataFrame(siparişler)

df.columns=["isim","adres","pizza","boy","icecek","toplamfiyat"]

st.table(df)