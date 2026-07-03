
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("youtube_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("YouTube Earnings Predictor")

st.write("Enter the channel details below to estimate earnings.")

# User Inputs
views = st.number_input("Total Video Views", min_value=0, value=100000, step=1000)
uploads = st.number_input("Total Uploads", min_value=0, value=50, step=1)
subscribers = st.number_input("Total Subscribers", min_value=0, value=10000, step=100)

# Predict
if st.button("Predict Earnings"):
    input_data = pd.DataFrame(
        [[views, uploads, subscribers]],
        columns=["video views", "uploads", "subscribers"]
    )

    prediction = model.predict(input_data)

    st.success(f"Estimated Earnings: ${prediction[0]:,.2f}")
