import streamlit as st #type: ignore
import pandas as pd #type: ignore

st.title("Streamlit Text Input")

# Text input
name = st.text_input("Enter your name", "Type here...")
if name:
    st.write(f"Hello {name}!")

# Slider input
age = st.slider("Enter your age", 0, 100, 25) # min, max, default
st.write(f"You are {age} years old.")

# Selectbox input
options = ["Python", "Java", "C++", "Go", "Rust", "JavaScript"]
choice = st.selectbox("Choose a programming language:", options)
st.write(f"You selected {choice}.")

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sample_data.csv")
st.write(f"Here is a simple dataframe:{df}")

# Upload Button
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)