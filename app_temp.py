"""
Freely adapted from another Omdena app:
https://saudi-arabia-industrial-co2.streamlit.app
"""

# Import of all required libraries
import requests
import pandas as pd
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.dates as mdates
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import pickle
import statsmodels.api as sm
import darts
import random
from darts import TimeSeries
from darts.dataprocessing.transformers import Scaler
from sklearn.preprocessing import StandardScaler
from darts.models import RegressionModel, CatBoostModel, RandomForest, LightGBMModel, XGBModel, RNNModel
from darts.metrics import rmse, mape
from statsmodels.tsa.arima.model import ARIMA
import os
import plotly.graph_objects as go
import plotly.figure_factory as ff

# Set the work directory to retrieve all data
temp = os.environ
script_dir = os.path.dirname(os.path.abspath(__file__))

st.write(f'{temp}')
