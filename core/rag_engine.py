import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableLambda,RunnablePassthrough

from core.vector_store import build_vector_store,get_embeddings,get_retriver,load_vector_store

from core.summarizer import get_llm


def format_docs(docs):
    formated_doc="\n\n".join([doc.page_content for doc in docs])
    return formated_doc

def build_rag_chain(transcrpit:str):
    llm=get_llm()
    vs=build_vector_store(transcrpit)

    retriver=get_retriver(vs)

    prompt = ChatPromptTemplate.from_messages(

        [(
            "system",
            """You are an expert meeting assistant. Answer the user's question 
            based ONLY on the meeting transcript context provided below.

            If the answer is not found in the context, say: 
            "I could not find this information in the meeting transcript."

            Always be concise and precise. If quoting someone, mention it clearly.

            Context from meeting transcript:
            {context}""",),
        
            ("human", "{question}"),
    ]
    )

    rag_chain = (

        {"context" : retriver | RunnableLambda(format_docs),
         "question": RunnablePassthrough()
         }
         |prompt|llm|StrOutputParser()
    )

    return rag_chain


def load_rag_chain():
    vs=load_vector_store()

    retriver=get_retriver()

    llm=get_llm()

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are an expert meeting assistant. Answer the user's question 
based ONLY on the meeting transcript context provided below.

If the answer is not found in the context, say: 
"I could not find this information in the meeting transcript."

Always be concise and precise. If quoting someone, mention it clearly.

Context from meeting transcript:
{context}""",
        ),
        ("human", "{question}"),
    ])

    rag_chain = (
        {
            "context":  retriver| RunnableLambda(format_docs),
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain

def ask_question(rag_chain, question:str) -> str:
    print(f"Question : {question}")
    answer = rag_chain.invoke(question)
    print(f"answer :{answer}")
    return answer



