import streamlit as st

# App title
st.title("💰 Discount Calculator")

# Input fields
price = st.number_input("Enter the original price (₹)", min_value=0.0, format="%.2f")
discount = st.number_input("Enter the discount (%)", min_value=0.0, max_value=100.0, format="%.2f")

# Calculate when button is clicked
if st.button("Calculate Final Price"):
    final_price = price - (price * discount / 100)
    st.success(f"Final Price after {discount}% discount: ₹{final_price:.2f}")
