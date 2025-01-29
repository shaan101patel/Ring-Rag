# pipeline_entry.py

# import os
# from decouple import config
# from utils.upload_utils import restructure_files
# from utils.query_utils import (
#     format_docs, retrieve_documents, generate_prompt, call_openai,
#     batch_insert, connect_to_zilliz, get_or_create_collection
# )

# def run_rag_pipeline(
#     do_upload=False,
#     upload_type=None,
#     files=None,
#     folder_path=None,
#     do_query=True,
#     query_text=None,
#     question=None
# ):
#     """
#     Run the entire RAG pipeline with optional file/folder upload
#     and optional query to the LLM.

#     :param do_upload: Boolean indicating if the user wants to upload data.
#     :param upload_type: 'files', 'folder', or None
#     :param files: List of file paths or file-like objects (depending on your approach).
#     :param folder_path: String path to a folder if folder upload is chosen.
#     :param do_query: Boolean indicating if we proceed to the RAG query portion.
#     :param query_text: Query text used for vector retrieval.
#     :param question: Actual question to ask the LLM after retrieval.
#     """

#     print("Starting RAG Pipeline...")

#     # 1. Load OpenAI API Key
#     openai_api_key = config("OPENAI_API_KEY")
#     if not openai_api_key:
#         raise ValueError("OpenAI API key is missing from environment variables.")

#     embedding_model = "text-embedding-ada-002"
#     uploaded_hashes = set()
#     collection_name = "AIS_Information"
#     vector_dimension = 1536

#     # 2. Connect to Zilliz DB
#     connect_to_zilliz()
#     print("Connected to Zilliz DB.")

#     # 3. Get or create the collection
#     collection = get_or_create_collection(collection_name, vector_dimension)

#     # 4. Perform uploads if requested
#     if do_upload:
#         if upload_type == "files" and files:
#             print(f"Uploading {len(files)} documents.")
#             docs = restructure_files(files, uploaded_hashes)  # You’ll adapt `upload_files` for your environment
#             print(f"Number of new documents: {len(docs[0])} (assuming docs[0] is your doc list).")
#             batch_insert(collection, docs, embedding_model, BATCH_SIZE=100)

#         elif upload_type == "folder" and folder_path:
#             # For folder uploads, gather all .pdf files or whatever your logic is
#             file_paths = [
#                 os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".pdf")
#             ]
#             print(f"Uploading {len(file_paths)} documents.")
#             docs = restructure_files(file_paths, uploaded_hashes)
#             batch_insert(collection, docs, embedding_model, BATCH_SIZE=100)

#         else:
#             print("No valid upload action was performed.")

#     # 5. If we want to query the LLM in a typical RAG flow:
#     if do_query:
#         print("Starting RAG Query Execution...")

#         if not query_text:
#             query_text = "Retrieve startup documents on AIS and Ring Rag."  # fallback or example

#         # 5a. Retrieve Documents from Zilliz
#         print("Retrieving documents...")
#         retrieved_docs = retrieve_documents(collection, query_text, embedding_model, limit=5)
#         if not retrieved_docs:
#             print("No documents found.")
#             return

#         formatted_context = format_docs(retrieved_docs)

#         # 5b. Generate Prompt
#         if not question:
#             question = (
#                 "Create a one page document with an overview of AIS and Ring Rag, and "
#                 "a brief description of how Ring Rag plans on using RAG."
#             )
#         prompt = generate_prompt(formatted_context, question)

#         # 5c. Call OpenAI API
#         print("Calling OpenAI API...")
#         result = call_openai(prompt, model="gpt-4o")
#         print("Result:", result)

#     print("Pipeline complete.")
