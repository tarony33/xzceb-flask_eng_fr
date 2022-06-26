from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translation = language_translator.translate(
    text='Hello',
    model_id='en-fr').get_result() 
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translation = language_translator.translate(
    text='Bonjour',
    model_id='fr-en').get_result()
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
   print(json.dumps(translation, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
