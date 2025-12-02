import streamlit as st
from data import MOVIES

st.set_page_config(page_title="Mini Netflix", layout="wide")

# --- HEADER ---
st.markdown("<h1 style='text-align:center;color:red;'>Mini Netflix Demo</h1>", unsafe_allow_html=True)
st.write("Browse a simple movie catalog like Netflix.")

# --- SEARCH BAR ---
query = st.text_input("Search Movies", "")

# Filter movies
filtered = [m for m in MOVIES if query.lower() in m["title"].lower()]

# --- DISPLAY MOVIES IN GRID ---
cols = st.columns(4)

for i, movie in enumerate(filtered):
    with cols[i % 4]:
        st.image(movie["image"], use_column_width=True)
        st.caption(movie["title"])
