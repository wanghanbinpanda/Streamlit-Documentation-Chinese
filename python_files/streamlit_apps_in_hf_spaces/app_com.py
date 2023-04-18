# This file is .....
# Author: Hanbin Wang
# Date: 2023/4/18
import transformers
import streamlit as st
from PIL import Image

from transformers import RobertaTokenizer, T5ForConditionalGeneration
from transformers import pipeline


def main():
    # `st.set_page_config` is used to display the default layout width, the title of the app, and the emoticon in the browser tab.

    st.set_page_config(
        layout="centered", page_title="MaMaL-Com Demo(代码补全)", page_icon="❄️"
    )

    c1, c2 = st.columns([0.32, 2])

    # The snowflake logo will be displayed in the first column, on the left.

    with c1:
        st.image(
            "./panda.png",
            width=100,
        )

    # The heading will be on the right.

    with c2:
        st.caption("")
        st.title("MaMaL-Com(代码补全)")


    ############ SIDEBAR CONTENT ############

    st.sidebar.image("./panda.png",width=270)

    st.sidebar.markdown("---")

    st.sidebar.write(
    """
    ## 使用方法：
    在【输入】文本框输入未完成的代码，点击【补全】按钮,即会显示补全的代码。
    """
    )

    st.sidebar.write(
    """
    ## 注意事项：
    1）APP托管在外网上，请确保您可以全局科学上网。
    
    2）您可以下载[MaMaL-Com](https://huggingface.co/hanbin/MaMaL-Com)模型，本地测试。（无需科学上网）
    """
    )


    st.sidebar.markdown("---")


    # Let's add some info about the app to the sidebar.

    st.sidebar.write(
    """
    App 由 东北大学NLP课小组成员创建， 使用 [Streamlit](https://streamlit.io/)🎈 和 [HuggingFace](https://huggingface.co/inference-api)'s [MaMaL-Com](https://huggingface.co/hanbin/MaMaL-Com) 模型.
    """
    )

    st.write(
        "> **Tip：** 首次运行需要加载模型，可能需要一定的时间！"
    )

    st.write(
        "> **Tip：** 该Demo使用了Hugging Face 的 Pipeline,可能需要网络非常顺畅"
    )

    # model, tokenizer = load_model("hanbin/MaMaL-Gen")
    st.write("### 输入：")
    input = st.text_area("", height=200)
    button = st.button('补全')
    st.write("### 输出：")
    generator = pipeline('text-generation', model="E:\DenseRetrievalGroup\卢帅学长ckpt\py150_model\checkpoint")
    output = generator(input)
    # code = '''def hello():
    #     print("Hello, Streamlit!")'''
    if button:
        st.code(output, language='python')
    else:
        st.write('')




if __name__ == '__main__':

    main()