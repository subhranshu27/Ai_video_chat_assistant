from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import os

CHROMA_DIR = "vector_db"
COLLECTION_NAME = "meeting_transcript"
EMBEDDING_MODEL  = "all-MiniLM-L6-v2"

def get_embeddings():
    em=HuggingFaceEmbeddings(
        model_kwargs={"device": "cpu",
                      "token":os.getenv("HUGGINGFACEHUB_API_TOKEN")}, 
        model_name=EMBEDDING_MODEL,


    )

    return em

def build_vector_store(transcript:str)->Chroma:
    print("Building vector store")

    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks=splitter.split_text(transcript)

    docs=[
        Document(page_content=chunk,meta_data={"index":i}) for i,chunk in enumerate(chunks)
    ]

    embeding=get_embeddings()

    vector_store=Chroma.from_documents(
        documents=docs,
        embedding=embeding,
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_DIR

    )
    return vector_store

def load_vector_store()->Chroma:
    em=get_embeddings()

    vector_store=Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_DIR,
        embedding_function=em
    )

    return vector_store

def get_retriver(vs:Chroma,k:int =4):
    retriver=vs.as_retriever(
        search_type="mmr",
        search_kwargs={"k":k}
    )

    return retriver