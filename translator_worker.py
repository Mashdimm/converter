from PyQt6.QtCore import QObject, pyqtSignal
from deep_translator import GoogleTranslator
from time import sleep




class TranslatorWorker(QObject):
    progress = pyqtSignal(str)
    finished = pyqtSignal(list)

    def __init__(self, texts, src='ru', dest='en', delay=0.2):
        super().__init__()
        self.texts = texts
        self.src = src
        self.dest = dest
        self.delay = delay
    def run(self):
        translator = GoogleTranslator(source=self.src, target=self.dest)
        result = []
        total = len(self.texts)

        for i, item in enumerate(self.texts, 1):
            try:
                translated = translator.translate(item).upper().strip()
                self.progress.emit(f'{i}. {item} -> {translated}')
                result.append(translated)
            except Exception as e:
                result.append(e)
                self.progress.emit(f'Ошибка перевода строки {i}. {item}: {e}')
            sleep(self.delay)
        self.finished.emit(result)


