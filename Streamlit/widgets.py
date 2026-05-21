import streamlit as st

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
