import requests

class RestClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def check_language(self, text):
        # Sende eine Anfrage an den Webservice mit dem übergebenen Text
        response = requests.get(f"{self.base_url}/lg?id={text}")

        # Verarbeite die Antwort und liefere die Ergebnisse zurück
        print(response.status_code)
        print(response.content)
        result = response.json()
        return result['reliable'], result['language'], result['short'], result['prob']