import pandas as pd

# === 1. Читаем файлы ===
file1 = "clean.csv"    # готовый первый файл с 8-значными кодами
file2 = "fg.csv"   # второй CSV с кодами для обработки

df1 = pd.read_csv(file1, header=None, dtype=str, sep=';')
df2 = pd.read_csv(file2, header=None, dtype=str)

# === 2. Создаём множество первых 8 символов из первого файла ===
set8 = set(df1[0].str[:8])
print(set8)

# === 3. Функция для деления на два столбца ===
def split_code(code):
    code = code.replace(' ', '')  # удаляем пробелы
    first8 = code[:8]
    if first8 in set8:
        # 8 символов → 6 + 2
        return pd.Series([first8[:6], first8[6:]])
    else:
        # 6 символов → первый столбец 6, второй пустой
        return pd.Series([code[:6], ''])

# === 4. Применяем функцию ===
df2[['col1', 'col2']] = df2[0].apply(split_code)

# === 5. Сохраняем CSV с разделителем ';' для Excel ===
output_file = "second_final.csv"
df2[['col1', 'col2']].to_csv(output_file, index=False, header=False, sep=';', quoting=0)

print(f"Готово! Файл сохранён как {output_file}")





