import streamlit as st
import qrcode

st.title("QR Code Generator")

data = st.text_input("Enter the any data (number, text, link, etc.): ")

if st.button("Generate") and data:
    img = qrcode.make(data)
    img.save("QR Code_app.png")
    st.image("QR Code_app,png")
    st.success("The QR Code has been generated Successfully! ")