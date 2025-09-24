from googletrans import Translator
from time import sleep


translator = Translator()

def translate_list(lst, src, dest, delay=0.2):
    translated_texts = []
    try:
        for item in lst:
            try:

                translated = translator.translate(item, src=src, dest=dest)
                translated_texts.append(translated.text.upper().strip())

                sleep(delay)
            except Exception as item_error:
                translated_texts.append(item)
                print(f"Ошибка перевода строки '{item}': {item_error}")
    except Exception as e:
        print(e)
    return translated_texts

