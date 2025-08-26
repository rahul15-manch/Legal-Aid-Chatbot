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


def _get_hf_hub_client(model=None):
    """Singleton HuggingFace Hub client."""
    global _hf_hub_client
    if _hf_hub_client is None or model is not None:
        model = model or os.getenv("HF_HUB_MODEL", "google/flan-t5-small")
        token = os.getenv("HF_API_KEY")
        _hf_hub_client = InferenceClient(model=model, token=token)
    return _hf_hub_client


def _hf_hub_complete(prompt: str) -> str:
    model = os.getenv("HF_HUB_MODEL", "google/flan-t5-small")
    hf_token = os.getenv("HF_API_KEY")

    client = _get_hf_hub_client(model=model)

    print(f">>> Sending prompt to Hugging Face Hub model: {model}")

    try:
        response = client.text_generation(
            prompt,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7,
        )

        if isinstance(response, str):
            return response.strip()
        elif isinstance(response, dict):
            return response.get("generated_text", "").strip()
        else:
            return "[HF Hub Error: Unexpected response type]"

    except Exception as e:
        print(f"[HF Hub Error on model {model}: {str(e)}]")

        # 🔄 Fallback to a safe default
        fallback_model = "google/flan-t5-small"
        print(f">>> Falling back to Hugging Face Hub model: {fallback_model}")
        try:
            fallback_client = _get_hf_hub_client(model=fallback_model)
            response = fallback_client.text_generation(
                prompt,
                max_new_tokens=200,
                do_sample=True,
                temperature=0.7,
            )
            return response.strip() if isinstance(response, str) else response.get("generated_text", "")
        except Exception as e2:
            return f"[HF Hub Fallback Error: {str(e2)}]"


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
