import streamlit as st

st.title("Unit Converter App")


col1,col2 = st.columns(2)

with col1:
   fromUnit= st.selectbox(
    "From",
    ("Kilometre", "Metre", "Centimetre","Millimetre","Micrometre","Nanometre","Mile","Yard","Foot","Inch"),
)
   toUnit= st.selectbox(
    "To",
    ("Metre", "Kilometre", "Centimetre","Millimetre","Micrometre","Nanometre","Mile","Yard","Foot","Inch"),
)
    


with col2:
    fromUnitVal = st.number_input("Enter the value", 1,key="from")
    toUnitVal = st.number_input("Enter the value",1000,key="to")
