import streamlit as st

X = st.slider("x")
st.write(X, "squared is", X * X)
