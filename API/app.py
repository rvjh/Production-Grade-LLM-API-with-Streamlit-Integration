from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain.chat_models import ChatOllama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

## creating a fast api

app = FastAPI(
    title="Langserve API",
    version= "1.0" ,
    description="Simple Langserve APIs"
)

# add_routes(
#     app,
#     ChatOllama(),
#     path="/ollama"
# )

# model = ChatOllama()

llm = Ollama(model="llama2")

prompt = ChatPromptTemplate.from_template("write me an essay about {topic} with 100 words")

## routing by combining all -> we can add any numbers of routs

add_routes(
    app,
    prompt | llm ,
    path="/essay"
)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)    # run python app.py

    ## http://localhost:8000/docs#/ -> this api part has been created

    # next go to client to interact with the api


