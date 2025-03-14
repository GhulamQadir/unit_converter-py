import streamlit as st


# Convert Units function
def convert_units(value, fromUnit,toUnit):
    conversions = {
        "Meter_Kilometer":0.001,    
        "Kilometer_Meter": 1000,    
        "Gram_kKlogram":0.001,    
        "Kilogram_Gram":1000    
    }
    key = f"{fromUnit}_{toUnit}"
    if key in conversions:
        conversion = conversions[key]
        return value*conversion
    else: 
        return "Conversion not Supported"



options:list[str] = []
units:list[str] = ["Length","Mass"]
convertedVal=0

st.title("Unit Converter App")
measuringUnit = st.selectbox("Select measuring unit", units)


col1,col2 = st.columns(2)

with col1:
    match(measuringUnit):
        case "Length":
            options = ["Kilometer", "Meter", "Centimeter","Millimeter","Micrometer","Nanometer","Mile","Yard","Foot","Inch"]
            fromUnit= st.selectbox("From", options, key="from_unit") 
            toUnit= st.selectbox( "To", options, key="to_unit")
        case "Mass":
            options = ["Kilogram","Gram","Milligram","Microgram"]
            fromUnit= st.selectbox("From", options, key="from_unit") 
            toUnit= st.selectbox("To", options, key="to_unit") 
         

with col2:
    fromUnitVal = st.number_input("Enter the value", 1,key="from")
    toUnitVal = st.empty()
    toUnitVal.text("")



convertedVal = convert_units(fromUnitVal, fromUnit, toUnit)
toUnitVal.text(convertedVal)

print(convertedVal)
