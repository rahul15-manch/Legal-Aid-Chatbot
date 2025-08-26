# llm_providers.py
import os
from dotenv import load_dotenv

load_dotenv()

# ======================================================
# OpenAI Provider
# ======================================================
from openai import OpenAI

_openai_client = None


def _get_openai_client():
    """Singleton OpenAI client."""
    global _openai_client
    if _openai_client is None:
        _openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return _openai_client


def _openai_complete(prompt: str) -> str:
    client = _get_openai_client()
    resp = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content


# ======================================================
# Hugging Face (Local transformers)
# ======================================================
from transformers import pipeline

_hf_generator = None


def _get_hf_pipeline():
    """Singleton HuggingFace local pipeline."""
    global _hf_generator
    if _hf_generator is None:
        print("Loading Hugging Face local model... (one-time load)")
        _hf_generator = pipeline(
            "text2text-generation",
            model=os.getenv("HF_LOCAL_MODEL", "google/flan-t5-base"),
            device_map="auto",  # uses GPU if available
        )
    return _hf_generator


def _hf_local_complete(prompt: str) -> str:
    generator = _get_hf_pipeline()
    outputs = generator(prompt, max_length=200, num_return_sequences=1)
    return outputs[0]["generated_text"]


# ======================================================
# Hugging Face Hub (Hosted API)
# ======================================================
from huggingface_hub import InferenceClient

_hf_hub_client = None


def _get_hf_hub_client():
    """Singleton HuggingFace Hub client."""
    global _hf_hub_client
    if _hf_hub_client is None:
        model = os.getenv("HF_HUB_MODEL", "bigscience/bloom-560m")
        token = os.getenv("HF_API_KEY")
        _hf_hub_client = InferenceClient(model=model, token=token)
    return _hf_hub_client


def _hf_hub_complete(prompt: str) -> str:
    client = _get_hf_hub_client()
    result = client.text_generation(prompt, max_new_tokens=200)
    return result


# ======================================================
# Main Router
# ======================================================
def llm_complete(prompt: str) -> str:
    backend = os.getenv("LLM_BACKEND", "openai")

    if backend == "openai":
        return _openai_complete(prompt)
    elif backend == "hf-local":
        return _hf_local_complete(prompt)
    elif backend == "hf-hub":
        return _hf_hub_complete(prompt)
    else:
        raise ValueError(f"Unknown LLM_BACKEND: {backend}")
