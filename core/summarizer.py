from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough,RunnableLambda,RunnableSequence

import os
from dotenv import load_dotenv
load_dotenv()
def get_llm():
    llm=ChatGoogleGenerativeAI(
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        model='gemini-3.5-flash-lite'
    )

    return llm

def split_transcript(transcript:str)->list:
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=100,

    )
    return splitter.split_text(transcript)

def get_summary(script:str)->str:

    llm =get_llm()
    map_prompt=ChatPromptTemplate.from_messages(
        [
            ("system","summarize this portion of meeting concisely."),
            ("human","{text}")

        ]
        )

    parser=StrOutputParser()

    map_chain = map_prompt | llm |parser

    chunks= split_transcript(transcript=script)

    chunk_summary=[map_chain.invoke({'text':chunk}) for chunk in chunks]

    combined="\n\n".join(chunk_summary)
    combined_prompt=ChatPromptTemplate.from_messages(
        [("system","You are an expert meeting summarizer. Combine the following text  "
        "into one final professional meeting summary in bullet points.",),
        ("human","{text}")


    ])

    combined_chain=RunnableSequence(
        RunnablePassthrough() ,RunnableLambda(lambda x:{"text":x}) ,combined_prompt , llm , StrOutputParser()
    )

    return combined_chain.invoke(combined)



def generate_title(transcipt : str) -> str:
    llm = get_llm()
    title_chain = (
        RunnablePassthrough() | RunnableLambda(lambda x:{"text":x}) | 
        ChatPromptTemplate.from_messages([
             (
                "system",
                "Based on the meeting transcript, generate a short professional meeting title "
                "(max 8 words). Only return the title, nothing else.",
            ),
            ("human", "{text}"),
        ])
        | llm
        |StrOutputParser()
    )

    return title_chain.invoke(transcipt[:2000])




