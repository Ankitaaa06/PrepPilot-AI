from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def create_vector_store(chunks):

    if not chunks:
        return None

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    documents = [
        Document(page_content=chunk)
        for chunk in chunks
        if chunk.strip()
    ]

    if not documents:
        return None

    vector_store = FAISS.from_documents(
        documents,
        embeddings
    )

    vector_store.save_local("vectorstore")

    return vector_store


def load_vector_store():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )