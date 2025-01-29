# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utils.upload_utils import restructure_files

# If you have a function like run_rag_pipeline or your custom retrieval logic:
from utils.query_utils import retrieve_documents, format_docs, generate_prompt, call_openai, batch_insert
from utils.query_utils import connect_to_zilliz, get_or_create_collection  # adjust imports
# from file_upload import ...

app = Flask(__name__)
CORS(app)  # Enable CORS if your frontend is on a different origin/port

@app.route('/query', methods=['POST'])
def handle_query():
    # 1. Get JSON data from request
    data = request.get_json()
    query_text = data.get('query_text', '')

    # 2. Connect to Zilliz / load or create your collection
    connect_to_zilliz()
    collection = get_or_create_collection("AIS_Information", 1536)  # adapt your actual name/dim

    # 3. Retrieve documents and format context
    retrieved_docs = retrieve_documents(collection, query_text, "text-embedding-ada-002", limit=5)
    if not retrieved_docs:
        return jsonify({"answer": "No relevant documents found."})

    formatted_context = format_docs(retrieved_docs)

    # 4. Build a prompt and call OpenAI
    prompt = generate_prompt(formatted_context, query_text)
    
    print(f"Prompt: {prompt}")

    result = call_openai(prompt, model="gpt-4o-mini")  # or your chosen model

    # 5. Return the answer
    return jsonify({"answer": result})



# File/Folder/Website upload logic:



UPLOAD_FOLDER = "uploads"  # Adjust if needed
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the folder exists

embedding_model = "text-embedding-ada-002"
uploaded_hashes = set()
collection = "AIS_Information"  # Or your actual collection object if needed
vector_dimension = 1536

@app.route("/upload_file", methods=["POST"])
def upload_file():
    """
    Endpoint for uploading a single file and running it through the RAG pipeline.
    """
    connect_to_zilliz()
    collection = get_or_create_collection("AIS_Information", 1536)  # adapt your actual name/dim


    # 1. Check if we actually got a file from the request
    if "file" not in request.files:
        return jsonify({"error": "No file part in request."}), 400

    file = request.files["file"]
    # For debugging: show what we received
    print(f"Received file object: {file}")

    if file.filename == "":
        return jsonify({"error": "No file selected."}), 400

    # 2. Build the full path and save the file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    print(f"Saved file to: {file_path}")

    # 3. Pass the *full path* into your ingestion logic
    #    If `restructure_files` expects a list, wrap file_path in [ ]
    docs = restructure_files([file_path], uploaded_hashes)

    # 4. Insert embeddings into your vector store
    batch_insert(collection, docs, embedding_model, BATCH_SIZE=100)

    return jsonify({"message": f"File '{file_path}' uploaded and ingested."}), 200


@app.route("/upload_folder", methods=["POST"])
def upload_folder():
    """
    Endpoint for uploading multiple files (folder).
    The frontend sends them via webkitdirectory.
    """
    connect_to_zilliz()
    collection = get_or_create_collection("AIS_Information", 1536)  # adapt your actual name/dim


    if not request.files:
        return jsonify({"error": "No files in request."}), 400

    file_paths = []
    # 1. Gather all uploaded files, save each to disk, and store the *full path*
    for f in request.files.getlist("files"):
        if f.filename:
            saved_path = os.path.join(UPLOAD_FOLDER, f.filename)
            f.save(saved_path)
            file_paths.append(saved_path)
            print(f"Saved folder file to: {saved_path}")

    if not file_paths:
        return jsonify({"error": "No files were actually saved."}), 400

    # 2. Call your ingestion logic with the list of full paths
    docs = restructure_files(file_paths, uploaded_hashes)

    # 3. Insert embeddings into your vector store
    batch_insert(collection, docs, embedding_model, BATCH_SIZE=100)

    return jsonify({
        "message": "Folder files uploaded and ingested.",
        "files": file_paths
    }), 200



@app.route("/process_url", methods=["POST"])
def process_url():
    """
    Receives a URL in JSON, processes it for ingestion.
    """
    data = request.get_json()
    url = data.get("url", None)

    if not url:
        return jsonify({"error": "No URL provided."}), 400
    
    # Insert logic to fetch the URL, parse HTML, embed, etc.
    # e.g. docs = fetch_and_parse_url(url)
    # batch_insert(collection, docs, ...)

    return jsonify({"message": f"URL {url} processed successfully."}), 200



if __name__ == '__main__':
    app.run(debug=True)
