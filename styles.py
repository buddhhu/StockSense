import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .stock-price-up {
            color: #00873c;
            font-weight: bold;
        }
        .stock-price-down {
            color: #ff4b4b;
            font-weight: bold;
        }
        .metric-container {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 0.5rem 0;
        }
        </style>
    """, unsafe_allow_html=True)
