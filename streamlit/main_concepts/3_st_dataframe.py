# This file is .....
# Author: Hanbin Wang
# Date: 2023/4/17
import streamlit as st
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)