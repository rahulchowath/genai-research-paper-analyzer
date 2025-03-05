import os
import tempfile
from langchain_google_vertexai import VertexAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.document_loaders import PyPDFLoader
from src.prompts import prompt_generate_text


def research_paper_extraction(
    pdf_file,
    llm="gemini-2.0-flash",
):
    """
    Reads a research paper PDF, extracts text, and identifies contextualized entities.

    Args:
        pdf_content (str): PDF content.
        llm (str): The Vertex AI model to use.

    Returns:
        list: A list of dictionaries, where each dictionary represents an entity and its context.
    """
    # Create a temporary file to store the uploaded file
    temp_file_path = f"/tmp/{pdf_file.filename}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(pdf_file.file.read())

    # Load the temp pdf file
    loader = PyPDFLoader(temp_file_path)
    documents = loader.load()
    text = "\n".join([doc.page_content for doc in documents])

    llm = VertexAI(
        model_name=llm,
        project=os.getenv("PROJECT"),
        location=os.getenv("REGION"),
    )
    parser = JsonOutputParser()

    chain = {"text": lambda x: x} | prompt_generate_text | llm | parser

    result = chain.invoke(text)

    return result
