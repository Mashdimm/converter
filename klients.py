import pandas as pd

# === 1. Загрузка CSV ===
clients_df = pd.read_csv('Клиенты.csv', encoding='cp1251', sep=';', on_bad_lines='skip')
invoices_df = pd.read_csv('Счета.csv', encoding='cp1251', sep=';', on_bad_lines='skip')

# === 2. Очистка и нормализация названий клиентов ===
clients_df = clients_df[['Наименование', 'Контроль']].dropna(subset=['Наименование'])
clients_df['Клиент_норм'] = clients_df['Наименование'].str.strip().str.lower().str.replace('"', '', regex=False)

invoices_df['Клиент'] = invoices_df['Заказчик'].astype(str).str.strip().str.lower().str.replace('"', '', regex=False)
clients_df['Контроль'] = clients_df['Контроль'].fillna('Без контроля')

# === 3. Преобразование данных по счетам ===
invoices_df['Сумма'] = invoices_df['Сумма'].str.replace(',', '.').str.replace(' ', '')
invoices_df['Сумма'] = pd.to_numeric(invoices_df['Сумма'], errors='coerce')

invoices_df['Дата акта'] = pd.to_datetime(invoices_df['Дата акта'], format='%d.%m.%Y', errors='coerce')
invoices_df = invoices_df[invoices_df['Дата акта'].dt.year == 2025]
invoices_df['Месяц'] = invoices_df['Дата акта'].dt.to_period('M').astype(str)

# === 4. Объединение по нормализованным названиям ===
df = invoices_df.merge(clients_df, left_on='Клиент', right_on='Клиент_норм', how='left')

# === 5. Группировка по клиенту, валюте и месяцу ===
df['Наименование'] = df['Наименование'].fillna(df['Заказчик'])  # если не найдено в справочнике — оставить оригинальное имя

grouped = df.groupby(['Наименование', 'Контроль', 'Валюта', 'Месяц'])['Сумма'].sum().reset_index()

# === 6. Сводная таблица (pivot) ===
pivot = grouped.pivot_table(
    index=['Наименование', 'Контроль', 'Валюта'],
    columns='Месяц',
    values='Сумма',
    aggfunc='sum',
    fill_value=0
).reset_index()

# === 6.1 Сортировка по полю Контроль ===
pivot = pivot.sort_values(by=['Контроль', 'Наименование'])

# === 7. Сохранение в Excel ===
pivot.to_excel('Сводная_по_клиентам_с_валютами.xlsx', index=False)

print("✅ Готово! Файл: Сводная_по_клиентам_с_валютами.xlsx")

