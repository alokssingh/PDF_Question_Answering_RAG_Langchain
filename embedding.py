from langchain_community.embeddings import OpenAIEmbeddings
from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.storage import InMemoryStore
from langchain_core.documents import Document
import uuid
from langchain_community.vectorstores import Chroma


def embeddings(text_summaries, table_summaries, texts, tables, openai_api_key):
    """
    Create embeddings for text chunks.

    Parameters:
        text_summaries (list): Summaries of text chunks.
        table_summaries (list): Summaries of table chunks.
        texts (list): List of text chunks.
        tables (list): List of table chunks.
        openai_api_key (str): API key for OpenAI service.

    Returns:
        object: Object containing text embeddings.
    """

    # Check if any of the input values are None
    if text_summaries is None or table_summaries is None or texts is None or tables is None:
        # Handle the case where summarization failed
        print("Summarization failed. Exiting.")
        return None

    # The vectorstore to use to index the child chunks
    vectorstore = Chroma(
        collection_name="summaries",
        embedding_function=OpenAIEmbeddings(openai_api_key=openai_api_key)
    )

    # The storage layer for the parent documents
    store = InMemoryStore()
    id_key = "doc_id"

    # The retriever (empty to start)
    retriever = MultiVectorRetriever(
        vectorstore=vectorstore,
        docstore=store,
        id_key=id_key,
    )

    # Add texts
    doc_ids = [str(uuid.uuid4()) for _ in texts]
    summary_texts = [Document(page_content=s, metadata={id_key: doc_ids[i]}) for i, s in enumerate(text_summaries)]
    retriever.vectorstore.add_documents(summary_texts)
    retriever.docstore.mset(list(zip(doc_ids, texts)))

    # Add tables
    table_ids = [str(uuid.uuid4()) for _ in tables]
    summary_tables = [Document(page_content=s, metadata={id_key: table_ids[i]}) for i, s in enumerate(table_summaries)]
    retriever.vectorstore.add_documents(summary_tables)
    retriever.docstore.mset(list(zip(table_ids, tables)))

    return retriever
