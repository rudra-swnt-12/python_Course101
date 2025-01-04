import streamlit as st #type: ignore
import pandas as pd #type: ignore
import numpy as np #type: ignore

# Title of the app
st.title('Hello Streamlit!')

# Displaying text
st.write('Here is a simple example of Streamlit.')

# Create a simple dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Display the dataframe
st.write(f"Here is the dataframe {df}")

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), # 20 rows, 3 columns
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
