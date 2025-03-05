import os
import gradio as gr
import requests
import google.auth
import google.auth.transport.requests
import logging


def process_pdf(file):
    """
    Uploads the PDF to the GenAI backend and returns the result.
    """
    credentials, _ = google.auth.default()
    authorized_session = google.auth.transport.requests.AuthorizedSession(credentials)
    backend_url = os.getenv("BACKEND_URL")

    if file is None:
        return "Please upload a PDF file."

    try:
        files = {"file": ("uploaded_file.pdf", open(file.name, "rb"), "application/pdf")}
        response = authorized_session.post(
            url=f"{backend_url}/predict",
            files=files,
            allow_redirects=False,
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()

    except requests.exceptions.RequestException as e:
        return f"Error connecting to processing service: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

ui = gr.Interface(
    fn=process_pdf,
    inputs=gr.File(file_types=["file"], label="Upload Research Paper"),
    outputs="json",
    title="AI-Powered Research Paper Analyzer",
    description="Upload a research paper to extract a summary & key topics discussed."
)

ui.launch(server_name="0.0.0.0", server_port=8080, share=True) #Cloud Run expects port 8080
