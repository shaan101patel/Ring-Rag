
# Custom prompt for the RAG app to summarize a document for upload
def summary_prompt_upload(doc_text):

    summary_prompt = (
        "Please provide a concise, high-level summary of the following document:\n\n"
        f"{doc_text}"
    )


    return summary_prompt


