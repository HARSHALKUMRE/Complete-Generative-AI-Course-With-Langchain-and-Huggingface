import validators, streamlit as st  
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

## streamlit app
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

## Get the Grow API key and url (YT or Website) to be summarized
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")
    
    
url = st.text_input("URL", label_visibility="collapsed")

if st.button("Summarize the Content from YT or Website"):
    ## Validate all the inputs 
    if not groq_api_key.strip() or not url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(url):
        st.error("Please enter a valid Url. It can may be a YT video utl or website url")
        
    else:
        try:
            with st.spinner("Waiting.."):
                ## loading the website or yt video data
                if "youtube.com" in url:
                    pass
            pass
        except:
            pass
    