from iso639 import languages
from langdetect import *
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/lg')
def language_detection():
    # Lese den übergebenen Text aus dem GET-Parameter 'id' ein
    text = request.args.get("id")
    # Verwende langdetect, um die Sprache des Textes zu erkennen
    language = detect_langs(text)
    best = language[0]
    # Verwende iso-639, um den vollständigen Namen und die Kurzform der Sprache zu bestimmen
    language_short = best.lang
    language_name = languages.get(part1=language_short)

    # Setze die Trefferwahrscheinlichkeit
    prob = best.prob * 100
    is_reliable = best.prob > 0.5
    # Erstelle das JSON-Objekt mit den Ergebnissen
    result = {
        "reliable": is_reliable,
        "language": language_name.name,
        "short": language_short,
        "prob": prob
    }

    # Erstelle eine Antwort-Objekt und füge die Ergebnisse als JSON-Objekt hinzu
    response = jsonify(result)
    # Gib die Antwort zurück
    return response

if __name__ == '__main__':
    app.run(debug=False)