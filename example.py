import streamlit as st

"""
# Hello world

This is an app
"""

num = st.slider("Pick a number")

st.metric("My number", num)