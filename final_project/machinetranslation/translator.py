import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
model_id = 'en-fr''fr-en'

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='{2018-05-01}',
    authenticator=authenticator

#Translate
def englishToFrench(englishText):
translation = language_translator.translate(
    text='Hello',
    model_id='en-fr').get_result() 
    return frenchText
def englishToFrench(englishText):
translation = language_translator.translate(
    text='Bonjour',
    model_id='fr-en').get_result()
    return frenchText
#Print Results 
print(json.dumps(translation, indent=2, ensure_ascii=False))
  
