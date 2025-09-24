import pandas as pd
import re

# === путь к исходному CSV ===
INPUT_FILE = "CN.csv"
OUTPUT_FILE = "hs8_codes.csv"

# читаем файл (одна колонка с кодами, без заголовка)
df = pd.read_csv(INPUT_FILE, header=None, dtype=str, encoding="utf-8")

codes = []
for val in df[0].dropna():
    # оставляем только цифры
    digits = re.sub(r"\D", "", str(val))
    # фильтруем только 8-значные
    if len(digits) == 8:
        codes.append(digits)

# убираем дубликаты и сортируем
unique_codes = sorted(set(codes))
print(unique_codes)

# сохраняем в новый CSV
pd.DataFrame({"hs8_code": unique_codes}).to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

print(f"Найдено {len(unique_codes)} кодов, сохранено в {OUTPUT_FILE}")
