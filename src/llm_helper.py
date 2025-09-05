# llm_helper.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def ask_mistral(prompt: str) -> str:
    """
    Essaie d'abord en local avec Ollama,
    puis bascule sur Hugging Face si ça échoue.
    """
    # --- essai local ---
    try:
        import ollama
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    except Exception:
        # --- fallback Hugging Face ---
        hf_token = os.getenv("HF_API_KEY")
        if not hf_token:
            return "❌ Clé Hugging Face manquante. Ajoute HF_API_KEY dans ton .env."

        try:
            # Choisis le modèle Mistral sur Hugging Face (exemple)
            model_id = "mistralai/mistral-7b-instruct"
            headers = {
                "Authorization": f"Bearer {hf_token}",
                "Content-Type": "application/json"
            }
            payload = {"inputs": prompt}

            url = f"https://api-inference.huggingface.co/models/{model_id}"
            response = requests.post(url, headers=headers, json=payload)
            response_json = response.json()

            # Hugging Face retourne souvent une liste de dicts [{"generated_text": "..."}]
            if isinstance(response_json, list) and "generated_text" in response_json[0]:
                return response_json[0]["generated_text"]
            else:
                return str(response_json)

        except Exception as e:
            return f"❌ Erreur Hugging Face : {e}"
