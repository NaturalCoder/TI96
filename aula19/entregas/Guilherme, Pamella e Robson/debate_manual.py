import requests
import re

def chat(prompt, model="joao"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return remove_think_tag(response.json()["response"])
    except Exception as e:
        print(f"Erro na API: {e}")
        return ""

def remove_think_tag(response):
    return re.sub(r'<think>.*?</think>\n?', '', response, flags=re.DOTALL)

# Debate: iPhone vs Android
if __name__ == "__main__":
    r2 = """Sou a Ana, usuária fiel de iPhone. A experiência do iOS é incomparável: fluidez, segurança e integração com todo o ecossistema Apple. 
    Android vive travando e cada marca inventa um sistema diferente. Quero ver como você vai defender isso."""

    for i in range(1, 6):
        r1 = chat(r2, "ana")
        print(f"\n Ana (iPhone): {r1}")
        r2 = chat(r1, "carlos")
        print(f"\nCarlos (Android): {r2}")
