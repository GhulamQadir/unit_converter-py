import streamlit as st
import random

# Convert Units function
def convert_units(value, fromUnit,toUnit):
    conversions = {
        "Meter_Kilometer":0.001,
        "Meter_Centimeter": 100,
        "Meter_Millimeter":1000,
        "Meter_Inch":39.37,
        "Meter_Micrometer": 1e6,    
        "Kilometer_Meter": 1000, 
        "Kilometer_Centimeter":1e5,
        "Kilometer_Millimeter":1e6,
        "Kilometer_Inch":39370.079, 
        "Kilometer_Micrometer": 1e9,
        "Centimeter_Kilometer":1e-5,
        "Centimeter_Meter":0.01,
        "Centimeter_Millimeter":10,
        "Centimeter_Micrometer":10000,
        "Centimeter_Inch":0.393701,
        "Millimeter_Kilometer":1e-6,
        "Millimeter_Meter":0.001,
        "Millimeter_Centimeter":0.1,
        "Millimeter_Micrometer":1000,
        "Millimeter_Inch":0.0393701,
        "Micrometer_Kilometer":1e-9,
        "Micrometer_Meter":1e-6,
        "Micrometer_Centimeter":1e-4,
        "Micrometer_Millimeter":0.001,
        "Micrometer_Inch":3.937e-5,
        "Inch_Kilometer":2.54e-5,
        "Inch_Meter":0.0254,
        "Inch_Centimeter":2.54,
        "Inch_Millimeter":25.4,
        "Inch_Micrometer":25400,
        "Kilogram_Gram":1000,
        "Kilogram_Milligram":1e6,
        "Kilogram_Microgram":1e9,
        "Kilogram_Pound":2.20462,
        "Gram_Kilogram":0.001,
        "Gram_Milligram":1000,
        "Gram_Microgram":1e6,
        "Gram_Pound":0.00220462,
        "Milligram_Kilogram":1e-6,
        "Milligram_Gram":0.001,
        "Milligram_Microgram":1000,
        "Milligram_Pound":2.2046e-6,
        "Microgram_Kilogram":1e-9,
        "Microgram_Gram":1e-6,
        "Microgram_Milligram":0.001,
        "Microgram_Pound":2.2046e-9,
        "Pound_Kilogram":0.453592,
        "Pound_Gram":453.592,
        "Pound_Milligram":453592,
        "Pound_Microgram":4.536e8,
    }

    # Logic to convert units
    key = f"{fromUnit}_{toUnit}"
    if key in conversions:
        conversion = conversions[key]
        return value*conversion
    elif fromUnit==toUnit:
        return value*1
    else:         
        return "Conversion not Supported"



options:list[str] = []   # convert from and to units list
units:list[str] = ["Length","Mass"] #measuring units list
convertedVal=0

st.title("Unit Converter App")
measuringUnit = st.selectbox("Select measuring unit", units)

# numerical value to convert
value = st.number_input("Enter the value", min_value=1.0, step=1.0)

match(measuringUnit):    # showing from and to options based on selected measuring unit
    case "Length":
        options = ["Kilometer", "Meter", "Centimeter","Millimeter","Micrometer","Inch"]
        fromUnit= st.selectbox("Convert From", options, key="from_unit") 
        toUnit= st.selectbox( "Convert To", options, key="to_unit")
    case "Mass":
        options = ["Kilogram","Gram","Milligram","Microgram","Pound"]
        fromUnit= st.selectbox("Convert From", options, key="from_unit") 
        toUnit= st.selectbox("Convert To", options, key="to_unit") 


# convert unit button
if st.button("Convert"):
    result = convert_units(value,fromUnit,toUnit)     
    st.write(f"Value after conversion: {result}")


