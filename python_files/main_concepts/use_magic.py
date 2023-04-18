# This file is .....
# Author: Chengxing Zhou
# Date: 2023/4/17

"""
# My first app
Here's our first attempt at using data to create a table:
"""
# begin
import streamlit as st
import pandas as pd
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
# end

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
