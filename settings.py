from PyQt6.QtCore import QSettings, QStandardPaths, Qt
from PyQt6.QtWidgets import QCompleter, QLineEdit
import os

app_settings = QSettings("Alesta", "Convert")
default_documents_path = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation)

DEFAULT_PATHS = {
    "csv_file": os.path.join(default_documents_path),
    "csv_razbivka": os.path.join(default_documents_path),
    "calc": os.path.join(default_documents_path),
    "calc_for_lv": os.path.join(default_documents_path),
    "csv_for_tardek": os.path.join(default_documents_path),
    "platezhka": os.path.join(default_documents_path),
    "platezhka_fito": os.path.join(default_documents_path)
}

def get_path(key: str) -> str:
    return app_settings.value(f"path/{key}", DEFAULT_PATHS.get(key, "C:/"))

def set_path(key: str, value: str) -> None:
    app_settings.setValue(f"path/{key}", value)

def ensure_valid_path(key: str) -> str:

    path = get_path(key)
    if not os.path.isdir(path):
        return DEFAULT_PATHS.get(key, "C:/")
    return path

def get_all_paths() -> dict:
    return {key: get_path(key) for key in DEFAULT_PATHS}

def reset_to_defaults():
    for key, path in DEFAULT_PATHS.items():
        set_path(key, path)

def save_to_history(key: str, value: str):
    """
    Сохраняет значение в историю, если оно новое.
    """
    history = app_settings.value(f"history/{key}", [])
    if isinstance(history, str):  # если только одно значение
        history = [history]

    if value and value not in history:
        history.append(value)
        app_settings.setValue(f"history/{key}", history)


def load_history(key: str) -> list[str]:
    """
    Загружает историю значений.
    """
    history = app_settings.value(f"history/{key}", [])
    if isinstance(history, str):
        return [history]
    return history


def setup_completer(lineedit: QLineEdit, key: str):
    """
    Устанавливает QCompleter с автозаполнением и стилем.
    """
    history = load_history(key)
    completer = QCompleter(history)
    completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
    completer.setFilterMode(Qt.MatchFlag.MatchContains)  # показывает по вхождению, не только с начала

    # Установка стиля на popup (выпадающий список)
    popup = completer.popup()
    popup.setStyleSheet("""
        QListView {
            background-color: #2e2e2e;
            color: white;
            border: 1px solid #444444;
            padding: 4px;
            font-size: 12pt;
            font-weight: bold;
            font-family: RussoOne-Regular;
            selection-background-color: #4e4e4e;
            selection-color: white;
            border-radius: 5px;
        }
    """)

    lineedit.setCompleter(completer)