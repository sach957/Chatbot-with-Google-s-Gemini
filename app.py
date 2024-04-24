import google.generativeai as genai

import warnings 
warnings.filterwarnings('ignore')
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
key="AIzaSyDgkL5jUfoLvXk5v8Xe7USiYGpn0NwT_0w"

import os

from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model="gemini-pro")

def get_genai_response(question):
    response=model.invoke(question)
    return response.content


st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Pro App")

ques=st.text_input("Input the question you want to ask: ",key="input")

submit = st.button("Ask the Quesion")

if submit:
    response = get_genai_response(ques)
    st.subheader("The Response is")
    st.write(response)



from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def prom(place):
    prompt_template = PromptTemplate(input_variables = ['country'],
                                     template="Tell me the capital of {country}")

    chain = LLMChain(llm=model,prompt=prompt_template)
    response=chain.invoke(place)
    return response['text']


ques2=st.text_input("Input the country/state whose capital you want to know: ",key="input2")

submit2 = st.button("Enter the state/country")

if submit2:
    response2 = prom(ques2)
    st.subheader("The Response is")
    st.write(response2)
