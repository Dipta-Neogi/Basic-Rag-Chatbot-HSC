from src.helper import load_pdf_file, text_split,HuggingFaceEmbeddings,HuggingFacePipeline, HumanMessagePromptTemplate
from qdrant_client import QdrantClient
from langchain.vectorstores import Qdrant
from dotenv import load_dotenv
import os

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
    prefer_grpc=False  
)
