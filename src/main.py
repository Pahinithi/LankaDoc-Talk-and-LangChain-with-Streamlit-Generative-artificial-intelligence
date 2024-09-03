import os

from dotenv import load_dotenv
import streamlit as st
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters.character import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Load the environment variables
load_dotenv()

working_dir = os.path.dirname(os.path.abspath(__file__))


def load_document(file_path):
    loader = UnstructuredPDFLoader(file_path)
    documents = loader.load()
    return documents


def setup_vectorstore(documents):
    embeddings = HuggingFaceEmbeddings()
    text_splitter = CharacterTextSplitter(
        separator="/n",
        chunk_size=1000,
        chunk_overlap=200
    )
    doc_chunks = text_splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(doc_chunks, embeddings)
    return vectorstore


def create_chain(vectorstore):
    llm = ChatGroq(
        model="llama-3.1-70b-versatile",
        temperature=0
    )
    retriever = vectorstore.as_retriever()
    memory = ConversationBufferMemory(
        llm=llm,
        output_key="answer",
        memory_key="chat_history",
        return_messages=True
    )
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        chain_type="map_reduce",
        memory=memory,
        verbose=True
    )
    return chain

# Set up the page config with a centered layout
st.set_page_config(
    page_title="LankaDoc Talk",
    page_icon="📄",
    layout="centered"
)

# Define the custom CSS for UI/UX enhancement
st.markdown("""
    <style>
    .reportview-container {
        background: linear-gradient(135deg, #5a5796, #965757, #819657);
    }
    .chat-message {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 10px;
        margin: 5px 0;
    }
    .chat-input {
        background-color: #f0f0f0;
        border-radius: 8px;
        padding: 10px;
    }
    .header {
        text-align: center;
        color: #ffffff;
    }
    .title {
        color: #ffffff;
        font-size: 2em;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🇱🇰 🔍 LankaDoc Talk")

# Initialize the chat history in Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


uploaded_file = st.file_uploader(label="Upload your PDF file", type=["pdf"])

if uploaded_file:
    file_path = f"{working_dir}/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = setup_vectorstore(load_document(file_path))

    if "conversation_chain" not in st.session_state:
        st.session_state.conversation_chain = create_chain(st.session_state.vectorstore)

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# User input field
user_input = st.chat_input("Ask LankaDoc Talk.....")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input, unsafe_allow_html=True)

    with st.chat_message("assistant"):
        response = st.session_state.conversation_chain({"question": user_input})
        assistant_response = response["answer"]
        st.markdown(assistant_response, unsafe_allow_html=True)
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
