import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0,100)
st.write(f'Yor age is {age}')

options = ["Python", 'Java','C++',"Javascript"]
choice = st.selectbox("Choose your favourite language:", options)
st.write(f'You selected {choice}.')

if name :
    st.write(f"Hello, {name}!")
if age==0:
    st.write(f"Hey {name} Sorry you are not eligible")
elif age <=10:
    st.write(f"Hey {name}! Sorry you are not eligible")

else :
    st.write("Hurray! You are eligible")

data = {

    "Name": ["Alice", "Bob", "Charlie", "David"],

    "Age": [22, 25, 21, 24],

    "City": ["New York", "London", "Paris", "Tokyo"]

}

df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
