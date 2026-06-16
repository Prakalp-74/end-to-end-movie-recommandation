import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Telusko Trac", layout="wide")

# Custom CSS for styling (simplified)
st.markdown("""
    <style>
    .main { background-color: #6c63ff; }
    </style>
    """, unsafe_allow_html=True)

st.title("📦 Telusko Trac")

# Initialize session state for products
if 'products' not in st.session_state:
    st.session_state.products = pd.DataFrame([
        {"ID": 1, "Name": "Phone", "Description": "A smartphone", "Price": 699.99, "Quantity": 50},
        {"ID": 2, "Name": "Laptop", "Description": "A powerful laptop", "Price": 999.99, "Quantity": 30},
        {"ID": 3, "Name": "Pen", "Description": "A blue ink pen", "Price": 1.99, "Quantity": 100},
        {"ID": 4, "Name": "Table", "Description": "A wooden table", "Price": 199.99, "Quantity": 20},
    ])

# Top Row: Add Product section
with st.container():
    st.subheader("Add Product")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: p_id = st.text_input("ID")
    with col2: p_name = st.text_input("Name")
    with col3: p_desc = st.text_input("Description")
    with col4: p_price = st.number_input("Price", min_value=0.0)
    with col5: p_qty = st.number_input("Quantity", min_value=0)
    
    if st.button("Add"):
        new_row = {"ID": p_id, "Name": p_name, "Description": p_desc, "Price": p_price, "Quantity": p_qty}
        st.session_state.products = pd.concat([st.session_state.products, pd.DataFrame([new_row])], ignore_index=True)
        st.rerun()

# Display Table
st.subheader("Products")
# Using data_editor to allow Edit/Delete functionality easily
edited_df = st.data_editor(st.session_state.products, use_container_width=True)
st.session_state.products = edited_df