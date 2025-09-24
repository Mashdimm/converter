# calculate_thread.py

from PyQt6.QtCore import QThread, pyqtSignal
from decimal import Decimal, InvalidOperation
from time import sleep

class CalculateThread(QThread):
    calculate_complete = pyqtSignal(list)

    def __init__(self, dict_csv, country_origin, rate_current, lst_for_csv_calc, error_message, callback, calculate_func):
        super().__init__()
        self.dict_csv = dict_csv
        self.country_origin = country_origin
        self.rate_current = rate_current
        self.lst_for_csv_calc = lst_for_csv_calc
        self.error_message = error_message
        self.callback = callback
        self.calculate = calculate_func  # новая ускоренная функция calculate

    def run(self):
        for i in range(len(self.dict_csv["Код товара"])):
            try:
                result_data = (i + 1, self.dict_csv["Код товара"][i])
                self.calculate_complete.emit(result_data)

                code = str(self.dict_csv["Код товара"][i])[0:6]
                mass = str(self.dict_csv["Вес Брутто"][i])

                try:
                    rate = Decimal(str(self.rate_current))
                    value = Decimal(str(self.dict_csv["Стоимость"][i])) * rate
                except (InvalidOperation, ValueError, TypeError) as e:
                    self.error_message.append(f"{self.dict_csv['Код товара'][i]}: Ошибка расчёта стоимости — {e}")
                    self.lst_for_csv_calc.append([self.dict_csv["Код товара"][i], "ERROR", "ERROR"])
                    continue

                try:
                    result = self.calculate(code, mass, str(value), self.country_origin)
                except Exception as e:
                    self.error_message.append(f"{self.dict_csv['Код товара'][i]}: Сбой вызова calculate — {e}")
                    self.lst_for_csv_calc.append([self.dict_csv["Код товара"][i], "ERROR", "ERROR"])
                    continue

                if result == "ERROR":
                    self.error_message.append(f"{self.dict_csv['Код товара'][i]}: Ошибка при расчёте")
                    self.lst_for_csv_calc.append([code, "ERROR", "ERROR"])
                else:
                    _, duty_rate, total_amount = result

                    try:
                        rate_value = float(duty_rate)
                        if rate_value < 1:
                            rate_for_csv = str(round(rate_value * 100, 3)).replace('.', ',') + '%'
                        else:
                            rate_for_csv = str(round(rate_value, 3)).replace('.', ',')
                    except (ValueError, TypeError):
                        rate_for_csv = "ERROR"

                    self.lst_for_csv_calc.append([
                        self.dict_csv['Код товара'][i],
                        rate_for_csv,
                        total_amount if total_amount else "ERROR"
                    ])

            except Exception as e:
                self.error_message.append(f"{self.dict_csv['Код товара'][i]}: Неизвестная ошибка — {e}")
                self.lst_for_csv_calc.append([self.dict_csv["Код товара"][i], "ERROR", "ERROR"])

        self.callback(self.lst_for_csv_calc)
