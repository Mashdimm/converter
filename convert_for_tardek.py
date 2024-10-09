import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QMessageBox, QTableWidget, \
    QTableWidgetItem, QProgressDialog, QProgressBar, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QFontDatabase, QIcon
from PyQt6.QtCore import QDate, Qt, QObject, QThread, pyqtSignal
from convert import Ui_MainWindow
from googletrans import Translator
from lang import Ui_Dialog
from qauntity_cmr import Ui_Qauntity_CMR
from qauntity_cmr_border import Ui_Qauntity_Border_CMR
from one_cmr import Ui_one_cmr
from consignor_dispatch import Ui_consignor_dispatch
from consignor_dest import Ui_consignor_destination
from qauntity_goods import Ui_Qauntity_goods
from calc_tax import Ui_calc_tax
from current_inv import Ui_Current_inv
from table_rate import Ui_table_rate
from progress import Ui_Progress_calc
from rate_json import rates_from_json
from new_doc import Ui_New_doc

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

type_package = ['43 - Bag, super bulk', '1A - Drum steel', '1B - Drum, aluminium', '1D - Drum, plywood',
                '1G - Drum, fibre', '1W - Drum, wooden', '2C - Barrel, wooden', '3A - Jerry-can, steel',
                '3H - Jerry-can, plastic', '4A - Box, steel', '4B - Box, aluminum', '4C - Box, natural wood',
                '4D - Box, plywood', '4F - Box, reconstituted wood', '4G - Box, fibreboard', '4H - Box, plastic',
                '5H - Bag, woven plastic', '5L - Bag, textile,' '5M - Bag, paper',
                '6H - Composite packaging, plastic receptable', '6P - Composite packaging, glass receptaple',
                'AA - Intermediate bulk container, rigid plastic', 'AB - Receptable, fibre', 'AC - Receptable, paper',
                'AD - Receptable, wooden', 'AE - Aerosol', 'AF - Pallet, modular, collars 80cm x 60cm',
                'AG - Pallet, shrink-wrapped', 'AH - Pallet, 100 cm x 110cm', 'AI - Clamshell', 'AJ - Cone',
                'AM - Ampoule, non-protected', 'AP - Ampoule, protected', 'AT - Atomiser', 'AV - Capsule',
                'BA - Barrel', 'BB - Bobbin', 'BC - Bottlecrate, bottlerack', 'BD - Board', 'BE - Bundle',
                'BF - Balloon, non-protected', 'BG - Bag', 'BH - Bunch', 'BI - Bin', 'BJ - Bucket', 'BK - Basket',
                'BL - Bale, compressed', 'BM - Basin', 'BN - Bale, non-compressed',
                'BO - Bottle, non-protected, cylindrical', 'BP - Balloon, protected',
                'BQ - Bottle, protected cylindrical', 'BR - Bar', 'BS - Bottle, non-protected, bulbous', 'BT - Bolt',
                'BU - Butt', 'BV - Bottle, protected bulbous', 'BW - Box, for liquids', 'BX - Box',
                'BY - Board, in bundle, bunch, truss', 'BZ - Bars, in bundle, bunch, truss', 'CA - Can, rectangular',
                'CB - Beer crate', 'CC - Churn', 'CD - Can, with handle and spout', 'CE - Creel', 'CF - Coffer',
                'CG - Cage', 'CH - Chest', 'CI - Canister', 'CJ - Coffin', 'CK - Cask', 'CL - Coil', 'CM - Collis',
                'CN - Container not otherwise specified as transport equipment', 'CO - Carboy, non-protected',
                'CP - Carboy, protected', 'CQ - Cartdidge', 'CR - Crate', 'CS - Case', 'CT - Carton', 'CU - Cup',
                'CV - Cover', 'CW - Cage, roll', 'CX - Can, cylindrical', 'CY - Cylinder', 'CZ - Canvas',
                'DA - Crate, multiple layer, plastic', 'DB - Crate, multiple layer, wooden',
                'DC - Crate, multiple layer, cardboard', 'DG - Cage, Commonwealth Handling Equipment Pool (CHEP)',
                'DH - Box, Commonweakth Handling Equipment Pool (CHEP), Eurobox', 'DI - Drum, iron',
                'DJ - Demijohn, non-protected', 'DK - Crate, bulk, cardboard', 'DL - Crate, bulk, plastic',
                'DM - Crate, bulk, wooden', 'DN - Dispenser', 'DP - Demijohn, protected', 'DR - Drum',
                'DS - Tray, one layer no cover, plastic', 'DT - Tray, one layer no cover, wooden',
                'DU - Tray, one layer no cover, polystyrene', 'DV - Tray, one layer no cover, cardboard',
                'DW - Tray, two layer no cover, plastic', 'DX - Tray, two layer no cover, wooden',
                'DY - Tray, two layer no cover,cardboard', 'EC - Bag, plastic', 'ED - Case, with pallet base',
                'EE - Case, with pallet base, wooden', 'EF - Case, with pallet base, cardboard',
                'EG - Case, with pallet base, plastic', 'EH - Case, with pallet base, metal', 'EI - Case, isothermic',
                'EN - Envelope', 'FC - Fruit crate', 'FD - Framed crate', 'FI - Firkin', 'FL - Flask',
                'FO - Footlocker', 'FP - Filmpack', 'FR - Frame', 'FT - Foodtainer', 'FX - Bag, flexible container',
                'GB - Gas bottle', 'GI - Girder', 'GR - Receptable, glass', 'GZ - Girders, in bundle,bunch,truss',
                'HA - Basket, with handle, plastic', 'HB - Basket, with handle, wooden',
                'HC - Basket, with handle, cardboard', 'HG - Hogshead', 'HR - Hamper', 'IA - Package, display, wooden',
                'IB - Package, display, cardboard', 'IC - Package, display, plastic', 'ID - Pack9age, display, metal',
                'IE - Pachage, show', 'IF - Package, flow', 'IG - Package, paper-wrapped', 'IH - Drum, plastic',
                'IK - Package, cardboard, with bottle grip-holes', 'IN - Ingot', 'IZ - Ingots, in bundle,bunch,truss',
                'JC - Jerrican, rectangular', 'JG - Jug', 'JR - Jar', 'JT - Jutebag', 'JY - Jerrican, cylindrical',
                'KG - Keg', 'LG - Log', 'LT - Lot', 'LV - Liftvan', 'LZ - Logs, in bundle,bunch,truss',
                'MB - Multiply bag', 'MC - Milk crate', 'MR - Receptable, metal', 'MS - Multiwall sack', 'MT - Mat',
                'MW - Receptable, plastic-wrapped', 'MX - Match box', 'NA - Not available',
                'NE - Unpacked or unpackaged', 'NF - Unpacked or unpackaged, single unit',
                'NG - Unpacked or unpackaged, multiple units', 'NS - Nest', 'NT - Net', 'NU - Net, tube, plastic',
                'NV - Net, tube, textile', 'PA - Packet', 'PB - Pallet, box', 'PC - Parcel',
                'PD - Pallet, modular, collars 80cm x 100cm', 'PE - Pallet, modular, collars 80cm x 120cm', 'PF - Pen',
                'PG - Plate', 'PH - Pitcher', 'PI - Pipe', 'PJ - Punnet', 'PK - Package', 'PL - Pail', 'PN - Plank',
                'PO - Pouch', 'PR - Receptable, plastic', 'PT - Pot', 'PU - Tray', 'PV - Pipes, in bundle,bunch,truss',
                'PX - Pallet', 'PY - Plates, in bundle,bunch,truss', 'PZ - Pipes, in bundle,bunch,truss',
                'QA - Drum, steel, non removable head', 'QB - Drum, steel, removable head',
                'QC - Drum, aluminium, non-removable head', 'QD - Drum, aluminium, removable head',
                'QF - Drum,plastic, non-removable head', 'QG - Drum,plastic, removable head',
                'QH - Barrel, wooden, bung type', 'QJ - Barrel, wooden, removable head',
                'QK - Jerry-can, steel, non removable head', 'QL - Jerry-can, steel, removable head',
                'QM - Jerry-can, plastic, non removable head', 'QN - Jerry-can, plastic, removable head',
                'QP - Box, wooden, natural wood, ordinary', 'QQ - Box, wooden, natural wood, with sift proof walls',
                'QR - Box, plastic, expanded', 'QS - Box, plastic, solid', 'RD - Rod', 'RG - Ring',
                'RJ - Rack, clothing hanger', 'RK - Rack', 'RL - Reel', 'RO - Roll', 'RT - Rednet',
                'RZ - Rods, in bundle/bunch/truss', 'SA - Sack', 'SB - Slab', 'SC - Shallow crate', 'SD - Spindle',
                'SE - Sea-chest', 'SH - Sachet', 'SI - Skid', 'SK - Skeleton case', 'SL - Slipsheet', 'SM - Sheetmetal',
                'SO - Spool', 'SP - Sheet, plastic wrapping', 'SS - Case, steel', 'ST - Sheet', 'SU - Suitcase',
                'SV - Envelope, steel', 'SW - Shrinkwrapped', 'SX - Set', 'SY - Sleeve',
                'SZ - Sheets, in bundle,bunch,truss', 'TB - Tub', 'TC - Tea chest', 'TD - Tube, collapsible',
                'TI - Tierce', 'TK - Tank, rectangular', 'TL - Trailers', 'TN - Tin', 'TO - Tun', 'TR - Trunk',
                'TS - Truss', 'TU - Tube', 'TV - Tube, with nozzle', 'TY - Tank, cylindrical',
                'TZ - Tubes, in bundle,bunch,truss', 'UC - Uncaged', 'VA - Vat',
                'VG - Bulk, gas (at 1 031 mbar and 15 ?C)', 'VI - Vial', 'VK - Vanpack', 'VL - Bulk, liquid',
                'VO - Bulk, solid, large particles (nodules)', 'VP - Vacuum-packed',
                'VQ - Bulk, liquefied gas (abnormal temp,pres)', 'VR - Bulk, solid, granular particles (grains)',
                'VY - Bulk, solid, fine particles (powders)', 'WA - Intermediate bulk container', 'WB - Wickerbottle',
                'WC - Intermediate bulk container, steel', 'WD - Intermediate bulk container, aluminium',
                'WF - Intermediate bulk container, metal',
                'WG - Intermediate bulk container, steel, pressurised > 10kPa',
                'WH - Intermediate bulk container, aluminium, pressurised > 10kPa',
                'WJ - Intermediate bulk container, metal, pressure 10kPa',
                'WK - Intermediate bulk container, steel, liquid',
                'WL - Intermediate bulk container, aluminium, liquid', 'WM - Intermediate bulk container, metal liquid',
                'WN - Intermediate bulk container, woven plastic, without coat  liner',
                'WP - Intermediate bulk container, woven plastic, coated',
                'WQ - Intermediate bulk container, woven plastic, with liner',
                'WR - Intermediate bulk container, woven plastic, coated and liner',
                'WS - Intermediate bulk container, plastic film',
                'WT - Intermediate bulk container, textile without coat liner',
                'WU - Intermediate bulk container, natural wood, with inner liner',
                'WV - Intermediate bulk container, textile, coated',
                'WW - Intermediate bulk container, textile, with liner',
                'WX - Intermediate bulk container, textile, coated and liner',
                'WY - Intermediate bulk container, plywood, with inner liner',
                'WZ - Intermediate bulk container, recontituted wood, with inner liner',
                'XA - Bag, woven plastic, without inner coat liner', 'XB - Bag, woven plastic, sift proof',
                'XC - Bag, woven plastic, water resistant', 'XD - Bag, plastics film',
                'XF - Bag, textile, without inner coat liner', 'XG - Bag, textile, sift proof',
                'XH - Bag, textile, water resistant', 'XJ - Bag, paper, multi-wall',
                'XK - Bag, paper, multi-wall, water resistant',
                'YA - Composite packaging, plastic receptable in steel drum',
                'YB - Composite packaging, plastic receptable in steel crate box',
                'YC - Composite packaging, plastic receptable in aluminium drum',
                'YD - Composite packaging, plastic receptable in aluminium crate',
                'YF - Composite packaging, plastic receptable in wooden box',
                'YG - Composite packaging, plastic receptable in plywood drum',
                'YH - Composite packaging, plastic receptable in plywood box',
                'YJ - Composite packaging, plastic receptable in fibre drum',
                'YK - Composite packaging, plastic receptable in fibreboard box',
                'YL - Composite packaging, plastic receptable in plastic drum',
                'YM - Composite packaging, plastic receptable in solid plastic box',
                'YN - Composite packaging, glass receptaple in steel drum',
                'YP - Composite packaging, glass receptaple in steel crate box',
                'YQ - Composite packaging, glass receptaple in aluminium drum',
                'YR - Composite packaging, glass receptaple in aluminium',
                'YS - Composite packaging, glass receptable in wooden box',
                'YT - Composite packaging, glass receptaple in plywood drum',
                'YV - Composite packaging, glass receptaple in wickerwork hammer',
                'YW - Composite packaging, glass receptaple in fibre drum',
                'YX - Composite packaging, glass receptaple in fibreboard box',
                'YY - Composite packaging, glass receptaple in expandable plastic pack',
                'YZ - Composite packaging, glass receptaple in solid plastic pack',
                'ZA - intermediate bulk container, paper, multi-wall', 'ZB - Bag, large',
                'ZC - intermediate bulk container, paper, multi-wall, water resistant',
                'ZD - intermediate bulk container, rigid plastic, freestanding, with structural equipment, solids',
                'ZF - intermediate bulk container, rigid plastic, freestanding, solids',
                'ZG - intermediate bulk container, rigid plastic, freestanding, with structural equipment, pressurised',
                'ZH - intermediate bulk container, rigid plastic, freestanding, pressurised',
                'ZJ - intermediate bulk container, rigid plastic, freestanding, with structural equipment, liquids',
                'ZK - intermediate bulk container, rigid plastic, freestanding, liquids',
                'ZL - intermediate bulk container, composite, rigid plastic, solids',
                'ZM - intermediate bulk container, composite, flexible plastic, solids',
                'ZN - intermediate bulk container, composite, rigid plastic, pressurised',
                'ZP - intermediate bulk container, composite, flexible plastic, pressurised',
                'ZQ - intermediate bulk container, composite, rigid plastic, liquids',
                'ZR - intermediate bulk container, composite, flexible plastic, liquids',
                'ZS - intermediate bulk container, composite', 'ZT - intermediate bulk container, fibreboard',
                'ZU - intermediate bulk container, flexible',
                'ZV - intermediate bulk container, metal, other than steel',
                'ZW - intermediate bulk container, natural wood', 'ZX - Intermediate bulk container, plywood',
                'ZY - Intermediate bulk container, recontituted wood', 'ZZ - Mutually defined']

type_doc_lv = [
    'C085 - Common Health Entry Document for Plants and Plant Products (CHED-PP) (as set out in Part 2, section C of Annex II to Commission Implementing Regulation (EU) 2019/1715 (OJ L 261))',
    'C640 - Common Veterinary Entry Document (CVED) in accordance with Commission Regulation (EC) No. 282/2004, used for veterinary checks on live animals',
    'C641 - Dissostichus - catch document import',
    'C651 - Electronic administrative document (e-AD), as referred to in Article 3(1) of Reg. (EC) No 684/2009',
    'C656 - Dissostichus - catch document export',
    'C658 - Fallback Accompanying Document for movements of excise goods under suspension of excise duty (FAD), as referred to in Article 8(1) Reg. (EC) No 684/2009',
    'C673 - Catch certificate',
    'C678 - Common entry document (CED) (model of which is set out in Annex II of the Regulation (EC) No 669/2009 (OJ L 194))',
    'C690 - FLEGT import licence for timber', 'L001 - Import licence AGRIM', 'L079 - Textile products: import licence',
    'L100 - Import licence "controlled substances" (ozone), issued by the Commission',
    'N002 - Certificate of conformity with the European Union marketing standards for fresh fruit and vegetables',
    'N003 - Certificate of quality', 'N018 - ATR certificate', 'N325 - Proforma invoice', 'N380 - Commercial invoice',
    'N820 - Transit declaration "T"', 'N821 - External Community transit declaration / common transit, T1',
    'N822 - Internal Community transit declaration T2', 'N825 - T2L document', 'N851 - Phytosanitary certificate',
    'N852 - Analysis and health certificate',
    'N853 - Common Veterinary Entry Document (CVED) in accordance with Commission Regulation (EC) No. 136/2004, used for veterinary checks on products',
    'N861 - Universal certificate of origin', 'N862 - Declaration of origin',
    'N864 - Preference certificate of origin (declaration of preferential origin on the invoice; EUR.2',
    'N865 - Certificate of origin Form A', 'N911 - Import licence', 'N933 - Cargo declaration (arrival)',
    'N941 - Embargo permit', 'N951 - TIF form', 'N954 - Movement certificate EUR.1',
    'NZZZ - Document equivalent to "ZZZ" defined in Commission Delegated Regulation (EU) 2016/341 (Appendix D2: Additional codes for the computerised transit system)',
    'C672 - Information document accompanying shipments of waste as mentioned in Regulation (EC) No 1013/2006 (OJ L 190) - Article 18 and Annex VII']
type_doc_lt = ['C710 - Teabeleht', 'C034 - Kimberley Eli sertifikaat',
               'Y072 - Andorrast tagasitoodavad Eli paritolu kaubad, vastavalt asjakohastele Eli oigusaktidele',
               'A017 - Maaruses (EL) nr 593/2013 (EUT L 170) nimetatud autentsussertifikaat',
               'Y078 - Norrast tagasitoodavad Eli paritolu kaubad, vastavalt asjakohastele Eli oigusaktidele',
               'Y216 - Poola - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y217 - Portugal - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'C673 - Свидетельство о вылове',
               'Y208 - Prantsusmaa - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'C076 - Padev asutus on andnud loa (maaruse (EL( 2017/1509) II lisa VI osa)',
               'C077 - Padev asutus on andnud loa (maaruse (EL( 2017/1509) II lisa VIII osa)',
               'U005 - Padevate asutuste valjaantud paritolunimetussertifikaat',
               'U110 - Paritolukinnitus (Eli ja Jaapani majanduspartnerluslepingu artikli 3.16 loike 2 punkt a ja artikli 3.17 loike 5 punkt a)',
               'U111 - Paritolukinnitus identsetest toodetest koosnevate mitmekordsete saadetiste puhul (Eli ja Jaapani majanduspartnerluslepingu artikli 3.16 loike 2 punkt a ja artikli 3.17 loike 5 punkt a)',
               'U052 - Paritolusertifikaat Vorm A kinnitusega Erand - delegeeritud maarus (EL) 2017/968',
               'U072 - Paritolusertifikaat Vorm A kinnitusega Erand - delegeeritud maarus (EL) 2019/561',
               '821 - Транспортная накладная модель Т1', '861 - Сертификат происхождения',
               '862 - Декларация происхождения', '955 - Карнет АТА',
               'U177 - Paritolutoend sisaldab jargmist ingliskeelset lauset: Derogation Anndex B(a) of Protocol Concerning the definition of the concept of originating products and methods of administrative cooperation of the EU-Singapore FTA.',
               'Y221 - Rootsi - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y218 - Rumeenia - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y203 - Saksamaa - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y079 - San Marinost tagasitoodavad Eli paritolu kaubad, vastavalt asjakohastele Eli oigusaktidele',
               'U176 - Sertifikaat EUR.1 kinnitusega Derogation - Decision No 1/2019 of the ESA-EU Customs Cooperation Committee of 14 January 2019 voi Derogation - Decision no 1/2019 du Comite de Cooperation Douaniere AfOA-UE du 14 janvier 2019',
               'C064 - Sisse - voi valjaveoluba kaupadele, mida on voimalik kasutada piinamiseks (maarus (EU) 2019/125)',
               'Y219 - Sloveenia - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y220 - Soome - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y202 - Taani - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'C700 - Teabeleht INF4',
               'Y951 - Turule Iastud fluorosusivesinike koguste vahendamise erandid vastavalt maaruse (EL) nr 517/2014 artikli 15 loikele 2.',
               'C057 - Vastavusdeklaratsiooni koopia - variant A, nagu on osutatud maaruse (EL) 2016/879 artikli 1 loikes 2 ja lisas.',
               'C079 - Vastavusdeklaratsiooni koopia - variant B, nagu on osutatud maaruse (EL) 2016/879 artikli 1 loikes 2 ja lisas.',
               'C082 - Vastavusdeklaratsiooni koopia - variant C, nagu on osutatud maaruse (EL) 2016/879 artikli 1 loikes 2 ja lisas.',
               'C018 - Valjavote dokumendist V I 2, millele on lisatud marge vastavalt maaruse (EL) 2018/273 artikli 25 loikele 2',
               'Y105 - Y105', 'Y109 - Y109',
               'Y222 - Uhendkuningriik - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y971 - Muud kui meetmega seotud MG joonealustes markustes kirjeldatud kaubad (maaruse (EL) 2017/1509) II lisa VIII osa)',
               'Y073 - Sveitsist tagasitoodavad Eli paritolu kaubad, vastavalt asjakohastele Eli oigusaktidele',
               'D018 - Arve tehingute kohta, mis ei ole vabastatud tasakaalustatud/dumpinguvastastest tollimaksudest',
               'Y200 - Belgia - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y201 - Bulgaria - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'C073 - C073', '705 - Накладная', '852 - Санитарный сертификат', '853 - Ветеринарный сертификат',
               '864 - Преференциальный сертификат происхождения', '951 - Форма TIF',
               'Y023 - Грузополучатель (номер сертификата УЭО)', 'Y025 - Представитель (номер сертификата АЕО)',
               'Y026 - Принципал (номер сертификата АЕО)', 'Y028 - Перевозчик (номер сертификата АЕО)',
               'D017 - Commercial invoice within the framework of undertakings and Export Undertaking Certificate issued by CCCME (Annex III of Regulation 513/2013 as amended by Regulation 748/2013)',
               'C664 - Deklaratsioon CN22 vastavalt maaruse (EL) 2015/2446 artiklile 144',
               'C665 - Deklaratsioon CN23 vastavalt maaruse (EL) 2015/2446 artiklile 144',
               'C017 - Dokument V I 1, millele on lisatud marge vastavalt maaruse (EL) 2018/273 artikli 25 loikele 2',
               'C075 - Dokument , mis naitab, et toupuhtad aretusloomad tuleb kanda aretusuhingu peetavasse touraamatusse voi aretusettevotte peetavasse aretustegistrisse (maarus (EL) 2016/1012, artikkel 37',
               'Y204 - Eesti - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y925 - Eksport laborimastaabis teadusliku too voi laborianaluusi tarbeks (maaruse (EL) nr 2017/852 artikli 3 loige 3)',
               'Y223 - Erand kaitsemeetmest vastavalt maaruse (EL) 2019/67 artiklile 2',
               'Y074 - Faari saartelt tagasitoodavad Eli paritolu kaubad, vastavalt asjakohastele Eli oigusaktidele',
               'Y077 - Goods with EU origin returning from Lichtenstein, according to the relevant EU legislation',
               'Y075 - Groonimaalt tagasitoodavad Eli paritolu kaubad, vastavalt asjakohastele Eli oigusaktidele',
               'Y207 - Hispaania - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'C078 - Hobuslase identifitseerimisdokument (maarus (EL) 2016/1012, artikkel 32)',
               'Y209 - Horvaatia - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y205 - lirimaa - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'U112 - Importija teadmine (Eli ja Jaapani majanduspartnerluslepingu artikli 3.16 loike 2 punkt b)',
               'Y076 -  Islandilt tagasitoodavad Eli paritolu kaubad, vastavalt asjakohastele Eli oigusaktidele',
               'Y210 - Itaalia - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y928 - Komisjoni rakendusmaarus (EL) 2019/1787 ei holma deklareeritud kaupu',
               'Y937 - Komisjoni rakendusmaarus (EL) 2019/1793 ei holma deklareeritud kaupu',
               '823 - Kontrolldokument T5',
               'Y206 - Kreeka - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'U065 - Kaesoleva maaruse kahaselt Pakistani padeva asutuse poolt valja antud paritolusertifikaadi vormi A lahtris 4 peab olema marge: Autonomous m',
               'Y211 - Kupros - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y213 - Leedu - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'C080 - Lihtsustatud VI 1', 'C081 - Lihtsustatud enesesertifitseerimisdokument VI 1',
               'C068 - Liidu Uldine Ekspordiluba EU GEA (maarus (EU) 2019/125)',
               'U164 - Uldiste tariifsete soodustuste kava kohane tegistreeritud eksporija koostatud paritolukinnitus sellise saadetise kohta, milles paritolustaatusega toodete koguvaartus ei uleta 6 000 eurot',
               'D019 - Luba rakendada dumpinguvastase/tasakaalustava meetmena majandusliku mojuga tolliprotseduuri / teatavat kasutusotstarvet (delegeeritud maaruse (EL) 2015/2446 A lisa veerg 8c)',
               '235 - Список контейнеров', '703 - Накладная', '704 - Главный коносамент',
               '741 - Главная авиагрузовая накладная', '750 - Уведомление об отправке (почтовые посылки)',
               '785 - Грузовой манифест', '820 - Транспортная накладная модель Т',
               '830 - Декларация на товары для вывоза', '911 - Лицензия на импорт', '941 - Разрешение на эмбарго',
               '954 - Сертификат происхождения 1 евро', 'C656 - Dissostichus - экспорт документов',
               'Y212 - Lati - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y215 - Madalmaad - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y214 - Malta - Mandrivala voi majandusvoond (maarus 2019/1131, millega luuakse tollimeede, ELT L 179, lk 12)',
               'Y950 - Muud kaubad kui fluorosusivesinikega eeltaidetud seadmed',
               'Y949 - Muud kaubad kui need, mida on kirjeldatud meetmega seotud joonealustes markustes (R267/2012)',
               'Y970 - Muud kui meetmega seotud MG joonealustes markustes kirjeldatud kaubad (maaruse (EL) 2017/1509) II lisa VI osa)',
               'C048 - Maaruse (EL) nr 704/2014 lisas satestatud sertifikaat idandite kasvatamiseks ette nahtud idandite ja seemnete importimiseks',
               '325 - Счет-проформа', '714 - Домовой коносамент', '720 - Накладная ЦИМ (ж / д)',
               '720A - NCTS железнодорожное испытательное движение', '380 - Счет-фактура', '722 - Дорожный лист-СМГС',
               '740 - Авианакладная', '787 - Bordereau', '952 - Книжка МДП', 'ZZZ - Другие',
               '18 - Сертификат движения A.TR.1', '2 - Сертификат соответствия', '271 - Товарная накладная',
               '3 - Сертификат качества', '730 - Транспортная накладная',
               '760 - Мультимодальные / комбинированные перевозки док.', '822 - Транспортная накладная модель Т2',
               '825 - Транспортная накладная модель T2L', '851 - Фитосанитарный сертификат',
               '865 - Сертификат происхождения по форме GSP', '933 - Грузовое декларирование (прибытие)',
               'C641 - Dissostichus - испорт документов отлова',
               'Y022 - Грузоотправитель / экспортер (номер сертификата УЭО)',
               'Y024 - Заявитель (номер сертификата УЭО)', 'Y027 - Владелец склада (номер сертификата АЕО)',
               'Y029 - Другой уполномоченный экономический оператор (номер сертификата УЭО)',
               'Y031 - Этот код сертификата может использоваться для обозначения того, что грузы прибывают или отправляются в Уполномоченный экономический оператор (УЭО) в третьей стране, с которой Европейский Союз (ЕС) заключил взаимное соглашение о признании программ УЭО. Помимо кода сертификата (Y031) индентификационный код этой третьей страны УЭО должен',
               'Y927 - Заявленные товары не подпадают под Регламент Совета (ЕС) № 1005/2008',
               'C085 - Единый ввозной документ для растений и растительных продуктов (CHED-PP) (как указано в Приложении II, Часть 2, Раздел С Регламента Комиссии (ЕС) 2019/1795 (OJ L 261))',
               '002 - Varske puu- ja koogivilja suhtes kohaldatavate Euroopa Liidu turustamisstandarditele vastavust toendav sertifikaat']

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

            self.name_file = QFileDialog.getOpenFileName(self, 'Open file', 'D://Документация//CSV', 'CSV File (*.csv)')[
                0]
            with open(self.name_file, 'r', newline='') as f:
                reader = csv.reader(f, delimiter=';')
                for i in reader:
                    self.lst_full.append(
                        [i[0], i[1].replace('"', '').replace("'", "").replace(';', '').replace(',', '').replace('«',
                                                                                                                '').replace(
                            '»', ''),
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
            message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            message.setText('Не выбран файл')
            message.setIcon(QMessageBox.Icon.Warning)
            message.setWindowTitle('Ошибка')
            message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 16pt;'
                                  'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
            message.exec()

    def group_kod(self):

        if self.lst_full:
            dlg_kod = Select_qauntity_cmr(self)
            dlg_kod.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            dlg_kod.setWindowTitle('Сгруппировать коды')
            dlg_kod.lbl_qunt_cmr.setText('Количество знаков')
            dlg_kod.spn_qunt.setWrapping(True)
            dlg_kod.spn_qunt.setRange(4, 10)
            dlg_kod.spn_qunt.setValue(8)
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
                with open('D:\\TD\output_csv.csv', 'w', encoding='utf-8-sig', newline='') as f:
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

        if self.lst_full:
            qauntity_cmr = Select_border_qauntity_cmr()
            qauntity_cmr.exec()
            kolvo_cmr = int(qauntity_cmr.spn_qunt.text())
            if qauntity_cmr.rdb_ee.isChecked():
                border_country = 'EE'
            elif qauntity_cmr.rdb_lt.isChecked():
                border_country = 'LT'
            else:
                border_country = None

            if border_country == 'LT' and kolvo_cmr == 1:

                dlg = One_cmr(border_country)
                dlg.exec()
                lst_for_writerows = ['description', 'marks', 'quantity', 'quantityUnit', 'hsCode', 'grossWeight',
                                     'dispatchCountryCode', 'destinationCountryCode', 'documentType_1',
                                     'documentNumber_1', 'documentType_2', 'documentNumber_2'] + dlg.numb_description
                lst_params = [dlg.lne_numb_cmr.text(), dlg.lne_numb_inv.text(), dlg.cmb_count_disp.currentText()[:2],
                              dlg.cmb_contr_dest.currentText()[:2], dlg.qaunt_cll.text()] + dlg.numb_new_doc
                if all(lst_params):

                    try:
                        with open('D:\\TD\output_csv_for_tardek_lt.csv', 'w', encoding='utf-8-sig', newline='') as f:
                            writer = csv.writer(f, delimiter=';')
                            writer.writerows([lst_for_writerows])
                            lst_for_tardek = []
                            for i in range(len(self.lst_full)):
                                lst_for_tardek.append([self.lst_full[i][1], '-', 0, 'ZZ', self.lst_full[i][0],
                                                       str(self.lst_full[i][2]).replace('.', ','), lst_params[2],
                                                       lst_params[3],
                                                       '730', lst_params[0], '380', lst_params[1]] + lst_params[5:])
                            lst_for_tardek[0][2] = lst_params[4]
                            writer.writerows(lst_for_tardek)
                            now = datetime.datetime.now()
                            self.btn_load_tardek.setText(
                                'Сформировать CSV для Тардека\n (файл сформирован ' + now.strftime(
                                    "%d-%m-%Y %H:%M") + ')')
                    except:
                        message = QMessageBox(self)
                        message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                        message.setText('Ошибка загрузки файла')
                        message.setIcon(QMessageBox.Icon.Warning)
                        message.setWindowTitle('Ошибка')
                        message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 16pt;'
                                              'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                        message.exec()

                else:
                    message = QMessageBox(self)
                    message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                    message.setText('Не все данные введены')
                    message.setIcon(QMessageBox.Icon.Information)
                    message.setWindowTitle('Информация')
                    message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 16pt;'
                                          'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                    message.exec()
            elif border_country == 'LT' and kolvo_cmr > 1:

                try:
                    with open('D:\\TD\output_csv_for_tardek_lt.csv', 'w', encoding='utf-8-sig', newline='') as f:
                        writer = csv.writer(f, delimiter=';')
                        writer.writerows(
                            [['description', 'marks', 'quantity', 'quantityUnit', 'hsCode', 'grossWeight',
                              'dispatchCountryCode', 'destinationCountryCode', 'consignor_name', 'consignor_street',
                              'consignor_city', 'consignor_country', 'consignor_zip', 'consignee_name',
                              'consignee_street', 'consignee_city', 'consignee_country', 'consignee_zip',
                              'documentType_1', 'documentNumber_1', 'documentType_2', 'documentNumber_2']])
                        for i in range(kolvo_cmr):
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

                            writer.writerows(lst_for_tardek)

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
            elif border_country == 'EE' and kolvo_cmr == 1:

                lst_for_writerows = ['countryOfDestination',
                                     'commodityDescriptionOfGoods',
                                     'commodityHarmonizedSystemSubHeadingCode', 'commodityCombinedNomenclatureCode',
                                     'goodsMeasureGrossMass',
                                     'packaging_typeOfPackages_1', 'packaging_numberOfPackages_1',
                                     'packaging_shippingMarks_1',
                                     'supportingDocument_documentType_1', 'supportingDocument_referenceNumber_1',
                                     'supportingDocument_complementOfInformation_1',
                                     'supportingDocument_documentLineNumber_1', 'transportDocument_documentType_1',
                                     'transportDocument_referenceNumber_1', 'supportingDocument_documentType_2',
                                     'supportingDocument_referenceNumber_2',
                                     'supportingDocument_complementOfInformation_2',
                                     'supportingDocument_documentLineNumber_2']

                try:
                    dlg = One_cmr(border_country)
                except Exception as e:
                    print(e)
                dlg.exec()

                lst_params = [dlg.lne_numb_cmr.text(), dlg.lne_numb_inv.text(), dlg.cmb_count_disp.currentText()[:2],
                              dlg.cmb_contr_dest.currentText()[:2], dlg.qaunt_cll.text(),
                              dlg.cmb_pakage.currentText()[:2]] + dlg.numb_new_doc

                lst_for_writerows = lst_for_writerows + dlg.numb_description

                if all(lst_params):
                    print(lst_params)
                    print(self.lst_full)
                    try:
                        with open('D:\\TD\output_csv_for_tardek_lv.csv', 'w', encoding='utf-8-sig', newline='') as f:
                            writer = csv.writer(f, delimiter=';')
                            writer.writerows([lst_for_writerows])
                            lst_for_tardek = []

                            def seven_eight_znak(commod_kod: str) -> str:

                                # if len(lst[i][0]) == 6:
                                # return '00'
                                # elif len(lst[i][0]) == 7:
                                # return lst[i][0][6] + '0'
                                if len(commod_kod) == 8:

                                    return commod_kod[6:8]


                            for i in range(len(self.lst_full)):
                                lst_for_tardek.append(
                                    [lst_params[3], self.lst_full[i][1], self.lst_full[i][0], seven_eight_znak(self.lst_full[i][0]),
                                     str(self.lst_full[i][2]).replace('.', ','), lst_params[5], 0, '-', 'N380',
                                     lst_params[1], '-', '1',
                                     'N730', lst_params[0], 'NZZZ', lst_params[0], '-', '1'] + lst_params[6:])

                                lst_for_tardek[0][6] = lst_params[4]
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
                            'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                        message.exec()

                else:
                    message = QMessageBox(self)
                    message.setText('Не все данные введены')
                    message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                    message.setIcon(QMessageBox.Icon.Information)
                    message.setWindowTitle('Информация')
                    message.setStyleSheet(
                        'background-color: rgb(35, 40, 49); color: white; font-size: 10pt; font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                    message.exec()
            elif border_country == 'EE' and kolvo_cmr > 1:

                message = QMessageBox(self)
                message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                message.setText('Сюда множественный набор делать нельзя')
                message.setIcon(QMessageBox.Icon.Information)
                message.setWindowTitle('Информация')
                message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 16pt;'
                                      'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                message.exec()
            elif border_country == None:
                message = QMessageBox(self)
                message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
                message.setText('Не все данные введены')
                message.setIcon(QMessageBox.Icon.Information)
                message.setWindowTitle('Информация')
                message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 16pt;'
                                      'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
                message.exec()

        else:
            message = QMessageBox(self)
            message.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            message.setText('Нет данных для формирования CSV')
            message.setIcon(QMessageBox.Icon.Warning)
            message.setWindowTitle('Ошибка')
            message.setStyleSheet('background-color: rgb(35, 40, 49); color: white; font-size: 16pt;'
                                  'font-weight: 700; font-family: RussoOne-Regular; border: 2px solid gray; border-radius: 10px;')
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
                    message.setText(f'Курс {self.current_inv[0]} к EUR:  {self.rate_current}')
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


class Select_border_qauntity_cmr(Ui_Qauntity_Border_CMR, QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Select_border_qauntity_cmr, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.btn_brd_qunt_ok.clicked.connect(self.accept)

    def closeEvent(self, event):
        event.ignore()

    # def get_qaunt_cmr(self) -> int:
    # return int(self.spn_qunt.text())


class One_cmr(Ui_one_cmr, QDialog):
    def __init__(self, border_country, *args, obj=None, **kwargs):
        super(One_cmr, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.cmb_contr_dest.addItems(lst_country)
        self.cmb_contr_dest.setCurrentText('LT - Lithuania')
        self.cmb_count_disp.addItems(lst_country)
        self.cmb_count_disp.setCurrentText('RU - Russian Federation')
        self.cmb_pakage.addItems(type_package)
        self.cmb_pakage.setCurrentText('PX - Pallet')
        self.btn_add_doc.clicked.connect(self.add_doc)
        self.numb_new_doc = []
        self.numb_description = []

        self.btn_ok.clicked.connect(self.accept)
        self.border_country = border_country

    def closeEvent(self, event):
        event.ignore()

    def add_doc(self):

        dlg = New_doc()
        if self.border_country == 'LT':
            dlg.current_cmb.clear()
            dlg.current_cmb.addItems(type_doc_lt)
            dlg.current_cmb.setCurrentText('ZZZ - Другие')

        dlg.exec()
        if self.border_country == 'EE':

            if not self.numb_new_doc:
                self.numb_new_doc = [dlg.get_values()[1], dlg.get_values()[0], '-', '1']
                self.numb_description = ['supportingDocument_documentType_3', 'supportingDocument_referenceNumber_3',
                                         'supportingDocument_complementOfInformation_3',
                                         'supportingDocument_documentLineNumber_3']
            else:
                try:
                    old_count = int(self.numb_description[-1].split('_')[-1])
                    self.count = str(old_count + 1)

                    new_lst = [
                        'supportingDocument_documentType_' + self.count,
                        'supportingDocument_referenceNumber_' + self.count,
                        'supportingDocument_complementOfInformation_' + self.count,
                        'supportingDocument_documentLineNumber_' + self.count
                    ]
                    self.numb_description.extend(new_lst)
                    self.numb_new_doc.extend([dlg.get_values()[1], dlg.get_values()[0], '-', '1'])
                except Exception as e:
                    print(e)
        elif self.border_country == 'LT':

            if not self.numb_new_doc:
                self.numb_new_doc = [dlg.get_values()[1], dlg.get_values()[0]]
                self.numb_description = ['documentType_3', 'documentNumber_3']

            else:
                try:
                    old_count = int(self.numb_description[-1].split('_')[-1])
                    self.count = str(old_count + 1)

                    new_lst = ['documentType_' + self.count, 'documentNumber_' + self.count]
                    self.numb_description.extend(new_lst)
                    self.numb_new_doc.extend([dlg.get_values()[1], dlg.get_values()[0]])
                except Exception as e:
                    print(e)


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


class New_doc(Ui_New_doc, QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(New_doc, self).__init__(*args, **kwargs)
        self.setupUi(self)
        QFontDatabase.addApplicationFont("RussoOne-Regular.ttf")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.current_cmb.addItems(type_doc_lv)
        self.current_cmb.setCurrentText(
            'NZZZ - Document equivalent to "ZZZ" defined in Commission Delegated Regulation (EU) 2016/341 (Appendix D2: Additional codes for the computerised transit system)')
        self.btn_ok.clicked.connect(self.accept)

    def get_values(self):
        return self.lne_nmb_doc.text(), self.current_cmb.currentText().split(' - ')[0]


class ProgressBarExample(Ui_Progress_calc, QProgressBar, QWidget):

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
