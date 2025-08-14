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
    #MainMenu {visibility: hidden;}     /* Hide Streamlit menu (GitHub link, About, etc.) */
    footer {visibility: hidden;}        /* Hide the footer */
    header {visibility: hidden;}        /* Hide the header */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ----------------------------
# Custom Branded Header
# ----------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
        💰 Discount Calculator
    </h1>
    <p style='text-align: center; color: gray; font-size: 16px;'>
        Calculate your savings instantly
    </p>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# App Logic
# ----------------------------
price = st.number_input("Enter the original price (₹)", min_value=0.0, format="%.2f")
discount = st.number_input("Enter the discount (%)", min_value=0.0, max_value=100.0, format="%.2f")

if st.button("Calculate Final Price"):
    final_price = price - (price * discount / 100)
    st.success(f"Final Price after {discount}% discount: ₹{final_price:.2f}")
