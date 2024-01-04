import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QMessageBox, QTableWidget, \
    QTableWidgetItem, QProgressDialog, QProgressBar, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QFontDatabase, QIcon
from PyQt6.QtCore import QDate, Qt, QObject, QThread, pyqtSignal
from convert import Ui_MainWindow
from googletrans import Translator
from lang import Ui_Dialog
from qauntity_cmr import Ui_Qauntity_CMR
from one_cmr import Ui_one_cmr
from consignor_dispatch import Ui_consignor_dispatch
from consignor_dest import Ui_consignor_destination
from qauntity_goods import Ui_Qauntity_goods
from calc_tax import Ui_calc_tax
from current_inv import Ui_Current_inv
from table_rate import Ui_table_rate
from progress import Ui_Progress_calc
from rate_json import rates_from_json

import csv
import datetime
from time import perf_counter, sleep
import payment
from calculate import calculate
import xls_for_lv

language = ['af, Afrikaans', 'sq, Albanian', 'am, Amharic', 'ar, Arabic', 'hy, Armenian', 'az, Azerbaijani',
            'eu, Basque', 'be, Belarusian', 'bn, Bengali', 'bs, Bosnian', 'bg, Bulgarian', 'ca, Catalan',
            'ceb, Cebuano', 'ny, Chichewa', 'zh-cn, Chinese (simplified)', 'zh-tw, Chinese (traditional)',
            'co, Corsican', 'hr, Croatian', 'cs, Czech', 'da, Danish', 'nl, Dutch', 'en, English', 'eo, Esperanto',
            'et, Estonian', 'tl, Filipino', 'fi, Finnish', 'fr, French', 'fy, Frisian', 'gl, Galician', 'ka, Georgian',
            'de, German', 'el, Greek', 'gu, Gujarati', 'ht, Haitian creole', 'ha, Hausa', 'haw, Hawaiian', 'iw, Hebrew',
            'he, Hebrew', 'hi, Hindi', 'hmn, Hmong', 'hu, Hungarian', 'is, Icelandic', 'ig, Igbo', 'id, Indonesian',
            'ga, Irish', 'it, Italian', 'ja, Japanese', 'jw, Javanese', 'kn, Kannada', 'kk, Kazakh', 'km, Khmer',
            'ko, Korean', 'ku, Kurdish (kurmanji)', 'ky, Kyrgyz', 'lo, Lao', 'la, Latin', 'lv, Latvian',
            'lt, Lithuanian', 'lb, Luxembourgish', 'mk, Macedonian', 'mg, Malagasy', 'ms, Malay', 'ml, Malayalam',
            'mt, Maltese', 'mi, Maori', 'mr, Marathi', 'mn, Mongolian', 'my, Myanmar (burmese)', 'ne, Nepali',
            'no, Norwegian', 'or, Odia', 'ps, Pashto', 'fa, Persian', 'pl, Polish', 'pt, Portuguese', 'pa, Punjabi',
            'ro, Romanian', 'ru, Russian', 'sm, Samoan', 'gd, Scots gaelic', 'sr, Serbian', 'st, Sesotho', 'sn, Shona',
            'sd, Sindhi', 'si, Sinhala', 'sk, Slovak', 'sl, Slovenian', 'so, Somali', 'es, Spanish', 'su, Sundanese',
            'sw, Swahili', 'sv, Swedish', 'tg, tajik', 'ta, Tamil', 'te, Telugu', 'th, thai', 'tr, Turkish',
            'uk, Ukrainian', 'ur, Urdu', 'ug, Uyghur', 'uz, Uzbek', 'vi, Vietnamese', 'cy, Welsh', 'xh, Xhosa',
            'yi, yiddish', 'yo, Yoruba', 'zu, zulu']

lst_country = ['AD - Andorra', 'AE - United Arab Emirates', 'AF - Afghanistan', 'AL - Albania', 'AM - Armenia',
               'AO - Angola', 'AQ - Antarctica', 'AR - Argentina', 'AT - Austria', 'AU - Australia', 'AZ - Azerbaijan',
               'BA - Bosnia and Herzegovina', 'BD - Bangladesh', 'BE - Belgium', 'BF - Burkina Faso', 'BG - Bulgaria',
               'BH - Bahrain', 'BI - Burundi', 'BJ - Benin', 'BN - Brunei Darussalam',
               'BO - Bolivia, Plurinational State of', 'BR - Brazil', 'BT - Bhutan', 'BW - Botswana', 'BY - Belarus',
               'BZ - Belize', 'CA - Canada', 'CD - Congo, the Democratic Republic of the',
               'CF - Central African Republic', 'CG - Congo', 'CH - Switzerland', "CI - Cote d'Ivoire", 'CL - Chile',
               'CM - Cameroon', 'CN - China', 'CO - Colombia', 'CR - Costa Rica', 'CU - Cuba', 'CV - Cape Verde',
               'CY - Cyprus', 'CZ - Czech Republic', 'DE - Germany', 'DJ - Djibouti', 'DK - Denmark',
               'DO - Dominican Republic', 'DZ - Algeria', 'EC - Ecuador', 'EE - Estonia', 'EG - Egypt',
               'EH - Western Sahara', 'ER - Eritrea', 'ES - Spain', 'ET - Ethiopia', 'FI - Finland', 'FR - France',
               'GA - Gabon', 'GB - United Kingdom', 'GE - Georgia', 'GF - French Guiana', 'GH - Ghana',
               'GL - Greenland', 'GM - Gambia', 'GN - Guinea', 'GQ - Equatorial Guinea', 'GR - Greece',
               'GT - Guatemala', 'GU - Guam', 'GW - Guinea-Bissau', 'GY - Guyana', 'HK - Hong Kong', 'HN - Honduras',
               'HR - Croatia', 'HT - Haiti', 'HU - Hungary', 'ID - Indonesia', 'IE - Ireland', 'IL - Israel',
               'IN - India', 'IQ - Iraq', 'IR - Iran, Islamic Republic of', 'IS - Iceland', 'IT - Italy',
               'JM - Jamaica', 'JO - Jordan', 'JP - Japan', 'KE - Kenya', 'KG - Kyrgyzstan', 'KH - Cambodia',
               "KP - Korea, Democratic People's Republic of", 'KR - Korea, Republic of', 'KW - Kuwait',
               'KZ - Kazakhstan', "LA - Lao People's Democratic Republic", 'LB - Lebanon', 'LI - Liechtenstein',
               'LK - Sri Lanka', 'LR - Liberia', 'LS - Lesotho', 'LT - Lithuania', 'LU - Luxembourg', 'LV - Latvia',
               'LY - Libyan Arab Jamahiriya', 'MA - Morocco', 'MC - Monaco', 'MD - Moldova, Republic of',
               'ME - Montenegro', 'MG - Madagascar', 'MK - Macedonia, the former Yugoslav Republic of', 'ML - Mali',
               'MM - Myanmar', 'MN - Mongolia', 'MO - Macao', 'MR - Mauritania', 'MT - Malta', 'MU - Mauritius',
               'MV - Maldives', 'MW - Malawi', 'MX - Mexico', 'MY - Malaysia', 'MZ - Mozambique', 'NA - Namibia',
               'NE - Niger', 'NG - Nigeria', 'NI - Nicaragua', 'NL - Netherlands', 'NO - Norway', 'NP - Nepal',
               'NZ - New Zealand', 'OM - Oman', 'PA - Panama', 'PE - Peru', 'PG - Papua New Guinea', 'PH - Philippines',
               'PK - Pakistan', 'PL - Poland', 'PR - Puerto Rico', 'PS - Palestine, State of', 'PT - Portugal',
               'PY - Paraguay', 'RE - Reunion', 'RO - Romania', 'RS - Serbia', 'RU - Russian Federation', 'RW - Rwanda',
               'SA - Saudi Arabia', 'SC - Seychelles', 'SD - Sudan', 'SE - Sweden', 'SG - Singapore',
               'SH - Saint Helena, Ascension and Tristan da Cunha', 'SI - Slovenia', 'SK - Slovakia',
               'SL - Sierra Leone', 'SM - San Marino', 'SN - Senegal', 'SO - Somalia', 'SR - Suriname',
               'ST - Sao Tome and Principe', 'SV - El Salvador', 'SY - Syrian Arab Republic', 'SZ - Swaziland',
               'TD - Chad', 'TG - Togo', 'TH - Thailand', 'TJ - Tajikistan', 'TL - Timor-Leste', 'TM - Turkmenistan',
               'TN - Tunisia', 'TR - Turkey', 'TW - Taiwan, Province of China', 'TZ - Tanzania, United Republic of',
               'UA - Ukraine', 'UG - Uganda', 'US - United States', 'UY - Uruguay', 'UZ - Uzbekistan',
               'VA - Holy See (Vatican City State)', 'VE - Venezuela, Bolivarian Republic of', 'VN - Viet Nam',
               'YE - Yemen', 'YT - Mayotte', 'ZA - South Africa', 'ZM - Zambia', 'ZW - Zimbabwe']

lst_current = ['AED - Дирхам', 'AFN - Афгани', 'ALL - Албанский лек', 'AMD - Армянский драм',
               'ANG - Нидерландский антильский гульден', 'AOA - Ангольская кванза', 'ARS - Аргентинское песо',
               'AUD - Австралийский доллар', 'AWG - Арубанский флорин', 'AZN - Азербайджанский манат',
               'BAM - Конвертируемая марка Боснии и Герцеговины', 'BBD - Барбадосский доллар',
               'BDT - Бангладешская така', 'BGN - Болгарский лев', 'BHD - Бахрейнский динар',
               'BIF - Бурундийский франк', 'BMD - Бермудский доллар', 'BND - Брунейский доллар',
               'BOB - Боливийский боливиано', 'BRL - Бразильский реал', 'BSD - Багамский доллар', 'BTC - Биткойн',
               'BTN - Бутанский нгултрум', 'BWP - Ботсванская пула', 'BYN - Белорусский рубль',
               'BZD - Белизский доллар', 'CAD - Канадский доллар', 'CDF - Конголезский франк',
               'CHF - Швейцарский франк', 'CLF - Условная расчетная единица Чили', 'CLP - Чилийское песо',
               'CNH - китайский офшорный юань', 'CNY - Китайский юань', 'COP - Колумбийское песо',
               'CRC - Коста-риканский колон', 'CUC - Кубинское конвертируемое песо', 'CUP - Кубинский песо',
               'CVE - Эскудо Кабо-Верде', 'CZK - Чешская крона', 'DJF - Франк Джибути', 'DKK - Датская крона',
               'DOP - Доминиканское песо', 'DZD - Алжирский динар', 'EGP - Египетский фунт',
               'ERN - Криптовалюта Ethernity Chain', 'ETB - Эфиопский быр', 'EUR - Евро',
               'FKP - Фунт Фолклендских островов', 'GBP - Фунт стерлингов', 'GEL - Грузинский лари',
               'GGP - Гернсийский фунт', 'GHS - Ганский седи', 'GIP - Гибралтарский фунт', 'GMD - Гамбийский даласи',
               'GNF - Гвинейский франк', 'GTQ - Гватемальский кетсаль', 'GYD - Гайанский доллар',
               'HKD - Гонконгский доллар', 'HNL - Гондурасская лемпира', 'HRK - Хорватская куна',
               'HTG - Гаитянский гурд', 'HUF - Венгерский форинт', 'IDR - Индонезийская рупия',
               'ILS - Новый израильский шекель', 'IMP - Фунт Острова Мэн', 'INR - Индийская рупия',
               'IQD - Иракский динар', 'IRR - Иранский риал', 'ISK - Исландская крона', 'JEP - Джерсийский фунт',
               'JMD - Ямайский доллар', 'JOD - Иорданский динар', 'JPY - Японская иена', 'KES - Кенийский шиллинг',
               'KGS - Киргизский сом', 'KHR - Камбоджийский риель', 'KMF - Франк Комор', 'KPW - Северокорейская вона',
               'KRW - Южнокорейская вона', 'KWD - Кувейтский динар', 'KYD - Доллар Каймановых Островов',
               'KZT - Казахстанский тенге', 'LAK - Лаосский кип', 'LBP - Ливанский фунт', 'LKR - Шри-ланкийская рупия',
               'LRD - Либерийский доллар', 'LSL - Лоти Лесото', 'LYD - Ливийский динар', 'MAD - Марокканский дирхам',
               'MDL - Молдавский лей', 'MGA - Малагасийский ариари', 'MKD - Македонский денар',
               'MMK - Мьянманский кьят', 'MNT - Монгольский тугрик', 'MOP - Патака Макао', 'MRU - Мавританская угия',
               'MUR - Маврикийская рупия', 'MVR - Мальдивская руфия', 'MWK - Малавийская квача',
               'MXN - Мексиканское песо', 'MYR - Малайзийский ринггит', 'MZN - Мозамбикский метикал',
               'NAD - Доллар Намибии', 'NGN - Нигерийская найра', 'NIO - Никарагуанская кордоба',
               'NOK - Норвежская крона', 'NPR - Непальская рупия', 'NZD - Новозеландский доллар', 'OMR - Оманский риал',
               'PAB - Панамский бальбоа', 'PEN - Перуанский соль', 'PGK - Кина Папуа – Новой Гвинеи',
               'PHP - Филиппинское песо', 'PKR - Пакистанская рупия', 'PLN - Польский злотый',
               'PYG - Парагвайский гуарани', 'QAR - Катарский Риал', 'RON - Румынский лей', 'RSD - Сербский динар',
               'RUB - Российский рубль', 'RWF - Франк Руанды', 'SAR - Саудовский риял',
               'SBD - Доллар Соломоновых Островов', 'SCR - Сейшельская рупия', 'SDG - Суданский фунт',
               'SEK - Шведская крона', 'SGD - Сингапурский доллар', 'SHP - Фунт Святой Елены',
               'SLL - Сьерра-леонские леоне', 'SOS - Сомалийский шиллинг', 'SRD - Суринамский доллар',
               'SSP - Южносуданский фунт', 'STD - Добра Сан-Томе и Принсипи', 'STN - Добра Сан-Томе и Принсипи',
               'SVC - Сальвадорский колон', 'SYP - Сирийский фунт', 'SZL - Свазилендский лилангени',
               'THB - Тайский бат', 'TJS - Таджикский сомони', 'TMT - Туркменский манат', 'TND - Тунисский динар',
               'TOP - Тонганская паанга', 'TRY - Турецкая лира', 'TTD - Доллар Тринидада и Тобаго',
               'TWD - Новый тайваньский доллар', 'TZS - Танзанийский шиллинг', 'UAH - Украинская гривна',
               'UGX - Угандийский шиллинг', 'USD - Доллар США', 'UYU - Уругвайское песо', 'UZS - Узбекский сум',
               'VES - Венесуэльский боливар', 'VND - Вьетнамский донг', 'VUV - Вануатский вату',
               'WST - Самоанская тала', 'XAF - Центральноафриканский франк КФА', 'XAG - Унция серебра',
               'XAU - Унция золота', 'XCD - Восточнокарибский доллар', 'XDR - Специальные права заимствования',
               'XOF - Западноафриканский франк КФА', 'XPD - Унция палладия', 'XPF - Франк КФП', 'XPT - Унция платины',
               'YER - Йеменский риал', 'ZAR - Южноафриканский рэнд', 'ZMW - Замбийская квача',
               'ZWL - Зимбабвийский доллар']

translator = Translator()


class Convert(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Convert, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.setWindowIcon(QIcon('icons.ico'))
        # self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.dict_csv = {}
        self.name_file = ''
        self.lst_full = []
        self.data_now = QDate().currentDate()
        self.lst_for_csv_calc = []
        self.current_inv = ''
        self.rate_current = ''

        self.btn_select_file.clicked.connect(self.get_name_file)
        self.btn_group_kod.clicked.connect(self.group_kod)
        self.btn_translate.clicked.connect(self.translate_dict_csv)
        self.btn_load_csv.clicked.connect(self.output_csv)
        self.btn_load_tardek.clicked.connect(self.load_csv_for_tardek)
        self.txt_vet_edit.setAcceptRichText(False)
        self.txt_ched_edit.setAcceptRichText(False)
        self.dte_vet.calendarWidget().setSelectedDate(self.data_now)
        self.dte_vet.setDisplayFormat('yyyy.MM.dd')
        self.dte_chedpp.calendarWidget().setSelectedDate(self.data_now)
        self.dte_chedpp.setDisplayFormat('yyyy.MM.dd')
        self.dte_poruch.calendarWidget().setSelectedDate(self.data_now)
        self.dte_poruch.setDisplayFormat('yyyy.MM.dd')
        self.dte_platezh.calendarWidget().setSelectedDate(self.data_now)
        self.dte_platezh.setDisplayFormat('yyyy.MM.dd')
        self.btn_create_pay.clicked.connect(self.create_payment_vet)
        self.btn_calc_tax.clicked.connect(self.calc_tax)
        self.btn_calc_csv.clicked.connect(self.calc_from_csv)

        self.btn_calc_lv.clicked.connect(self.create_excel_for_lv)

    @staticmethod
    def str_to_float(a: str) -> float:
        a = a.replace(' ', '')
        return float(a.replace(',', '.'))

    @staticmethod
    def name_good(a: str, b: str) -> str:
        lst = a.split('.')

        if b.upper() in lst:
            return '.'.join(lst)
        else:
            if (len(a) + len(b)) < 99:
                lst.append(b.upper())
            return '.'.join(lst)

    @staticmethod
    def weight(a: float, b: float) -> float:
        return round(a + b, 3)

    @staticmethod
    def cost(a: float, b: float) -> float:
        return round(a + b, 2)

    def trans_late(self, a, b, c) -> list:

        x = translator.translate(a, src=b, dest=c)

        return x

    class TranslateThread(QThread):
        translation_complete = pyqtSignal(list)

        def __init__(self, lst_for_translate, src, dest, callback):
            super().__init__()
            self.lst_for_translate = lst_for_translate
            self.src = src
            self.dest = dest
            self.callback = callback

        def run(self):
            # Выполнение перевода (вызов функции trans_late() в классе Convert для списка текстов)

            try:
                self.lst_translate = Convert.trans_late(self, self.lst_for_translate, self.src, self.dest)

            except Exception as e:
                message = QMessageBox(self)
                message.setText(e)
                message.setIcon(QMessageBox.Icon.Warning)
                message.setWindowTitle(e)
                message.setStyleSheet(
                    'background-color: rgb(35, 40, 49); color: white; font-size: 10pt;' 'font-weight: 700; font-family: RussoOne-Regular;')
                message.exec()

            # Оповещение о завершении перевода
            self.callback(self.lst_translate)

    def get_name_file(self):

        self.dict_csv = {}
        self.name_file = ''
        self.lst_full = []
        self.data_now = QDate().currentDate()
        self.lst_for_csv_calc = []
        self.current_inv = ''
        self.rate_current = ''

        try:

            self.name_file = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\Документация\CSV', 'CSV File (*.csv)')[
                0]
            with open(self.name_file, 'r', newline='') as f:
                reader = csv.reader(f, delimiter=';')
                for i in reader:
                    self.lst_full.append(
                        [i[0], i[1].replace('"', '').replace("'", "").replace(';', '').replace(',', ''),
                         self.str_to_float(i[2]),
                         self.str_to_float(i[3])])

            now = datetime.datetime.now()
            self.lbl_input_file.setText('Файл выбран ' + now.strftime("%d-%m-%Y %H:%M"))
            self.lbl_group_kod.setText('')
            self.lbl_translate.setText('')
            self.btn_load_csv.setText('Загрузить CSV')
            self.btn_load_tardek.setText('Сформировать CSV для Тардека')
        except:
            message = QMessageBox(self)
            message.setText('Файл не выбран')
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle('Информация')
            message.setStyleSheet(
                'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular;')
            message.exec()

    def group_kod(self):

        if self.lst_full:
            dlg_kod = Select_qauntity_cmr(self)
            dlg_kod.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            dlg_kod.setWindowTitle('Сгруппировать коды')
            dlg_kod.lbl_qunt_cmr.setText('Количество знаков')
            dlg_kod.spn_qunt.setWrapping(True)
            dlg_kod.spn_qunt.setRange(1, 10)
            dlg_kod.spn_qunt.setValue(6)
            dlg_kod.spn_qunt.setSingleStep(1)
            dlg_kod.exec()
            qaunt_kod = int(dlg_kod.get_qaunt_cmr())

            for i in self.lst_full:

                if i[0][0:qaunt_kod] in self.dict_csv:

                    self.dict_csv[i[0][0:qaunt_kod]] = [self.name_good(self.dict_csv[i[0][0:qaunt_kod]][0], i[1]),
                                                        self.weight(self.dict_csv[i[0][0:qaunt_kod]][1], i[2]),
                                                        self.cost(self.dict_csv[i[0][0:qaunt_kod]][2], i[3])]

                else:

                    self.dict_csv[i[0][0:qaunt_kod]] = [i[1].upper()[:99], i[2], i[3]]

            self.lst_full = []
            for k, v in self.dict_csv.items():
                self.lst_full.append([k, v[0], v[1], v[2]])

            now = datetime.datetime.now()
            self.lbl_group_kod.setText('Коды сгруппированы ' + now.strftime("%d-%m-%Y %H:%M"))
        else:
            message = QMessageBox(self)
            message.setText('Не выбран файл')
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle('Информация')
            message.setStyleSheet(
                'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular;')
            message.exec()

    def get_src(self):
        dlg = Select_language(self)
        dlg.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        dlg.exec()
        return dlg.get_lang()

    def translate_dict_csv(self) -> None:
        self.lst_for_translate = []
        if self.lst_full:
            self.lst_for_translate = [i[1] for i in self.lst_full]
            in_out_lang = self.get_src()

            if in_out_lang:
                try:
                    # Создание и запуск потока для выполнения перевода в фоновом режиме
                    self.translate_thread = self.TranslateThread(self.lst_for_translate, in_out_lang[0], in_out_lang[1],
                                                                 self.on_translation_complete)
                    self.translate_thread.start()


                except Exception as e:
                    message = QMessageBox(self)
                    message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                    message.setText(e)
                    message.setIcon(QMessageBox.Icon.Warning)
                    message.setWindowTitle(e)
                    message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 10pt;'
                                          'font-weight: 700; font-family: RussoOne-Regular;')
                    message.exec()



            else:
                message = QMessageBox(self)
                message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                message.setText('Ничего не выбрано')
                message.setIcon(QMessageBox.Icon.Information)
                message.setWindowTitle('Информация')
                message.setStyleSheet(
                    'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular;')
                message.exec()


        else:
            message = QMessageBox(self)
            message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            message.setText('Не выбран файл')
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle('Информация')
            message.setStyleSheet(
                'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular;')
            message.exec()

    def on_translation_complete(self, lst_translate):
        # Закрытие диалогового окна прогресса и обработка результатов перевода
        try:
            for k, v in enumerate(lst_translate):
                self.lst_full[k][1] = v.text
            now = datetime.datetime.now()
            self.lbl_translate.setText('Описание переведено ' + now.strftime("%d-%m-%Y %H:%M"))

        except Exception as e:
            message = QMessageBox(self)
            message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            message.setText(e)
            message.setIcon(QMessageBox.Icon.Warning)
            message.setWindowTitle(e)
            message.setStyleSheet(
                'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular;')
            message.exec()

    def output_csv(self):
        if self.lst_full:

            try:
                with open('D:\\td\output_csv.csv', 'w', encoding='utf-8-sig', newline='') as f:
                    writer = csv.writer(f, delimiter=';')
                    temp_lst = []

                    for i in self.lst_full:
                        temp_lst.append([i[0], i[1], str(i[2]).replace('.', ','), str(i[3]).replace('.', ',')])

                    writer.writerows(temp_lst)
                    now = datetime.datetime.now()
                    self.btn_load_csv.setText('Загрузить CSV\n (файл загружен ' + now.strftime("%d-%m-%Y %H:%M") + ')')
            except:
                message = QMessageBox(self)
                message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                message.setText('Ошибка загрузки файла')
                message.setIcon(QMessageBox.Icon.Warning)
                message.setWindowTitle('Ошибка')
                message.setStyleSheet(
                    'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular;')
                message.exec()
        else:
            message = QMessageBox(self)
            message.setText('Нет данных для формирования CSV')
            message.setIcon(QMessageBox.Icon.Warning)
            message.setWindowTitle('Ошибка')
            message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 10pt;'
                                  'font-weight: 700; font-family: RussoOne-Regular;')
            message.exec()

    def get_cmr_qaunt(self) -> int:
        dlg = Select_qauntity_cmr(self)
        dlg.exec()
        return dlg.get_qaunt_cmr()

    def load_csv_for_tardek(self):
        global lst_params
        if self.lst_full:
            qauntity_cmr = self.get_cmr_qaunt()
            if qauntity_cmr == 1:
                dlg = One_cmr(self)
                dlg.exec()
                lst_params = [dlg.lne_numb_cmr.text(), dlg.lne_numb_inv.text(), dlg.cmb_count_disp.currentText()[:2],
                              dlg.cmb_contr_dest.currentText()[:2], dlg.qaunt_cll.text()]
                if all(lst_params):
                    try:
                        with open('D:\\td\output_csv_for_tardek.csv', 'w', encoding='utf-8-sig', newline='') as f:
                            writer = csv.writer(f, delimiter=';')
                            writer.writerows(
                                [['description', 'marks', 'quantity', 'quantityUnit', 'hsCode', 'grossWeight',
                                  'dispatchCountryCode',
                                  'destinationCountryCode', 'documentType_1', 'documentNumber_1',
                                  'documentType_2',
                                  'documentNumber_2']])
                            lst_for_tardek = []
                            for i in range(len(self.lst_full)):
                                lst_for_tardek.append([self.lst_full[i][1], '-', 0, 'ZZ', self.lst_full[i][0],
                                                       str(self.lst_full[i][2]).replace('.', ','), lst_params[2],
                                                       lst_params[3],
                                                       '730', lst_params[0], '380', lst_params[1]])
                            lst_for_tardek[0][2] = lst_params[4]
                            writer.writerows(lst_for_tardek)
                            now = datetime.datetime.now()
                            self.btn_load_tardek.setText(
                                'Сформировать CSV для Тардека\n (файл сформирован ' + now.strftime(
                                    "%d-%m-%Y %H:%M") + ')')
                    except:
                        message = QMessageBox(self)
                        message.setText('Ошибка загрузки файла')
                        message.setIcon(QMessageBox.Icon.Warning)
                        message.setWindowTitle('Ошибка')
                        message.setStyleSheet(
                            'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular;')
                        message.exec()

                else:
                    message = QMessageBox(self)
                    message.setText('Не все данные введены')
                    message.setIcon(QMessageBox.Icon.Information)
                    message.setWindowTitle('Информация')
                    message.setStyleSheet(
                        'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular;')
                    message.exec()
            else:

                try:
                    with open('D:\\td\output_csv_for_tardek.csv', 'w', encoding='utf-8-sig', newline='') as f:
                        writer = csv.writer(f, delimiter=';')
                        writer.writerows(
                            [['description', 'marks', 'quantity', 'quantityUnit', 'hsCode', 'grossWeight',
                              'dispatchCountryCode', 'destinationCountryCode', 'consignor_name', 'consignor_street',
                              'consignor_city', 'consignor_country', 'consignor_zip', 'consignee_name',
                              'consignee_street', 'consignee_city', 'consignee_country', 'consignee_zip',
                              'documentType_1', 'documentNumber_1', 'documentType_2', 'documentNumber_2']])
                        for i in range(qauntity_cmr):
                            lst_for_tardek = []
                            dlg_cmr_inv = One_cmr(self)
                            dlg_cmr_inv.setWindowTitle('CMR № ' + str(i + 1))
                            dlg_cmr_inv.exec()
                            lst_params = [dlg_cmr_inv.lne_numb_cmr.text(), dlg_cmr_inv.lne_numb_inv.text(),
                                          dlg_cmr_inv.cmb_count_disp.currentText()[:2],
                                          dlg_cmr_inv.cmb_contr_dest.currentText()[:2], dlg_cmr_inv.qaunt_cll.text()]
                            dlg_disp = Consignor_dispatch(self)
                            dlg_disp.setWindowTitle("Отправитель CMR № " + str(i + 1))
                            dlg_disp.exec()
                            lst_disp = [dlg_disp.lne_name.text(), dlg_disp.lne_zipkod.text(),
                                        dlg_disp.cmb_country.currentText()[:2],
                                        dlg_disp.lne_city.text(), dlg_disp.lne_adres.text()]
                            dlg_dest = Consignor_destination(self)
                            dlg_dest.setWindowTitle("Получатель CMR № " + str(i + 1))
                            dlg_dest.exec()
                            lst_dest = [dlg_dest.lne_name.text(), dlg_dest.lne_zipkod.text(),
                                        dlg_dest.cmb_country.currentText()[:2],
                                        dlg_dest.lne_city.text(), dlg_dest.lne_adres.text()]
                            dlg_qaunt_goods = Select_qauntity_goods(self)
                            dlg_qaunt_goods.setWindowTitle('Количество кодов CMR № ' + str(i + 1))
                            dlg_qaunt_goods.exec()
                            quant_goods = int(dlg_qaunt_goods.spn_qunt.text())
                            for i in range(quant_goods):
                                lst_for_tardek.append([self.lst_full[i][1], '-', 0, 'ZZ', self.lst_full[i][0],
                                                       str(self.lst_full[i][2]).replace('.', ','), lst_params[2],
                                                       lst_params[3], lst_disp[0], lst_disp[4], lst_disp[3],
                                                       lst_disp[2], lst_disp[1], lst_dest[0], lst_dest[4], lst_dest[3],
                                                       lst_dest[2], lst_dest[1], '730', lst_params[0], '380',
                                                       lst_params[1]])
                            lst_for_tardek[0][2] = lst_params[4]
                            print(lst_for_tardek)
                            writer.writerows(lst_for_tardek)
                            print(lst_params, lst_disp, lst_dest, quant_goods)

                        now = datetime.datetime.now()
                        self.btn_load_tardek.setText(
                            'Сформировать CSV для Тардека\n (файл сформирован ' + now.strftime("%d-%m-%Y %H:%M") + ')')
                except:
                    message = QMessageBox(self)
                    message.setText('Ошибка загрузки файла')
                    message.setIcon(QMessageBox.Icon.Warning)
                    message.setWindowTitle('Ошибка')
                    message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 10pt;'
                                          ' font-weight: 700; font-family: RussoOne-Regular;')
                    message.exec()

        else:
            message = QMessageBox(self)
            message.setText('Нет данных для формирования CSV')
            message.setIcon(QMessageBox.Icon.Warning)
            message.setWindowTitle('Ошибка')
            message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 10pt;'
                                  'font-weight: 700; font-family: RussoOne-Regular;')
            message.exec()

    def create_payment_vet(self):

        perehod = ''
        if self.rdi_sal.isChecked():
            perehod = self.rdi_sal.text()
        elif self.rdi_kyb.isChecked():
            perehod = self.rdi_kyb.text()
        elif self.rdi_lav.isChecked():
            perehod = self.rdi_lav.text()
        elif self.rdi_med.isChecked():
            perehod = self.rdi_med.text()

        dannye_payment = {'plat_poruch': self.lne_poruch.text(), 'dte_poruch': self.dte_poruch.text(),
                          'platezhka': self.lne_platezh.text(), 'dte_plat': self.dte_platezh.text(),
                          'dte_svid': self.dte_vet.text(), 'dte_ched': self.dte_chedpp.text(),
                          'numb_truck': self.lne_avto.text(), 'pereh': perehod,
                          'chedp': self.txt_ched_edit.toPlainText().split(),
                          'svid': self.txt_vet_edit.toPlainText().split()}
        if len(dannye_payment['chedp']) != len(dannye_payment['svid']):
            message = QMessageBox(self)
            message.setText('Количество CHEDP не равно количеству вет. свидетельств\n проверьте введенные данные')
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle('Информация')
            message.setStyleSheet(
                'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular;')
            message.exec()
        elif all(dannye_payment.values()):
            try:
                payment.create_payment_vet(dannye_payment)
                now = datetime.datetime.now()
                message = QMessageBox(self)
                message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                message.setText('Файл сформирован')
                message.setIcon(QMessageBox.Icon.Information)
                message.setWindowTitle('Ошибка')
                message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 16pt;'
                                      'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                message.exec()
                self.btn_create_pay.setText(
                    'Сформировать платежку\n (файл сформирован ' + now.strftime(
                        "%d-%m-%Y %H:%M") + ')')
            except Exception as e:
                message = QMessageBox(self)
                message.setText(e)
                message.setIcon(QMessageBox.Icon.Warning)
                message.setWindowTitle('Ошибка')
                message.setStyleSheet(
                    'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular;')
                message.exec()
        else:
            message = QMessageBox(self)
            message.setText('Введены не все данные')
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle('Информация')
            message.setStyleSheet(
                'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular;')
            message.exec()

    def calc_tax(self):
        dlg = Calc_tax(self)
        dlg.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        dlg.exec()

        try:
            result = calculate(dlg.lne_tax_kod.text(), dlg.lne_mass.text(), dlg.lne_value.text(),
                               dlg.cmb_count_origin.currentText()[:2])

            if result[0] and result[1] and result[2]:
                message = QMessageBox(self)
                message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                message.setText(f'{result[0]}')
                message.setIcon(QMessageBox.Icon.Information)
                message.setWindowTitle('Информация')
                message.setStyleSheet(
                    'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                message.exec()
                try:
                    message = Table_rate()
                    message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                    message.comm_lbl.setText('Commodity Code:   ' + result[1])
                    message.total_lbl.setText('Total Amount: ' + result[2] + ' EUR')
                    message.tbl_wdg.setColumnCount(len(result[4]))
                    message.tbl_wdg.setHorizontalHeaderLabels(result[4])
                    message.tbl_wdg.verticalHeader().setVisible(False)

                    message.tbl_wdg.setRowCount(0)
                    for i, row in enumerate(result[3]):
                        message.tbl_wdg.setRowCount(message.tbl_wdg.rowCount() + 1)
                        for j, elem in enumerate(row):
                            message.tbl_wdg.setItem(i, j, QTableWidgetItem(elem))

                    message.exec()
                except Exception as e:
                    message = QMessageBox(self)
                    message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                    message.setText(e)
                    message.setIcon(QMessageBox.Icon.Information)
                    message.setWindowTitle('Информация')
                    message.setStyleSheet(
                        'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                    message.exec()

            elif result[0]:
                message = QMessageBox(self)
                message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                message.setText(f'{result[0]}')
                message.setIcon(QMessageBox.Icon.Information)
                message.setWindowTitle('Информация')
                message.setStyleSheet(
                    'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                message.exec()

            else:
                try:
                    message = Table_rate()
                    message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                    message.comm_lbl.setText('Commodity Code:   ' + result[1])
                    message.total_lbl.setText('Total Amount: ' + result[2] + ' EUR')
                    message.tbl_wdg.setColumnCount(len(result[4]))
                    message.tbl_wdg.setHorizontalHeaderLabels(result[4])
                    message.tbl_wdg.verticalHeader().setVisible(False)

                    message.tbl_wdg.setRowCount(0)
                    for i, row in enumerate(result[3]):
                        message.tbl_wdg.setRowCount(message.tbl_wdg.rowCount() + 1)
                        for j, elem in enumerate(row):
                            message.tbl_wdg.setItem(i, j, QTableWidgetItem(elem))

                    message.exec()
                except Exception as e:
                    message = QMessageBox(self)
                    message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                    message.setText(f'{result[0]}')
                    message.setIcon(QMessageBox.Icon.Information)
                    message.setWindowTitle('Информация')
                    message.setStyleSheet(
                        'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                    message.exec()
        except Exception as e:
            message = QMessageBox(self)
            message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            message.setText(e)
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle('Информация')
            message.setStyleSheet(
                'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
            message.exec()

    class CalculateThread(QThread, QWidget):
        calculate_complete = pyqtSignal(list)

        def __init__(self, lst_full, country_origin, rate_current, lst_for_csv_calc, error_message, callback):
            super().__init__()
            self.lst_full = lst_full
            self.country_origin = country_origin
            self.rate_current = rate_current
            self.callback = callback
            self.lst_for_csv_calc = lst_for_csv_calc
            self.error_message = error_message

        def run(self):
            try:

                for i, item in enumerate(self.lst_full):
                    result_data = (i, item)
                    self.calculate_complete.emit(result_data)

                    error, hs_code, total, table_row, table_headers = calculate(self.lst_full[i][0][0:6],
                                                                                self.lst_full[i][2], str(float(
                            self.lst_full[i][3]) * self.rate_current), self.country_origin)

                    # проверяем процентную ставку

                    if any(table_row) and float(table_row[0][4]) < 1:
                        rate_for_csv = str(round(float(table_row[0][4]) * 100, 3)).replace('.', ',') + '%'

                    elif any(table_row) and float(table_row[0][4]) > 1:
                        rate_for_csv = round(float(table_row[0][4]), 3)

                    else:
                        rate_for_csv = 'ERROR'

                        # подготавлеваем список для записи в файл
                    if error and hs_code and total:
                        self.lst_for_csv_calc.append([hs_code, rate_for_csv, total])
                        self.error_message.append(hs_code + ': ' + error)
                    elif error:
                        self.error_message.append(self.lst_full[i][0][0:6] + ': ' + error)
                        self.lst_for_csv_calc.append([self.lst_full[i][0][0:6], 'ERROR', 'ERROR'])

                    else:
                        self.lst_for_csv_calc.append([hs_code, rate_for_csv, total])







            except Exception as e:
                print(e)

            self.callback(self.lst_for_csv_calc)

    def calc_from_csv(self):

        if self.lst_full:
            try:
                dlg = Current_inv(self)
                dlg.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                dlg.exec()
                country_origin = dlg.country_cmb.currentText().split()[0]
                self.current_inv = dlg.current_cmb.currentText().split(' - ')

                self.rate_current = rates_from_json(self.current_inv[0])

                if self.rate_current:

                    message = QMessageBox(self)
                    message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                    message.setText(f'Курс {self.current_inv[0]} к EURO:  {self.rate_current}')
                    message.setIcon(QMessageBox.Icon.Information)
                    message.setWindowTitle('Информация')
                    message.setStyleSheet(
                        'background-color: rgb(35, 40, 49); color: white; font-size: 12pt;''font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                    message.exec()

                    self.lst_for_csv_calc = []
                    self.error_message = []

                    self.calculate_thread = self.CalculateThread(self.lst_full, country_origin, self.rate_current,
                                                                 self.lst_for_csv_calc, self.error_message,
                                                                 self.on_calculate_complete)

                    self.calculate_thread.calculate_complete.connect(self.handle_calculate_complete)

                    self.calculate_thread.start()

                    self.progress_class = ProgressBarExample(self)
                    self.progress_class.prgbar.setMinimum(0)
                    self.progress_class.prgbar.setMaximum(len(self.lst_full) + 1)

                    self.progress_class.show()
                else:

                    message = QMessageBox(self)
                    message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                    message.setText(f'НЕ ПОЛУЧИЛОСЬ\nКакая-то хрень\nНужно разбираться')
                    message.setIcon(QMessageBox.Icon.Warning)
                    message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 10pt;'
                                          'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                    message.exec()

            except Exception as e:
                message = QMessageBox(self)
                message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                message.setText(e)
                message.setIcon(QMessageBox.Icon.Warning)
                message.setWindowTitle('Ошибка')
                message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 10pt;'
                                      'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                message.exec()

        else:
            message = QMessageBox(self)
            message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            message.setText('Не выбран CSV файл\n Платежи не рассчитаны')
            message.setIcon(QMessageBox.Icon.Warning)
            message.setWindowTitle('Ошибка')
            message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 10pt;'
                                  'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
            message.exec()

    def handle_calculate_complete(self, result_data):

        self.progress_class.prgbar.setValue(result_data[0] + 1)

        self.progress_class.lbl_process.setText(f'{str(result_data[0] + 1)}: {result_data[1][0]} {result_data[1][1]}')

        if self.progress_class.lbl_process.text().split(':')[0] == str(len(self.lst_full)):
            self.progress_class.prgbar.setValue(len(self.lst_full) + 1)
            sleep(14)
            self.progress_class.close()

    def on_calculate_complete(self, lst_for_csv_calc):
        # Закрытие диалогового окна прогресса и обработка результатов перевода

        try:

            with open('D:\\td\calc_tax.csv', 'w', encoding='utf-8-sig', newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerows([['HS CODE', 'RATE', 'AMOUNT']])
                writer.writerows(lst_for_csv_calc)
                now = datetime.datetime.now()
                self.btn_calc_csv.setText(
                    'Рассчитать платежи из CSV файла\n (файл сформирован ' + now.strftime("%d-%m-%Y %H:%M") + ')')



        except Exception as e:
            message = QMessageBox(self)
            message.setText(e)
            message.setIcon(QMessageBox.Icon.Warning)
            message.setWindowTitle('Ошибка')
            message.setStyleSheet(
                'background-color: rgb(35, 40, 49); color: white; font-size: 12pt; font-weight: 700; font-family: RussoOne-Regular;')
            message.exec()

    def create_excel_for_lv(self):
        global lst_for_lv_tax
        try:
            if not self.lst_for_csv_calc:
                message = QMessageBox(self)
                message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                message.setText('Не рассчитаны платежи из CSV файла')
                message.setIcon(QMessageBox.Icon.Warning)
                message.setWindowTitle('Ошибка')
                message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 10pt;'
                                      'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 5px;')
                message.exec()
            else:
                lst_for_lv_tax = []

                for i in range(len(self.lst_full)):
                    lst_for_lv_tax.append(
                        [self.lst_for_csv_calc[i][0], self.lst_for_csv_calc[i][1], self.lst_full[i][2],
                         self.lst_full[i][3], self.lst_for_csv_calc[i][2]])
            try:
                xls_for_lv.create_tax_lv(lst_for_lv_tax, self.current_inv[0], self.rate_current)
                now = datetime.datetime.now()
                message = QMessageBox(self)
                message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                message.setText('Файл сформирован')
                message.setIcon(QMessageBox.Icon.Information)
                message.setWindowTitle('Ошибка')
                message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 16pt;'
                                      'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                message.exec()
                self.btn_calc_lv.setText(
                    'Сформировать расчет платежей для LV таможни\n (файл сформирован ' + now.strftime(
                        "%d-%m-%Y %H:%M") + ')')


            except Exception as e:
                message = QMessageBox(self)
                message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                message.setText(e)
                message.setIcon(QMessageBox.Icon.Warning)
                message.setWindowTitle('Ошибка')
                message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 10pt;'
                                      'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                message.exec()

        except Exception as e:
            message = QMessageBox(self)
            message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            message.setText(e)
            message.setIcon(QMessageBox.Icon.Warning)
            message.setWindowTitle('Ошибка')
            message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 10pt;'
                                  'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 5px;')
            message.exec()


class Select_language(Ui_Dialog, QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Select_language, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.cobmo_input.addItems(language)
        self.combo_output.addItems(language)
        self.cobmo_input.setCurrentText('ru, Russian')
        self.combo_output.setCurrentText('en, English')
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.get_src = 'ru'
        self.get_dest = 'en'

        self.btn_ok.clicked.connect(self.accept)

    def closeEvent(self, event):
        event.ignore()

    def get_lang(self):
        return self.cobmo_input.currentText()[:2], self.combo_output.currentText()[:2]


class Select_qauntity_cmr(Ui_Qauntity_CMR, QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Select_qauntity_cmr, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.btn_qunt_ok.clicked.connect(self.accept)

    def closeEvent(self, event):
        event.ignore()

    def get_qaunt_cmr(self) -> int:
        return int(self.spn_qunt.text())


class One_cmr(Ui_one_cmr, QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(One_cmr, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.cmb_contr_dest.addItems(lst_country)
        self.cmb_contr_dest.setCurrentText('LT - Lithuania')
        self.cmb_count_disp.addItems(lst_country)
        self.cmb_count_disp.setCurrentText('RU - Russian Federation')
        self.btn_ok.clicked.connect(self.accept)

    def closeEvent(self, event):
        event.ignore()


class Consignor_dispatch(Ui_consignor_dispatch, QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Consignor_dispatch, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.cmb_country.addItems(lst_country)
        self.cmb_country.setCurrentText('RU - Russian Federation')

        self.btn_ok.clicked.connect(self.accept)

    def closeEvent(self, event):
        event.ignore()


class Consignor_destination(Ui_consignor_destination, QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Consignor_destination, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.cmb_country.addItems(lst_country)
        self.cmb_country.setCurrentText('RU - Russian Federation')

        self.btn_ok.clicked.connect(self.accept)

    def closeEvent(self, event):
        event.ignore()


class Select_qauntity_goods(Ui_Qauntity_goods, QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Select_qauntity_goods, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.btn_qunt_ok.clicked.connect(self.accept)

    def closeEvent(self, event):
        event.ignore()


class Calc_tax(Ui_calc_tax, QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Calc_tax, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.cmb_count_origin.addItems(lst_country)
        self.cmb_count_origin.setCurrentText('RU - Russian Federation')

        self.btn_ok.clicked.connect(self.accept)

    def closeEvent(self, event):
        event.ignore()


class Current_inv(Ui_Current_inv, QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Current_inv, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.current_cmb.addItems(lst_current)
        self.current_cmb.setCurrentText('EUR - Евро')

        self.country_cmb.addItems(lst_country)
        self.country_cmb.setCurrentText('RU - Russian Federation')

        self.btn_ok.clicked.connect(self.accept)


class Table_rate(Ui_table_rate, QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Table_rate, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.btn_ok.clicked.connect(self.accept)


class ProgressBarExample(Ui_Progress_calc, QWidget):

    def __init__(self, *args, obj=None, **kwargs):
        super(ProgressBarExample, self).__init__(*args, **kwargs)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Convert()
    window.setWindowIcon(QIcon('icons.ico'))
    window.show()
    sys.exit(app.exec())
