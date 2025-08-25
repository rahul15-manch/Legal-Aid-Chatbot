import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

BACKEND = os.getenv("LLM_BACKEND", "openai").lower()

# OpenAI
from openai import OpenAI
_openai_client = None

def _get_openai_client():
    global _openai_client
    if _openai_client is None:
        _openai_client = OpenAI()
    return _openai_client

def llm_complete(prompt: str, system: Optional[str] = None, max_tokens: int = 512, temperature: float = 0.2) -> str:
    if BACKEND == "openai":
        client = _get_openai_client()
        model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        msgs = []
        if system:
            msgs.append({"role": "system", "content": system})
        msgs.append({"role": "user", "content": prompt})
        resp = client.chat.completions.create(model=model, messages=msgs, temperature=temperature, max_tokens=max_tokens)
        return resp.choices[0].message.content.strip()
    else:
        # HF local transformers (text2text, e.g., flan-t5-base)
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
        import torch
        model_name = os.getenv("HF_LOCAL_MODEL", "google/flan-t5-base")
        max_new_tokens = int(os.getenv("HF_MAX_NEW_TOKENS", 384))
        temperature = float(os.getenv("HF_TEMPERATURE", 0.2))
        device = 0 if torch.cuda.is_available() else -1
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=temperature > 0,
            temperature=temperature,
        )
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
