# import os
# from tkinter import filedialog, Tk
# import textwrap
# import fitz


# def upload_files(file_paths):
#     """Upload multiple files and return titles & descriptions in a 2D list."""
#     data = [[], []]  # [titles, descriptions]
#     for file_path in file_paths:
#         if file_path.endswith(".pdf"):
#             docs = load_pdf(file_path)
#             for doc in docs:
#                 title = doc["metadata"]["source"]
#                 description = doc["page_content"]
#                 data[0].append(title)
#                 data[1].append(description)
#                 print(f"Uploaded PDF: {title}")
#         elif file_path.endswith(".txt"):
#             with open(file_path, "r") as f:
#                 text = f.read()
#                 title = file_path
#                 description = text
#                 data[0].append(title)
#                 data[1].append(description)
#         else:
#             print(f"Unsupported file type: {file_path}")
#             continue
#     return data



# def load_pdf(file_path):
#     """Load a PDF file and extract its text content."""
#     documents = []
#     try:
#         doc = fitz.open(file_path)
#         for page_num in range(len(doc)):
#             page = doc.load_page(page_num)
#             text = page.get_text()
#             documents.append({
#                 "page_content": text,
#                 "metadata": {"source": file_path, "page": page_num},
#             })
#     except Exception as e:
#         print(f"Error processing PDF {file_path}: {e}")
#     return documents


# folder_path = filedialog.askdirectory(title="Select folder to upload")
# if folder_path:
#     file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".pdf")]
# print(file_paths)

# data = upload_files(file_paths)
# print(data)
# print((data[0]))
# print(len(data[1]))
# print(len(data[0]))


# print(res.)


# print("Request status code:", res.status_code)

# for i, hit in enumerate(res):
#         print('Results:')
#         for ii, hits in enumerate(hit):
#             print('\t' + 'Rank:', ii + 1, 'Title:', hits.entity.get('title'))
#             print(textwrap.fill(hits.entity.get('description'), 88))
#             print()

#             hits.



# import google.generativeai as genai

# genai.configure(api_key="AIzaSyBxtYWh-4ofsYjXmhvdu5Ne0pbolfcO_BU")
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Explain how AI works")
# print(response.text)



import os
from openai import OpenAI

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="backend\\ragapp\\rag-app\\.env")

# Retrieve the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Your test code here

client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)

print(completion.choices[0].message.content)






# import os
# import openai
# from openai import OpenAI

# # Set your API key
# openai.api_key = "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"
# os.environ['OPENAI_API_KEY'] = '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'



# try:
#     # Make a test API call
    
#     client = OpenAI(
#         organization='org-nHfTrCzFD9yhNjkomPMQ9fM9',
#         project='proj_d1R0g7dreOFj6FAVnt1hcxz9',
#     )
#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         store=True,
#         messages=[
#         {"role": "user", "content": "what are the colors of the rainbow?"},
#     ]
# )
    
#     print(response.choices[0].text.strip())
# except openai.error.AuthenticationError:
#     print("Invalid API key or authentication error.")
# except Exception as e:
#     print(f"An error occurred: {e}")
