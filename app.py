import time
import streamlit as st
from utils import load_chain



st.set_page_config(
    page_title="DIP V2 Chatbot",
)

# st.image(company_logo, width=150)  
st.title("DIP V2 Chatbot")
st.write(""" 

""")

st.markdown('''This is a QA Chatbot over the DIP V2 codebase (dev branch). ''')

if 'chain' not in st.session_state:
    st.session_state['chain'] = load_chain()

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{"role": "assistant",
                                     "content": "Enter your question"}]


for message in st.session_state.messages:
    if message["role"] == 'assistant':
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


if query := st.chat_input("Ask me about DIP V2"):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.spinner("Thinking..."):
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            # Send user question to chat
            result = st.session_state['chain']({"question": query})
            response = result['answer']
                
                
            full_response = ""

            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": response})

