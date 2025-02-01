streamlit_app.py
import streamlit as st

st.title("Anomaly Detection in Network Traffic")
st.write("Welcome to the Network Traffic Anomaly Detection App!")

# Upload file
uploaded_file = st.file_uploader("Upload your network traffic dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    st.write("File uploaded successfully!")
