import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Discount Calculator", 
    page_icon="💰", 
    layout="centered"
)

# ----------------------------
# Hide Streamlit Branding
# ----------------------------
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ----------------------------
# Custom CSS Styling
# ----------------------------
custom_css = """
    <style>
    body {
        background: linear-gradient(to right, #f0f9ff, #cbebff, #a1dbff);
        font-family: 'Arial', sans-serif;
    }
    .stNumberInput label {
        font-weight: bold;
        color: #333;
    }
    .card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        max-width: 400px;
        margin: auto;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .success-box {
        background: #e6ffed;
        color: #256029;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        border: 1px solid #a5d6a7;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ----------------------------
# App Header
# ----------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
        💰 Discount Calculator
    </h1>
    <p style='text-align: center; color: #333; font-size: 16px;'>
        Calculate your savings instantly — now in a premium look
    </p>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Main Card UI
# ----------------------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    price = st.number_input("Enter the original price (₹)", min_value=0.0, format="%.2f")
    discount = st.number_input("Enter the discount (%)", min_value=0.0, max_value=100.0, format="%.2f")

    if st.button("Calculate Final Price"):
        final_price = price - (price * discount / 100)
        st.markdown(f"<div class='success-box'>Final Price after {discount}% discount: ₹{final_price:.2f}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

