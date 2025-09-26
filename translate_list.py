from deep_translator import GoogleTranslator
from time import sleep



def translate_list(lst, src='ru', dest='en', delay=0.2):
    translated_texts = []
    translator = GoogleTranslator(source=src, target=dest, delay=delay)
    try:
        for item in lst:
            try:

                translated = translator.translate(item)
                translated_texts.append(translated.upper().strip())
                print(f"Переведено: {translated_texts}")


            except Exception as item_error:
                translated_texts.append(item)
                print(f"Ошибка перевода строки '{item}': {item_error}")
    except Exception as e:
        print(e)
    return translated_texts

