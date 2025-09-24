from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QFontDatabase
from dlg_settings import Ui_dlg_settings
from settings import get_path, set_path, reset_to_defaults, ensure_valid_path


from PyQt6 import QtWidgets, QtCore, QtGui
from dlg_settings import Ui_dlg_settings
from settings import get_path, set_path, reset_to_defaults, ensure_valid_path

import os

class SettingsDialog(Ui_dlg_settings, QtWidgets.QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(SettingsDialog, self).__init__(*args, **kwargs)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setupUi(self)
        QtGui.QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")

        self.load_paths()

        # Привязка кнопок "Обзор..."
        self.btn_csv_file.clicked.connect(lambda: self.browse_folder(self.lne_csv_file))
        self.btn_csv_razbivka.clicked.connect(lambda: self.browse_folder(self.lne_csv_razbivka))
        self.btn_calc.clicked.connect(lambda: self.browse_folder(self.lne_calc))
        self.btn_calc_for_lv.clicked.connect(lambda: self.browse_folder(self.lne_calc_for_lv))
        self.btn_csv_for_tardek.clicked.connect(lambda: self.browse_folder(self.lne_csv_for_tardek))
        self.btn_platezhka.clicked.connect(lambda: self.browse_folder(self.lne_platezhka))
        self.btn_platezhka_fito.clicked.connect(lambda: self.browse_folder(self.lne_platezhka_fito))
        #self.btn_pdf_exports.clicked.connect(lambda: self.browse_folder(self.lne_pdf_exports))
        #self.btn_xml_exports.clicked.connect(lambda: self.browse_folder(self.lne_xml_exports))

        # Привязка кнопок "Сохранить" и "Сброс"
        self.btn_save.clicked.connect(self.save_paths)
        self.btn_reset.clicked.connect(self.reset_paths)

    def load_paths(self):
        """Загрузка всех путей в поля формы."""
        try:
            self.lne_csv_file.setText(get_path("csv_file"))
            self.lne_csv_razbivka.setText(get_path("csv_razbivka"))
            self.lne_calc.setText(get_path("calc"))
            self.lne_calc_for_lv.setText(get_path("calc_for_lv"))
            self.lne_csv_for_tardek.setText(get_path("csv_for_tardek"))
            self.lne_platezhka.setText(get_path("platezhka"))
            self.lne_platezhka_fito.setText(get_path("platezhka_fito"))
            #self.lne_pdf_exports.setText(get_path("pdf_exports"))
            #self.lne_xml_exports.setText(get_path("xml_exports"))
        except Exception as e:
            self.show_error(str(e))

    def browse_folder(self, line_edit):
        """Открыть диалог выбора папки и записать в поле."""
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if folder:
            line_edit.setText(folder)

    def save_paths(self):
        """Сохранить все пути из полей."""
        try:
            paths = {
                "csv_file": self.lne_csv_file.text(),
                "csv_razbivka": self.lne_csv_razbivka.text(),
                "calc": self.lne_calc.text(),
                "calc_for_lv": self.lne_calc_for_lv.text(),
                "csv_for_tardek": self.lne_csv_for_tardek.text(),
                "platezhka": self.lne_platezhka.text(),
                "platezhka_fito": self.lne_platezhka_fito.text()

            }

            for key, path in paths.items():
                if not os.path.isdir(path):
                    self.show_error(f"Путь недействителен: {path}")
                    return
                set_path(key, path)

            self.accept()

        except Exception as e:
            self.show_error(str(e))

    def reset_paths(self):
        """Сброс всех путей к значениям по умолчанию."""
        reset_to_defaults()
        self.load_paths()

    def show_error(self, text: str, title="Ошибка"):
        message = QtWidgets.QMessageBox(self)
        message.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        message.setText(text)
        message.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        message.setWindowTitle(title)
        message.setStyleSheet('''
            background-color: rgb(35, 40, 49);
            color: white;
            font-size: 12pt;
            font-weight: 700;
            font-family: RussoOne-Regular;
            border: 2px solid gray;
            border-radius: 10px;
        ''')
        message.exec()
