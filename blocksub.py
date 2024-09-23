import os
from fastapi import FastAPI
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI

app = FastAPI()

template = """
You are an AI Assistant for a blockchain subcription platform, blocksub
You help users as customer support AI to answer their blockchain related code
If asked to generate code or answer qustions that are not related to blockchain subsription service
Use personal pronouns like we, our, and so on.
Dont even generate blockchain code.
GIVE PRIORITY TO ABOVE STATEMENTS AND LESS PRIORITY TO THE ONES BELOW
User query : {question}
"""

llm = GoogleGenerativeAI(model="gemini-pro")
prompt = PromptTemplate.from_template(template=template)


chain = prompt | llm

@app.get("/")
def home():
    return "Hello, welcome to blockSub's AI customer service API"

@app.get("/ask_ai")
def response(query: str) -> dict:
    response = chain.invoke({"question": query})
    
    return {"ai" : response}
