<img width="760" height="657" alt="image" src="https://github.com/user-attachments/assets/611323fc-0276-4621-a3c6-9cfc4af018ba" />
# Basic-Rag-Chatbot-HSC
For HSC students who wants help with their studies
Backend Workflow
1. PDF Loader:
- Loads and splits content using RecursiveCharacterTextSplitter
- Source: /Data/ folder
2. Embeddings:
- Model: sentence-transformers/all-MiniLM-L6-v2
3. Vector Store:
- Qdrant Cloud (hsc-bot-qdrant2)
- Similarity search (k=5)
4. Language Model:
- Qwen/Qwen3-0.6B via Hugging Face Transformers

project repo:https://github.com

conda create -n 11mapp python=3.10 -y

conda activate llmapp

### STEP 02 install the requirements

pip install -r requirements.txt
