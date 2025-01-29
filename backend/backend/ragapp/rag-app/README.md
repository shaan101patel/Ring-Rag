# RAG Application

## Overview
The RAG (Retrieval-Augmented Generation) application is designed to facilitate the retrieval and processing of documents using advanced language models. This application allows users to upload multiple files, which are then processed to extract relevant information and generate responses based on user queries.

## Project Structure
```
rag-app
├── src
│   ├── main.py          # Main logic for loading, processing, and querying documents
│   ├── file_upload.py   # Handles file uploads from the user's computer
│   ├── utils
│   │   └── __init__.py  # Utility functions for various tasks
│   └── types
│       └── index.py     # Custom types and interfaces for type safety
├── requirements.txt     # Project dependencies
└── README.md            # Documentation for the project
```

## Installation
To set up the RAG application, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd rag-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Start the application by running the main script:
   ```
   python src/main.py
   ```

2. Use the file upload feature to upload multiple documents from your computer. The application will process these documents and allow you to query them.

3. You can ask questions related to the uploaded documents, and the application will provide relevant answers based on the content.

## Changes going forward

The Vector store need to be hosted.
the way I vectorize docuemnts needs to change rn we take everything and put it into one string and the chunk it, we need to seperate it and incluude meta tags hopefully the API for the new vector store will help

## Contributing
Contributions are welcome! If you would like to contribute to the project, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.