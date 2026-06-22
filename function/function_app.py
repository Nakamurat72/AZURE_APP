import azure.functions as func
import json
import random
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

QUOTES = [
    {"text": "Hayatta en hakiki mürşit ilimdir.", "author": "Mustafa Kemal Atatürk"},
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
    {"text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"text": "Simplicity is the ultimate sophistication.", "author": "Leonardo da Vinci"},
    {"text": "The journey of a thousand miles begins with one step.", "author": "Lao Tzu"},
    {"text": "Whether you think you can or you think you can't, you're right.", "author": "Henry Ford"},
    {"text": "Success is not final, failure is not fatal.", "author": "Winston Churchill"},
    {"text": "The best time to plant a tree was 20 years ago. The second best time is now.", "author": "Chinese Proverb"},
    {"text": "What we think, we become.", "author": "Buddha"},
]


@app.route(route="GetRandomQuote", methods=["GET"])
def GetRandomQuote(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("GetRandomQuote function triggered.")

    quote = random.choice(QUOTES)

    return func.HttpResponse(
        json.dumps(quote, ensure_ascii=False),
        status_code=200,
        mimetype="application/json",
        headers={"Access-Control-Allow-Origin": "*"},
    )
