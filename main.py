import streamlit as st


# Convert Units function
def convert_units(value, fromUnit,toUnit):
    conversions = {
        "Meter_Kilometer":0.001,
        "Meter_Centimeter": 100,
        "Meter_Millimeter":1000,
        "Meter_Inch":39.37,
        "Meter_Micrometer": 1e6,    
        "Meter_Meter":1,  
        "Kilometer_Meter": 1000, 
        "Kilometer_Centimeter":1e5,
        "Kilometer_Millimeter":1e6,
        "Kilometer_Inch":39370.079, 
        "Kilometer_Micrometer": 1e9,
        "Kilometer_Kilometer":1,  
    }

    # Logic to convert units
    key = f"{fromUnit}_{toUnit}"
    if key in conversions:
        conversion = conversions[key]
        return value*conversion
    else: 
        return "Conversion not Supported"



options:list[str] = []   # convert from and to units list
units:list[str] = ["Length","Mass"] #measuring units list
convertedVal=0

st.title("Unit Converter App")
measuringUnit = st.selectbox("Select measuring unit", units)


value = st.number_input("Enter the value", 1,key="from")
match(measuringUnit):    # showing from and to options based on selected measuring unit
    case "Length":
        options = ["Kilometer", "Meter", "Centimeter","Millimeter","Micrometer","Inch"]
        fromUnit= st.selectbox("Convert From", options, key="from_unit") 
        toUnit= st.selectbox( "Convert To", options, key="to_unit")
    case "Mass":
        options = ["Kilogram","Gram","Milligram","Microgram"]
        fromUnit= st.selectbox("Convert From", options, key="from_unit") 
        toUnit= st.selectbox("Convert To", options, key="to_unit") 


# convert unit button
if st.button("Convert"):
    result = convert_units(value,fromUnit,toUnit)     
    st.write(f"Value after conversion: {result}")


