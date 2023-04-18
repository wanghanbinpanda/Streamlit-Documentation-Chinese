# This file is .....
# Author: Chengxing Zhou
# Date: 2023/4/17

import streamlit as st
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
