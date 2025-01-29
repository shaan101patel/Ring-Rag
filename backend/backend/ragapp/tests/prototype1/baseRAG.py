# import os
# import bs4
# import numpy as np
# from langchain import hub
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.document_loaders import WebBaseLoader
# from langchain_community.vectorstores import Chroma
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnablePassthrough
# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# import tiktoken

# # Environment Setup
# os.environ['LANGCHAIN_TRACING_V2'] = 'true'
# os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
# os.environ['LANGCHAIN_API_KEY'] = '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'
# os.environ['LANGCHAIN_PROJECT'] = 'prototype1.0'
# os.environ['LANGCHAIN_USER_AGENT'] = 'Shaan M Patel'
# os.environ['OPENAI_API_KEY'] = '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'



# print("Line 19")


# # Functions
# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)

# def num_tokens_from_string(string: str, encoding_name: str) -> int:
#     encoding = tiktoken.get_encoding(encoding_name)
#     return len(encoding.encode(string))

# def cosine_similarity(vec1, vec2):
#     dot_product = np.dot(vec1, vec2)
#     norm_vec1 = np.linalg.norm(vec1)
#     norm_vec2 = np.linalg.norm(vec2)
#     return dot_product / (norm_vec1 * norm_vec2)

# # Load Documents
# loader = WebBaseLoader(
#     web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
#     bs_kwargs=dict(
#         parse_only=bs4.SoupStrainer(
#             class_=("post-content", "post-title", "post-header")
#         )
#     ),
# )
# docs = loader.load()

# # Split Documents
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# splits = text_splitter.split_documents(docs)

# # Embed and Index
# vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
# retriever = vectorstore.as_retriever()

# # Prompt and LLM Setup
# prompt = hub.pull("rlm/rag-prompt")
# llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# # RAG Chain
# rag_chain = (
#     {"context": retriever | format_docs, "question": RunnablePassthrough()}
#     | prompt
#     | llm
#     | StrOutputParser()
# )

# # Run Query
# result = rag_chain.invoke("What are the case studies in the document?")
# print("Result:", result)

