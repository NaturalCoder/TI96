import requests
import re

def chat(prompt, model="joao"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
        #"options": { "raw": True }  # Opcional: evita tags <think>
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Verifica erros HTTP
        return remove_think_tag(response.json()["response"])
    except Exception as e:
        print(f"Erro na API: {e}")
        return ""

def remove_think_tag(response):
    return re.sub(r'<think>.*?</think>\n?', '', response, flags=re.DOTALL)

# Loop de debate
if __name__ == "__main__":
    r2 = "Do que vc gosta"
    for i in range(1, 10):
        r1 = chat(r2, "sw")
        print(f"SW: {r1}")
        r2 = chat(r1, "st")
        print(f"ST: {r2}")
        