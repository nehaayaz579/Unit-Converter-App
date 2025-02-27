import streamlit as st

# Updated Conversion factors with new categories
conversion_factors = {
    "Length": {
        "meters": 1,
        "kilometers": 1000,
        "miles": 1609.34,
        "feet": 0.3048,
        "inches": 0.0254,
        "nautical mile": 1852,
        "yard": 0.9144,
        "nanometer": 1e-9,
        "micrometer": 1e-6,
        "millimeter": 0.001,
        "centimeter": 0.01
    },
    "Weight": {
        "kilograms": 1,
        "grams": 1000,
        "pounds": 2.20462,
        "ounces": 35.274
    },
    "Temperature": {
        "Celsius": "lambda x: x",
        "Fahrenheit": "lambda x: (x - 32) * 5/9",
        "Kelvin": "lambda x: x - 273.15"
    },
    "Area": {
        "square meters": 1,
        "square kilometers": 1e6,
        "square yard": 0.83612736,
        "square miles": 2.58999e6,
        "square feet": 0.092903,
        "square inches": 0.00064516,
        "hectares": 1e4,
        "acres": 4046.86
    },
    "Data Transfer Rate": {
        "bits per second": 1,
        "kilobits per second": 1000,
        "kilobyte per second": 8000,
        "kibibit per second": 1024,
        "megabits per second": 1e6,
        "megabyte per second": 8e6,
        "mebibit per second": 1048576,
        "gigabits per second": 1e9,
        "gigabyte per second": 8e9,
        "gibibit per second": 1073741824,
        "terabits per second": 1e12,
        "terabyte per second": 8e12,
        "tebibit per second": 1099511627776,
        "bytes per second": 8,
        "kilobytes per second": 8000,
        "megabytes per second": 8e6
    },
    "Digital Storage": {
        "bit": 1,
        "kilobit": 1000,
        "kibibit": 1024,
        "megabit": 1e6,
        "mebibit": 1048576,
        "gigabit": 1e9,
        "gibibit": 1073741824,
        "terabit": 1e12,
        "tebibit": 1099511627776,
        "petabit": 1e15,
        "pebibit": 1125899906842624,
        "bytes": 1,
        "kilobytes": 1024,
        "kibibyte": 1024,
        "megabytes": 1024**2,
        "mebibyte": 1024**2,
        "gigabytes": 1024**3,
        "gibibyte": 1024**3,
        "terabytes": 1024**4,
        "tebibyte": 1024**4,
        "petabytes": 1024**5,
        "pebibyte": 1024**5
    },
    "Energy": {
        "joules": 1,
        "kilojoules": 1000,
        "calories": 4.184,
        "kilocalories": 4184,
        "watt-hours": 3600,
        "kilowatt-hours": 3.6e6,
        "electronvolts": 1.60218e-19,
        "british thermal unit": 1055.06,
        "US therm": 1.05506e5,
        "foot-pound": 1.35582
    },
    "Frequency": {
        "hertz": 1,
        "kilohertz": 1e3,
        "megahertz": 1e6,
        "gigahertz": 1e9
    },
    "Fuel Economy": {
        "liters per 100 kilometers": 1,
        "miles per gallon (US)": 235.214,
        "miles per gallon (UK)": 282.481,
        "kilometers per liter": 100
    },
    "Mass": {
        "kilograms": 1,
        "grams": 1000,
        "milligram": 1e3,
        "microgram": 1e6,
        "imperial ton": 1016.05,
        "US ton": 907.184,
        "stone": 6.35029,
        "pounds": 2.20462,
        "ounces": 35.274
    },
    "Plane Angle": {
        "arcsecond": 4.84814e-6,
        "radians": 1,
        "degrees": 57.2958,
        "gradians": 63.66198,
        "milliradian": 1e-3,
        "minute of arc": 1/60
    },
    "Pressure": {
        "pascals": 1,
        "kilopascals": 1000,
        "bars": 100000,
        "atmospheres": 101325,
        "mmHg": 133.322,
        "pound per square inch": 6894.76,
        "torr": 133.322
    },
    "Speed": {
        "meters per second": 1,
        "kilometers per hour": 0.277778,
        "miles per hour": 0.44704,
        "feet per second": 0.3048,
        "knots": 0.514444
    },
    "Time": {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400,
        "weeks": 604800,
        "months": 2628000,
        "years": 31536000,
        "decade": 315360000,
        "century": 3153600000
    },
    "Volume":  {
        "Liter": 0.0353,
        "Cubic Meter": 35.3147,
        "Cubic Foot": 1,
        "Imperial Gallon": 6.22884,
        "Imperial Quart": 1.55721,
        "Imperial Pint": 0.778605,
        "Imperial Cup": 0.389302,
         "Imperial Fluid Ounce": 0.034632,
         "Imperial Tablespoon": 0.021645,
         "Imperial Teaspoon": 0.007215,
        "US Liquid Gallon": 7.48052,
        "US Liquid Quart": 1.87013,
        "US Liquid Pint": 0.935013,
        "US Legal Cup": 0.422675,
        "US Fluid Ounce": 0.0295735,
        "US Tablespoon": 0.0147868,
        "US Teaspoon": 0.00492892,
        "Cubic Inches": 1.63871e-5,
        "Cubic Feet": 0.0283168
}
}
# Function to convert units
def convert_units(value, from_unit, to_unit, category):
    if category in ['Length', 'Weight', 'Area', 'Data Transfer Rate', 'Digital Storage', 'Energy', 'Frequency', 'Fuel Economy', 'Mass', 'Pressure', 'Speed', 'Volume']:
        value_in_base = value * conversion_factors[category][from_unit]
        converted_value = value_in_base / conversion_factors[category][to_unit]
    elif category == 'Temperature':
        if from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                converted_value = (value * 9/5) + 32
            elif to_unit == 'Kelvin':
                converted_value = value + 273.15
            else:
                converted_value = value
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                converted_value = (value - 32) * 5/9
            elif to_unit == 'Kelvin':
                converted_value = (value - 32) * 5/9 + 273.15
            else:
                converted_value = value
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                converted_value = value - 273.15
            elif to_unit == 'Fahrenheit':
                converted_value = (value - 273.15) * 9/5 + 32
            else:
                converted_value = value
    return converted_value

# Streamlit interface
st.title("🔄Unit Converter")

# User inputs
category = st.selectbox("Select Category", list(conversion_factors.keys()))
value = st.number_input("Enter value", min_value=0.0)
from_unit = st.selectbox("From unit", list(conversion_factors[category].keys()))
to_unit = st.selectbox("To unit", list(conversion_factors[category].keys()))

# Convert and display result
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}.")
