

def m(s):
  d={}
  for i in s:
    d[i] = s.count(i)
  return d
m("sdlvnlkn")

def m(a,b):
  d = {}
  for i in a:
    d[i] = True
  for j in b:
    if j in d:
      return j
  return None

m([1,2,3],[2,3])


def m(l,x):
  d={}
  for i in l:
    diff = x - l[i]
    if diff in d:
      return [d[diff],i]
    else:
      d[l[i]] = i 
  
m([1,2,3,4],7)


def m(x):
  if x==0 or x==1:
    return 1
  else:
    return x*m(x-1)
m(10)

def per(n,r):
  if n>r:
    return m(n)/m(n-r)
def com(n,r):
  if n>r:
    return m(n)/(m(r)*m(n-r))

print(per(5,2))
print(com(5,2))

def m(x):
  l=[0,1]
  if x==0:
    return l[0]
  elif x==1:
    return l
  else:
    a,b = 0,1
    for i in range(2,x):
      c = a + b
      l.append(c)
      a = b
      b = c
  return l

m(10)



a = lambda x,y: x*y
a(10,2)

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














