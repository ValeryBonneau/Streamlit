"""
Freely adapted from another Omdena app:
https://saudi-arabia-industrial-co2.streamlit.app
"""

# Import of all required libraries
import streamlit as st
import os
import json
from darts.models import RegressionModel, CatBoostModel, RandomForest, LightGBMModel, XGBModel, RNNModel

# Set the work directory to retrieve all data
temp = os.environ
script_dir = os.path.dirname(os.path.abspath(__file__))


config_json = "config.json"
models_dir = "models"
rel_to_config_json_path = os.path.join(script_dir, config_json)

with open(rel_to_config_json_path, 'r') as f:
    # Load JSON data from file
    json_data = json.load(f)

# Load evo_model json_data['evo_model']
evo_model_path = os.path.join(script_dir, models_dir, json_data["evo_model"])
evo_model = RNNModel.load(evo_model_path, map_location='cpu')


st.write(f'{temp}')
