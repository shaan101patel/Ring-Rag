import hashlib
import fitz  # PyMuPDF
import os

print("file_upload.py imports are working!") 

def hash_file(file_path):
    """Create a hash of the file contents to track processed files."""
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    return file_hash


def load_pdf(file_path):
    """Load a PDF file and extract its text content."""
    documents = []
    try:
        doc = fitz.open(file_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            documents.append({
                "page_content": text,
                "metadata": {"source": file_path, "page": page_num},
            })
    except Exception as e:
        print(f"Error processing PDF {file_path}: {e}")
    return documents


def chunk_text(text, chunk_size=1200):
    """
    Split text into chunks of a given size.
    """
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i : i + chunk_size])
    return chunks

# * 
def restructure_files(file_paths, uploaded_hashes):
    """
    Upload multiple files. Concatenate all text from a file, then chunk it, then
    name each chunk using the filename and the chunk number (e.g., "file.pdf - 1").
    Returns titles & descriptions in a 2D list.
    """
    data = [[], []]  # [titles, descriptions]
    for file_path in file_paths:
        file_hash = hash_file(file_path)
        if file_hash in uploaded_hashes:
            print(f"File already processed: {file_path}")
            continue

        filename = os.path.basename(file_path)

        # PDF handling
        if file_path.endswith(".pdf"):
            docs = load_pdf(file_path)
            full_text = " ".join(doc["page_content"] for doc in docs)
            full_text = full_text.replace("\n", " ")
            chunks = chunk_text(full_text, chunk_size=1200)
            for idx, chunk in enumerate(chunks, start=1):
                data[0].append(f"{filename} - {idx}")
                data[1].append(chunk)
            print(f"Uploaded {filename} in {len(chunks)} chunks.")

        # TXT handling
        elif file_path.endswith(".txt"):
            with open(file_path, "r") as f:
                full_text = f.read()
            chunks = chunk_text(full_text, chunk_size=1200)
            for idx, chunk in enumerate(chunks, start=1):
                data[0].append(f"{filename} - {idx}")
                data[1].append(chunk)
            print(f"Uploaded {filename} in {len(chunks)} chunks.")

        else:
            print(f"Unsupported file type: {file_path}")
            continue

        uploaded_hashes.add(file_hash)

    return data


def insert_to_zilliz(collection, documents, embedding_model):
    """Insert documents into Zilliz DB."""
    embeddings = embedding_model.embed_documents([doc["page_content"] for doc in documents])
    primary_keys = list(range(len(embeddings)))
    data = [primary_keys, embeddings]

    collection.insert(data)
    collection.flush()
    print(f"Inserted {len(documents)} documents into Zilliz DB.")
