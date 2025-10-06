import streamlit as st

st.set_page_config(page_title="Label Generator")

st.title("Label Generator")

name = st.text_input("Enter your name or text")
color = st.color_picker("Choose a color", "#ff0000")
size = st.slider("Select label size (mm)", 10, 100, 50)

if st.button("Generate Label"):
    st.markdown(f"<div style='background-color:{color}; padding:10px; width:{size*3}px; text-align:center; border-radius:5px;'>"
                f"<h2 style='color:white;'>{name}</h2></div>", unsafe_allow_html=True)
