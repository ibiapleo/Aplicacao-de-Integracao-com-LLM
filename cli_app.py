from dotenv import load_dotenv
import os
from gemini_client import send_prompt

def main():
    load_dotenv()
    model = os.getenv("GEMINI_MODEL")

    print(f"Usando modelo: {model}\n")
    print("Digite seu prompt (ou 'sair' para encerrar):")

    history = []

    while True:
        prompt = input("> ").strip()
        if prompt.lower() in ("sair", "exit", "quit"):
            print("Encerrando.")
            break

        history.append({"role": "user", "content": prompt})

        try:
            resposta = send_prompt(history, prompt)

            history.append({"role": "model", "content": resposta})
            
            print("\nResposta do Gemini:\n")
            print(resposta)
            print("\n---\n")
        except Exception as e:
            print(f"[Erro] {e}")

if __name__ == "__main__":
    main()
