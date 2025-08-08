import streamlit as st
import pandas as pd
import numpy as np


st.markdown(
    """
    <style>
    .stApp [data-testid="stDecoration"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.header("MLB Game prediction")
# team=st.text_input("enter your prompt")
# st.write(
# f"your winning : {team}")
st.subheader("Aug 08-Best Bet Recommendation")
body = """

team A   - perplexity
team B - Grok

"""
st.code(body)

st.subheader("AI Prediction Data")
re=pd.read_csv("mlb_betting_analysis.csv")
st.write(re)


