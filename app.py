from flask import Flask, render_template,jsonify,request
from src.helper import HuggingFaceEmbeddings,HuggingFacePipeline,HumanMessagePromptTemplate,text_split,load_pdf_file
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.chains import create_retrieval_chain
import torch
from qdrant_client import QdrantClient
from langchain.vectorstores import Qdrant
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

# Check for GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

extracted_data = load_pdf_file(data='Data/')
text_chunks = text_split(extracted_data)

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

collection_name = "hsc-bot-qdrant2"

docsearch = Qdrant.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    url="https://e4e35b2d-339f-4fd1-be49-f757c694232d.us-west-1-0.aws.cloud.qdrant.io:6333",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.hET2Ps4DMbkBTIIwOAc5sHHbP704CLyevrk0FGRRYso",
    collection_name=collection_name,
    prefer_grpc=False,
    
    
)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# 4. Qwen Model Setup
print("Loading Qwen3-0.6B model...")
model_name = "Qwen/Qwen3-0.6B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    device_map="auto" if device == "cuda" else None,
    low_cpu_mem_usage=True
)

# Create generation pipeline
try:
 qwen_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=500,
    temperature=0.4,
    top_p=0.9,
    device=0 if device == "cuda" else -1
 )
except Exception as e:
    print("Error loading model:", e)
    exit(1)
# LangChain wrapper
llm = HuggingFacePipeline(pipeline=qwen_pipeline) 

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt + "\nContext: {context}"),
    ("human", "{input}"),
])

rag_chain = create_retrieval_chain(
    retriever,
    create_stuff_documents_chain(llm, prompt)
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg= request.form["msg"]
    input=msg
    print(input)
    response = rag_chain.invoke({"input":msg})
    print("Response: ", response["answer"])
    return str(response["answer"])

if __name__ == '__main__':
    print(" Flask app starting...")
    app.run(host="0.0.0.0", port=8080, debug=False)



