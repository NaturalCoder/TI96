import requests, re

def chat_with_ollama(prompt, model="Deadpool"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    return remove_think_tag(response.json()["response"])

def remove_think_tag(response):
    return re.sub(r'<think>.*?</think>\n?', '', response, flags=re.DOTALL)

# Teste
resposta = chat_with_ollama("Quem e seu pai de mentira")
print(resposta)