import streamlit as st

st.set_page_config(page_title="🔁 Unit Converter", layout="centered")
st.title("🔁 Simple Unit Converter")
st.write("Convert units of length, weight, and temperature easily!")

# Choose category
category = st.selectbox("Choose a category:", ["Length", "Weight", "Temperature"])

# Length Conversion
if category == "Length":
    units = {"Meters": 1, "Kilometers": 1000, "Feet": 0.3048, "Miles": 1609.34}
    from_unit = st.selectbox("From:", list(units.keys()), key="len_from")
    to_unit = st.selectbox("To:", list(units.keys()), key="len_to")
    value = st.number_input("Enter value:", key="len_value")
    
    if st.button("Convert Length"):
        result = value * units[from_unit] / units[to_unit]
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

# Weight Conversion
elif category == "Weight":
    units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592}
    from_unit = st.selectbox("From:", list(units.keys()), key="wt_from")
    to_unit = st.selectbox("To:", list(units.keys()), key="wt_to")
    value = st.number_input("Enter value:", key="wt_value")
    
    if st.button("Convert Weight"):
        result = value * units[from_unit] / units[to_unit]
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

# Temperature Conversion
elif category == "Temperature":
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_from")
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_to")
    value = st.number_input("Enter value:", key="temp_value")
    
    def convert_temperature(value, from_u, to_u):
        if from_u == to_u:
            return value
        # Convert to Celsius first
        if from_u == "Fahrenheit":
            value = (value - 32) * 5/9
        elif from_u == "Kelvin":
            value = value - 273.15
        # Now convert from Celsius to target
        if to_u == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_u == "Kelvin":
            return value + 273.15
        return value
    
    if st.button("Convert Temperature"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
