import streamlit as st
import pandas as pd
import numpy as np

st.header("MLB Game prediction")
# team=st.text_input("enter your prompt")
# st.write(
# f"your winning : {team}")
st.subheader("Aug 05-Best Bet Recommendation")
body = """

Miami Marlins (+1.5 at -185)   - perplexity
Houston Astros (-1.5 at +143)  - Grok

"""
st.code(body)

st.subheader("AI Prediction Data")
re=pd.read_csv("mlb_betting_analysis.csv")
st.write(re)

