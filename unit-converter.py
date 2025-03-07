# unit Convertor
# Build a Google Unit Convertor using Python and Streamlit:

import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(45deg, #6a11cb, #2575fc);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: transform 0.3s, box-shadow 0.3s;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(0, 201, 255, 0.6);
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    .icon {
        display: inline-block;
        margin: 0 10px;
        font-size: 24px;
        color: #6a11cb;
        transition: color 0.3s;
    }
    .icon:hover {
        color: #2575fc;
    }
    /* Sidebar styling */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.3);
    }
    .css-1d391kg h1 {
        font-size: 24px;
        color: white;
        text-align: center;
    }
    .css-1d391kg p {
        font-size: 16px;
        color: white;
    }
    .sidebar-selectbox {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 20px;
    }
    .sidebar-selectbox label {
        font-size: 18px;
        color: white;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, temperature, time, and area.")

# Sidebar menu
with st.sidebar:
    st.markdown("<h1>🔧 Unit Converter</h1>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-selectbox'>", unsafe_allow_html=True)
    conversion_type = st.selectbox(
        "Select Conversion Type",
        ["Length", "Weight", "Temperature", "Time", "Area"],
        key="conversion_type",
    )
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### About")
    st.write("This app is developed by **Muhammad Hamza Khan** to help you easily convert between different units.")

# Input value
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)

# Unit options based on conversion type
col1, col2 = st.columns(2)
if conversion_type == "Length":
    units = [
        "Meters", "Kilometers", "Miles", "Feet", "Yards", "Inches",
        "Centimeters", "Millimeters", "Micrometers"
    ]
elif conversion_type == "Weight":
    units = [
        "Kilograms", "Grams", "Pounds", "Ounces", "Stones", "Tons", "Milligrams", "Micrograms"
    ]
elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
elif conversion_type == "Time":
    units = ["Seconds", "Minutes", "Hours", "Days"]
elif conversion_type == "Area":
    units = [
        "Square Meters", "Square Kilometers", "Square Miles", "Square Feet", "Square Yards",
        "Acres"
    ]

with col1:
    from_unit = st.selectbox("From", units)
with col2:
    to_unit = st.selectbox("To", units)

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Nautical Miles": 0.000539957,
        "Inches": 39.3701,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Micrometers": 1000000,
        "Nanometers": 1000000000
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
        "Stones": 0.157473,
        "Tons": 0.00110231,
        "Milligrams": 1000000,
        "Micrograms": 1000000000,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9 / 5) + 32
        else:  # Kelvin
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5 / 9
        else:  # Kelvin
            return (value - 32) * 5 / 9 + 273.15
    else:  # from Kelvin
        if to_unit == "Celsius":
            return value - 273.15
        else:  # Fahrenheit
            return (value - 273.15) * 9 / 5 + 32

def convert_time(value, from_unit, to_unit):
    time_units = {
        "Seconds": 1,
        "Minutes": 1 / 60,
        "Hours": 1 / 3600,
        "Days": 1 / 86400,
    }
    return (value / time_units[from_unit]) * time_units[to_unit]

def convert_area(value, from_unit, to_unit):
    area_units = {
        "Square Meters": 1,
        "Square Kilometers": 0.000001,
        "Square Miles": 0.000000386102,
        "Square Feet": 10.7639,
        "Square Yards": 1.19599,
        "Acres": 0.000247105,
        "Hectares": 0.0001,
    }
    return (value / area_units[from_unit]) * area_units[to_unit]

# Perform conversion
if st.button(" Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif conversion_type == "Time":
        result = convert_time(value, from_unit, to_unit)
    elif conversion_type == "Area":
        result = convert_area(value, from_unit, to_unit)

    st.success(f"The converted value is {result:.4f}")
    st.markdown(
        f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>",
        unsafe_allow_html=True,
    )

# Footer 
st.markdown(
    """
    <div class='footer'>
        Developed by Muhammad Hamza Khan😎🤖<br>
        <a href="https://github.com/MuhammadHamzaKhan786" target="_blank" class="icon"><i class="fab fa-github"></i></a>
        <a href="https://www.linkedin.com/in/muhammad-hamza-khan-6234772bb/" target="_blank" class="icon"><i class="fab fa-linkedin"></i></a>
        <a href="https://personal-portfolio-hamza.vercel.app/" target="_blank" class="icon"><i class="fas fa-globe"></i></a>
    </div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    """,
    unsafe_allow_html=True,
)