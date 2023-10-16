import streamlit as st
import openai
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate

openai.api_key = st.secrets["OPENAI_API_KEY"]


@st.cache_resource
def load_chain():
    
    # OpenAI models
    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI(model='gpt-4', temperature=0)

    # Create retriever
    vector_store = FAISS.load_local("faiss_index", embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    # Create memory
    memory = ConversationBufferWindowMemory(k=3, memory_key="chat_history")
    
    # Create chain
    chain = ConversationalRetrievalChain.from_llm(llm,
                                                  retriever=retriever,
                                                  memory=memory,
                                                  get_chat_history=lambda h: h,
                                                  verbose=True)

    # Create system prompt
    template = """
    You are an AI assistant for answering questions about a Spark Structured Streaming data pipeline. The pipeline  
    ingests, transforms and enriches wearables fitness data. The pipeline is in the medallion architecture, moving from bronze  
    to silver to gold. The context provided will include current development source code for the pipeline. 

    Use the following context from the current development codebase to help answer questions about the pipeline.
    If you don't know the answer, just say 'Sorry, I don't know... 😔'.
    Don't try to make up an answer.

    {context}
    Question: {question}
    Helpful Answer:"""

    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)
    chain.combine_docs_chain.llm_chain.prompt.messages[0] = SystemMessagePromptTemplate(prompt=QA_CHAIN_PROMPT)

    return chain
