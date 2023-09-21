"""
Freely adapted from another Omdena app:
https://saudi-arabia-industrial-co2.streamlit.app
"""

# Import of all required libraries
import streamlit as st
import os

# Set the work directory to retrieve all data
temp = os.environ
script_dir = os.path.dirname(os.path.abspath(__file__))

st.write(f'{temp}')
