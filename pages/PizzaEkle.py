import streamlit as st
import sqlite3

conn = sqlite3.connect("pizzadb.sqlite3")
c=conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS pizzalar(isim TEXT,smfiyat REAL,mdfiyat REAL,lgfiyat REAL,içindekiler TEXT,resim TEXT)")
conn.commit()



st.header("Pizza Ekle")


with st.form("pizzaekle",clear_on_submit=True):

    isim = st.text_input("Pizza İsmi")

    smfiyat = st.number_input("Küçük Fiyat")
    mdfiyat = st.number_input("Orta Fiyat")
    lgfiyat = st.number_input("Büyük Fiyat")

    içindekiler = st.multiselect("İçindekiler",["Mantar","Domates","Mısır","Zeytin","Biber","Mozerella",
                                                "Pastırma","Tavuk","Pizza Sos","Jambon","Salam","Sucuk"])

    resim = st.file_uploader("Pizza Resmi Ekle")

    ekle= st.form_submit_button("Pizza Ekle")

    if ekle:
        içindekiler = str(içindekiler)
        içindekiler = içindekiler.replace("[","")
        içindekiler = içindekiler.replace("]","")


        resimurl= "img/" + resim.name

        open(resimurl,"wb").write(resim.read())

        c.execute("INSERT INTO pizzalar VALUES(?,?,?,?,?,?)",(isim,smfiyat,mdfiyat,lgfiyat,içindekiler,resimurl))
        conn.commit()

        st.success("Pizza Ekleme Başarılı")


