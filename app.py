import google.generativeai as genai
import warnings 
warnings.filterwarnings('ignore')

from IPython.display import Markdown

import streamlit as st
key="AIzaSyDgkL5jUfoLvXk5v8Xe7USiYGpn0NwT_0w"
genai.configure(api_key=key)

def get_genai_response(question="Welcome"):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(question)
    return response.text

# sam = "write a pick up to ask for a date"
# response = get_genai_response(sam)
# print(response)

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Pro App")

ques=st.text_input("Input: ",key="input")

submit = st.button("Ask the Quesion")

if submit:
    response = get_genai_response(ques)
    st.subheader("The Response is")
    st.write(response)