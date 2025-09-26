from flask import Flask, request, render_template_string
import os
from dotenv import load_dotenv
from gemini_client import send_prompt

load_dotenv()
MODEL = os.getenv("GEMINI_MODEL")
app = Flask(__name__)

history = []

HTML = """
<!doctype html>
<html>
<head
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
>
  <meta charset="utf-8">
  <title>Gemini Chat</title>
  <style>
    body {
      font-family: 'Inter', sans-serif;
      background-color: #2c2c2c;
      color: #fff;
      padding: 20px;
      max-width: 900px;
      margin: auto;
    }

    h1 {
      background: linear-gradient(90deg, #4f6cf4, #9b5de5);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-size: 2.5em;
      margin-bottom: 10px;
      font-weight: 700;
    }

    .model-label {
      color: #9b5de5;
      margin-bottom: 20px;
      display: block;
      font-weight: bold;
    }

    form {
      margin-bottom: 30px;
    }

    textarea {
      width: 100%;
      font-family: monospace;
      font-size: 1em;
      padding: 12px;
      border-radius: 12px;
      border: none;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      background-color: #3a3a3a;
      color: #fff;
      resize: vertical;
    }

    button {
      padding: 12px 24px;
      border-radius: 12px;
      border: none;
      background: linear-gradient(90deg, #4f6cf4, #9b5de5);
      color: #fff;
      font-size: 1em;
      cursor: pointer;
      transition: all 0.3s ease;
    }

    button:hover {
      box-shadow: 0 0 20px rgba(159, 80, 255, 0.6);
      transform: translateY(-2px);
    }

    pre {
      background-color: #3a3a3a;
      padding: 15px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      white-space: pre-wrap;
      color: #fff;
      font-family: monospace;
      font-size: 1em;
    }

    h2 {
      color: #4f6cf4;
      margin-bottom: 10px;
    }

    .history {
      margin-top: 30px;
    }

    .history pre {
      background-color: #2e2e2e;
      color: #fff;
    }
  </style>
</head>
<body>
  <h1>Gemini Chat</h1>
  <span class="model-label">Modelo: {{model}}</span>
  <form method="post">
    <textarea name="prompt" rows="6" placeholder="Digite seu prompt aqui...">{{prompt or ''}}</textarea><br><br>
    <button type="submit">Enviar</button>
  </form>
  {% if response %}
    <h2>Resposta</h2>
    <pre>{{response}}</pre>
  {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    global history
    prompt = ""
    response = ""

    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()
        if prompt:
            history.append({"role": "user", "content": prompt})

            try:
                response_text = send_prompt(history, prompt)
                response = response_text
                history.append({"role": "model", "content": response_text})
            except Exception as e:
                response = f"Erro: {e}"

    return render_template_string(HTML, prompt=prompt, response=response, history=history, model=MODEL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
