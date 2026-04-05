import streamlit as st
import re
from datetime import datetime

# Initialize session state
if "calc_history" not in st.session_state:
    st.session_state.calc_history = []

# Theme options
THEMES = ["material_light", "material_dark", "cyberpunk"]

def apply_theme(theme):
    if theme == "material_light":
        st.set_page_config(page_title="Material Calculator", layout="centered", bg_color="#ffffff", text_color="#000000")
        st.set_sidebar_color("#ffffff")
        st.set_sidebar_bg_color("#000000")
    elif theme == "material_dark":
        st.set_page_config(page_title="Material Calculator", layout="centered", bg_color="#121212", text_color="#ffffff")
        st.set_sidebar_color("#121212")
        st.set_sidebar_bg_color("#ffffff")
    elif theme == "cyberpunk":
        st.set_page_config(page_title="Cyberpunk Calculator", layout="centered", bg_color="#0d002b", text_color="#00ffff")
        st.set_sidebar_color("#0d002b")
        st.set_sidebar_bg_color="#ff00ff")

@st.cache_data
def calculate(value1, value2, operator):
    try:
        val1 = float(value1)
        val2 = float(value2)
        if operator == "+":
            return val1 + val2
        elif operator == "-":
            return val1 - val2
        elif operator == "*":
            return val1 * val2
        elif operator == "/":
            if val2 == 0:
                return "Error: Division by zero"
            return val1 / val2
        else:
            return "Invalid operator"
    except:
        return "Error: Invalid input"

def format_number(num):
    if isinstance(num, str):
        return num
    try:
        if num == int(num):
            return str(int(num))
        else:
            return format(num, ".6f").rstrip('0').rstrip('.')
    except:
        return str(num)

def main():
    apply_theme("material_light")
    
    st.title("🧮 Material Calculator")
    st.write("Theme: " + st.session_state.theme if hasattr(st.session_state, "theme") else "Material Light")
    
    st.subheader("Calculator")
    col1, col2 = st.columns(2)
    
    val1 = st.text_input("Value 1", key="val1", on_change=lambda: None)
    val2 = st.text_input("Value 2", key="val2", on_change=lambda: None)
    
    operations = ["+", "-", "*", "/"]
    selected_op = st.selectbox("Operation", operations, key="op")
    
    result = ""
    if val1 and val2 and selected_op:
        result = calculate(val1, val2, selected_op)
        st.session_state.calc_history.append({"val1": val1, "val2": val2, "op": selected_op, "result": result})
    
    if result != "":
        st.write(f"Result: {format_number(result)}")
        
    st.subheader("Calculation History")
    for i, h in enumerate(st.session_state.calc_history[-10:]):
        st.write(f"{i+1}. {h['val1']} {h['op']} {h['val2']} = {format_number(h['result'])}")
        
    st.write("---")
    st.subheader("Unit Conversion")
    
    col1, col2 = st.columns(2)
    
    with col1:
        unit_type = st.selectbox("Type", ["Length", "Weight", "Temperature"])
        from_unit = st.selectbox("From", ["m", "cm", "km", "mm", "in", "ft", "mi", "g", "kg", "lb", "oz", "C", "F"])
        
    with col2:
        to_unit = st.selectbox("To", ["m", "cm", "km", "mm", "in", "ft", "mi", "g", "kg", "lb", "oz", "C", "F"])
        value = st.text_input("Value")
    
    if value and unit_type:
        val = float(value)
        if unit_type == "Length":
            conversions = {"m": 1, "cm": 0.01, "km": 1000, "mm": 0.001, "in": 0.0254, "ft": 0.3048, "mi": 1609.34}
            if from_unit == "in":
                converted = val * conversions[from_unit] / conversions[to_unit]
            else:
                converted = val * conversions[to_unit] / conversions[from_unit]
        elif unit_type == "Weight":
            conversions = {"g": 1, "kg": 1000, "lb": 453.592, "oz": 28.3495}
            if from_unit == "oz":
                converted = val * conversions[from_unit] / conversions[to_unit]
            else:
                converted = val * conversions[to_unit] / conversions[from_unit]
        elif unit_type == "Temperature":
            if from_unit == "C":
                celsius = val
                if to_unit == "F":
                    converted = (celsius * 9/5) + 32
                else:
                    converted = celsius
            elif from_unit == "F":
                fahrenheit = val
                if to_unit == "C":
                    converted = (fahrenheit - 32) * 5/9
                else:
                    converted = fahrenheit
            else:
                converted = val
        
        st.write(f"{val} {from_unit} = {converted:.4f} {to_unit}")

if __name__ == "__main__":
    main()