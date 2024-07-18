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



