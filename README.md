# Aplicação de Integração com LLM

Projeto em **Python** que conecta ao modelo `gemini-2.5-flash` da Google Gemini,
envia prompts, mantém histórico de conversa e exibe respostas.

Inclui:

- `cli_app.py` — aplicação de linha de comando (console) com histórico.
- `web_app.py` — aplicação web mínima em Flask com interface moderna e histórico.
- `gemini_client.py` — cliente reutilizável para chamar a API Gemini.
- `.env.example` — configuração de modelo e API Key.
- `requirements.txt` — dependências do projeto.

---

## Pré-requisitos

- Python 3.10+
- Conta Google e API Key do Gemini configurada na variável de ambiente `GEMINI_API_KEY`.

---

## Setup rápido

### Linux / macOS
```bash
cd aplicacao_integracao_ia  # ou a pasta onde o seu projeto está
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edite .env se precisar:
# GEMINI_API_KEY=<sua_api_key>
# GEMINI_MODEL=gemini-2.5-flash
```

### Windows (Prompt de Comando)
```bat
cd aplicacao_integracao_ia
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
rem edite .env se precisar:
rem GEMINI_API_KEY=<sua_api_key>
rem GEMINI_MODEL=gemini-2.5-flash
```
### Windows (PowerShell)
```powershell
cd aplicacao_integracao_ia
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
# edite .env se precisar
# Obs.: .env deve conter pelo menos:
# GEMINI_API_KEY=coloque_sua_api_key_aqui
# GEMINI_MODEL=gemini-2.5-flash
```


## Rodar CLI

```bash
python cli_app.py
```
- Digite seu prompt e veja a resposta do Gemini.

- Digite sair, exit ou quit para encerrar.

- O histórico de mensagens é mantido enquanto o CLI estiver aberto.

## Rodar Web (Flask)

```bash
python web_app.py
```
- Abra http://localhost:5000 no navegador e use o formulário.

- O resposta da conversa aparece abaixo do formulário, permitindo continuidade de contexto.


## Estrutura do projeto

```bash
.
├── cli_app.py          # CLI interativa
├── web_app.py          # WebApp Flask
├── gemini_client.py    # Cliente Gemini com histórico
├── requirements.txt
├── .env.example
└── README.md
```
