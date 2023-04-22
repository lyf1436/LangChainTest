from flask import Flask, jsonify, request
import requests
import sys
import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = "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"
loader = TextLoader('document.txt')
documents = loader.load()
textSplitter = RecursiveCharacterTextSplitter(chunk_size = 200, chunk_overlap = 20)
texts = textSplitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embeddings)
retriever = db.as_retriever()
retriever.search_kwargs['distance_metric'] = 'cos'
retriever.search_kwargs['k'] = 4
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever, return_source_documents=False)

# query = "what season is this product for"

# # The Hungry Lobster
# ans = qa({"query": query})

# print(ans['result])



app = Flask(__name__)





@app.route('/', methods=["GET"])
def index():
    print("Hello there, welcome to use my chat service")
    return "Hello there, welcome to use my chat service", 200


@app.route('/chat', methods=["POST"])
def test():
    question = request.form['question']
    ans = qa({"query": question})
    print(ans['result'])
    return ans['result'], 200

