

from functools import reduce

reduce(a,[1,2,3,4])

a = [1,2]
b = ['a','b']
c = dict(zip(a,b))
print(c)
c.update({3:'c'})
print(c)

a = [1,2,3]
b = [3,4,5]
c = set(a).union(set(b))
d = set(a).intersection(set(b))
e = set(a).difference(set(b))

print(c)
print(d)
print(e)

import numpy as np

def mat_mul(a,b):
  col_a = a.shape[0]
  row_b = b.shape[1]
  if col_a != row_b:
    return "not possible"
  else:
    r = np.zeros((col_a, row_b))
    for i in range(col_a):
      for j in range(row_b):
        for k in range(col_a):
          r[i][j] = r[i][j] + a[i][k]*b[k][j]
    return r

a = np.array([
    [1,3],[4,1]
])

b = np.array([
    [1,3],[4,1]
])

mat_mul(a,b)

from langchain_community.document_loaders import TextLoader, WebBaseLoader, PyPDFLoader
import bs4
from langchain.text_splitter import  RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

## Textloader
loader = TextLoader("RAG/speech.txt")
text_documents = loader.load()

print(text_documents)

## webloader

# web_loader = WebBaseLoader(web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
#                            bs_kwargs=dict(parse_only=bs4.SoupStrainer(
#                                class_=("post-title","post-content","post-header")
#                            )))
#
# text_documents_web = web_loader.load()
# print(text_documents_web)

## load from PDF

pdf_loader = PyPDFLoader(file_path="RAG/Srijan Nirmal Kumar Galla_Data Analyst (1).pdf")
text_pdf_loader = pdf_loader.load()
print(text_pdf_loader)

## text splitting

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)
documents = text_splitter.split_documents(text_pdf_loader)
print(documents)

## vector embeddings and vectr store

db = Chroma(documents[:], OllamaEmbeddings())

query = "Who are the authors of attention is all you need?"
retireved_results=db.similarity_search(query)
print(retireved_results[0].page_content)







