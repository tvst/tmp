import streamlit as st

"""
# Hello world

This is an app
"""

with st.sidebar:
    num = st.slider("Pick a number")
    
    
a, b = st.columns(2)

with a:
    f"# {num}"

with b:
    st.metric("My number", num)
