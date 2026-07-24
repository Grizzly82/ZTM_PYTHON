#This program will translate a given text into a different language using the Google Translate API.
#using the googletrans library, we can easily translate text from one language to another.
#external file 

from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='it')  # Change 'ja' to the desired target language code (e.g., 'es' for Spanish, 'fr' for French, etc.)
try:
    with open('my_translator.txt', 'r') as file:
        text = file.read()
        translated_text = translator.translate(text)
        print(f"Original Text: {text}")
        print(f"Translated Text: {translated_text}")
except FileNotFoundError:
    print("The file 'my_translator.txt' was not found. Please make sure the file exists in the same directory as this script.")