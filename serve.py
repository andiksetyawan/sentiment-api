# serve.py
from japronto import Application
from sentistrength_id import sentistrength

import json

config = dict()
config["negation"] = True
config["booster"] = True
config["ungkapan"] = True
config["consecutive"] = True
config["repeated"] = True
config["emoticon"] = True
config["question"] = True
config["exclamation"] = True
config["punctuation"] = True
senti = sentistrength(config)

def get_sentiment(request):
    """Handles API request"""
    if request.method == 'GET':
        tutorial = (
            "Lakukan POST dengan parameter <b>text</b>"
            "&nbsp;ke route <b>/</b> untuk mendapatkan hasil analisis"
        )
        return request.Response(text=tutorial, code=400)

    if request.method == 'POST':
        if "text" in request.form:
            text = request.form["text"]
            data = senti.main(text)
            return request.Response(text=json.dumps(data), code=200)
        else:
            return request.Response("'text' param not found", code=500)

app = Application()
app.router.add_route('/', get_sentiment)
app.run(port=8000, debug=False)
