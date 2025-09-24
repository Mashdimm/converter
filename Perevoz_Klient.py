import csv
import re
from difflib import get_close_matches

pattern = r'^П/'

perevozy = []

def find_matching_carriers(client_name, carriers, cutoff=0.7):
    """Ищет совпадения среди перевозчиков, используя нечеткое сравнение"""
    matches = get_close_matches(client_name, carriers, n=1, cutoff=cutoff)
    return matches[0] if matches else None

with open('perevozy.csv', 'r', newline='') as file:
    reader = csv.reader(file, delimiter=';')
    for perevoz in reader:

        perevoz = re.sub(pattern, '', ''.join(perevoz)).strip()
        perevozy.append(perevoz)
klient_perevoz = []
with open('Клиенты.csv', 'r', newline='') as file:
    line = csv.reader(file, delimiter=';')
    for row in line:
        klient_perevoz.append(row)

result_1 = []
for perevoz in perevozy:
    for klient in klient_perevoz:

        if perevoz == klient[0].upper().strip():
            result_1.append([perevoz] + klient)
        print(perevoz)
result_1 = sorted(result_1, key=lambda x: (x[5], x[0]))
with open('клиенты - перевозчики.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    #writer.writerow(['', 'Наименование', 'Примечание', 'Эл. почта', 'Контроль', 'Примечание к агенту', 'Почта (не для счетов)', 'Телефон'])
    for row in result_1:

        writer.writerow(row)
# result_2 = []
#
# for perevoz in perevozy:
#     for klient in klient_perevoz:
#         match = find_matching_carriers(perevoz, klient[0].upper().strip())
#         print(f'{perevoz} ** {match} ** {klient[0].upper().strip()}')
#         if match:
#             result_2.append([perevoz] + klient)
# print(len(result_1), '***', len(result_2))