import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Azure Function'ın URL'si - Azure'da App Service Configuration kısmında
# ortam değişkeni (environment variable) olarak ayarlanacak.
# Örnek: https://<function-app-adiniz>.azurewebsites.net/api/GetRandomQuote
FUNCTION_URL = os.environ.get(
    "QUOTE_FUNCTION_URL",
    "http://localhost:7071/api/GetRandomQuote"  # yerel test için varsayılan
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/quote")
def get_quote():
    """Web App, Azure Function'ı sunucu tarafında çağırır (CORS sorunu olmaz)."""
    try:
        response = requests.get(FUNCTION_URL, timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": f"Function çağrısı başarısız: {str(e)}"}), 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
