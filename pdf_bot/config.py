import os

base_url = os.environ.get('OLLAMA_API_BASE_URL', "http://host.docker.internal:11434")
if base_url.endswith('/'):
    base_url = base_url.rstrip('/')


class Config:
    MODEL = os.environ.get('MODEL', "snickers8523/llama3-taide-lx-8b-chat-alpha1-q4-0")
    EMBEDDING_MODEL_NAME = os.environ.get('EMBEDDING_MODEL_NAME', "BAAI/bge-large-en-v1.5")
    OLLAMA_API_BASE_URL = base_url
    HUGGING_FACE_EMBEDDINGS_DEVICE_TYPE = os.environ.get('HUGGING_FACE_EMBEDDINGS_DEVICE_TYPE',
                                                         "cpu")
