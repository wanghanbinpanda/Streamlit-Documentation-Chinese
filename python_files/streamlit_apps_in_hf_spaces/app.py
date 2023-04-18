# This file is .....
# Author: Hanbin Wang
# Date: 2023/4/18
import transformers
import streamlit as st

from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("gpt2-large")


@st.cache
def load_model(model_name):
    model = AutoModelWithLMHead.from_pretrained("gpt2-large")
    return model


model = load_model("gpt2-large")