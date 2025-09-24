import csv
from googletrans import Translator

translator = Translator()


def str_to_float(a):
    return float(a.replace(',', '.'))


def name_good(a, b):
    lst = a.split('.')
    if b in lst:
        return '.'.join(lst)
    else:
        if (len(a) + len(b)) < 99:
            lst.append(b.upper())
        return '.'.join(lst)


def weight(a, b):
    return round(a + b, 3)


def cost(a, b):
    return round(a + b, 2)


def trans_late(a):
    x = translator.translate(a)
    return x.text


d = {}
with open("D:\Документация\CSV\TSCOMPLEX T1.csv", 'r', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    for i in reader:
        if i[0][0:6] in d:

            d[i[0][0:6]] = [name_good(d[i[0][0:6]][0], i[1]), weight(d[i[0][0:6]][1], str_to_float(i[2])),
                            cost(d[i[0][0:6]][2], str_to_float(i[3]))]
        else:
            d[i[0][0:6]] = [i[1].upper()[:99], str_to_float(i[2]), str_to_float(i[3])]

lst = []
for k, v in d.items():
    lst.append([k, v[0], str(v[1]).replace('.', ','), str(v[2]).replace('.', ',')])

while True:
    s = input('Переводить текст y/n')
    if s == 'n':
        break
    elif s == 'y':
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                lst[i][1] = trans_late(lst[i][1])
        break

with open('D:\Документация\CSV\output.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(lst)
