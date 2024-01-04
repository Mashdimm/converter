import googletrans
from googletrans import Translator

translator = Translator()

r = translator.translate("Папа", dest='pl')
print(r.text)
