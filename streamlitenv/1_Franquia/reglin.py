# Import
## User Interface
import streamlit as st
## Data Use
import pandas as pd
## Create Model Linear Regression 
from sklearn.linear_model import LinearRegression
## Generate Graphic
import matplotlib.pyplot as plt

# Load Data
data = pd.read_csv("slr12.csv", sep=";")

# Separate Variables
X = data[['FrqAnual']] # Its posible have more than one indepentent variable
y = data['CusInic'] # Dependent variable usually is one in this case

# Create Model
model = LinearRegression().fit(X, y)