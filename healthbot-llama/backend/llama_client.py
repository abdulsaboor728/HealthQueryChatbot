import requests

class LlamaClient:
    def __init__(self, base_url="http://localhost:11434", model="llama3.2:3b"):
        self.base_url = base_url
        self.model = model

    def chat(self, system_prompt, user_message):
        url = f"{self.base_url}/api/chat"

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            "stream": False
        }

        r = requests.post(url, json=payload, timeout=600)

        r.raise_for_status()

        data = r.json()

        return data["message"]["content"]