import streamlit as st
import numpy as np
import pandas as pd



#Title of the application
st.title("Hello Streamlit")

#Display a simple text
st.write("This is a simple text")

#Create a simple Dataframe
df = pd.DataFrame({
    'first_column' : [1,2,3,4],
    'second_column' : [10,20,30,40]
})

# Display the data frame
st.write('Here is the dataframe')
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)