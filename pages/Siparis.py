import streamlit as st
import sqlite3

conn= sqlite3.connect("pizzadb.sqlite3")

c=conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS siparişler(isim TEXT,adres TEXT,pizza TEXT,boy TEXT,içecek TEXT,fiyat REAL)")

c.execute("SELECT isim FROM pizzalar")
isimler = c.fetchall()

isimlerlist=[]
for i in isimler:
    isimlerlist.append(i[0])






st.header("Sipariş")


with st.form("sipariş",clear_on_submit=True):
    isim= st.text_input("İsim Soyisim")
    adres = st.text_area("Adres")
    pizza = st.selectbox("Pizza Seç",isimlerlist)
    boy = st.selectbox("Boy",["Küçük","Orta","Büyük"])
    icecek = st.selectbox("İçecek",["Kola","Fanta","Ayran","Su","Soda","Ice Tea"])
    siparişver = st.form_submit_button("Sipariş Ver")

    if siparişver:
        if boy == "Küçük":
            c.execute("SELECT smfiyat FROM pizzalar WHERE isim=?",(pizza,))
            fiyat = c.fetchone()

        elif boy == "Orta":
            c.execute("SELECT mdfiyat FROM pizzalar WHERE isim=?", (pizza,))
            fiyat = c.fetchone()

        elif boy == "Büyük":
            c.execute("SELECT lgfiyat FROM pizzalar WHERE isim=?", (pizza,))
            fiyat = c.fetchone()


    içecekler={
        "Kola": 30,
        "Fanta":30,
        "Ayran":20,
        "Su":10,
        "Ice Tea":30,
        "Soda":20
    }

    icecekfiyat = içecekler[icecek]

    toplamfiyat = fiyat[0]+icecekfiyat


    c.execute("INSERT INTO siparişler VALUES(?,?,?,?,?,?)",(isim,adres,pizza,boy,icecek,toplamfiyat))
    conn.commit()

    st.success(f"Sipariş Başarılı Bir Şekilde Gerçekleşti Toplam Ücret {toplamfiyat} ₺")