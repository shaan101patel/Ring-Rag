# import os
# from tkinter import filedialog, Tk
# from utils.upload_utils import restructure_files
# from decouple import config
# from utils.query_utils import format_docs, retrieve_documents, generate_prompt, call_openai, get_embedding, batch_insert, connect_to_zilliz, get_or_create_collection


# def main():
#     print("Starting RAG Pipeline...")
#     # Load OpenAI API Key
#     openai_api_key = config("OPENAI_API_KEY")
#     if not openai_api_key:
#         raise ValueError("OpenAI API key is missing from environment variables.")
#     embedding_model = "text-embedding-ada-002"
#     uploaded_hashes = set()
#     collection_name = "AIS_Information"
#     vector_dimension = 1536

#     # Connect to Zilliz DB
#     connect_to_zilliz()
#     print("Connected to Zilliz DB.")

#     # Get or create collection
#     collection = get_or_create_collection(collection_name, vector_dimension)

#     # Prompt user for inputs
#     while True:
#         user_input = input("Do you want to upload files or websites? (yes/no): ").strip().lower()
#         if user_input == "yes":
#             print("Choose the upload type:")
#             print("1. Upload files")
#             print("2. Upload folder")
#             choice = input("Enter your choice (1/2): ").strip()

#             if choice == "1":
#                 root = Tk()
#                 root.withdraw()
#                 file_paths = filedialog.askopenfilenames(title="Select files to upload")
#                 if file_paths:
#                     print(f"Uploading {len(file_paths)} documents.")
#                     docs = restructure_files(file_paths, uploaded_hashes)
#                     print(f"Number: {len(docs[0])} documents.")
#                     batch_insert(collection, docs, embedding_model, BATCH_SIZE=100)

#             elif choice == "2":
#                 folder_path = filedialog.askdirectory(title="Select folder to upload")
#                 if folder_path:
#                     file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".pdf")]
#                     print(f"Uploading {len(file_paths)} documents.")
#                     docs = restructure_files(file_paths, uploaded_hashes)
                
#                     batch_insert(collection, docs, embedding_model, BATCH_SIZE=100)

#             else:
#                 print("Invalid choice. Try again.")

#         elif user_input == "no":
#             print("Starting LLM and RAG Query Execution.")
#             break
#         else:
#             print("Invalid input. Please enter 'yes' or 'no'.")


#     # Retrieve Documents from Zilliz
#     print("Retrieving documents...")
#     query = "Retrieve startup documents on AIS and Ring Rag."
#     retrieved_docs = retrieve_documents(collection, query, embedding_model, limit=5)
#     if not retrieved_docs:
#         print("No documents found.")
#         return

#     formatted_context = format_docs(retrieved_docs)  # Now it expects list-of-lists of Hits

#     # Generate Prompt
#     question = "Create I one page document with a overview of what AIS and Ring Rag is. And a brief descirption on how ring rag plans on using RAG?"
#     prompt = generate_prompt(formatted_context, question)

#     # Call OpenAI API
#     print("Calling OpenAI API...")
#     result = call_openai(prompt, model="gpt-4o")
#     print("Result:", result)


# if __name__ == "__main__":
#     main()

