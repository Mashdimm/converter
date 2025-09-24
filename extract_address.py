import re
from typing import Tuple

# БАЗОВЫЙ токен: число + (опц. буквы) + (опц. блоки / или - с числами и буквами)
BASE_TOKEN = r"""
(?:
    (?:No\.?|Nr\.?|N|№)\s*   # опциональный префикс No/Nr/N/№ с точкой или без
)?
(
    \d+                      # цифры
    (?:[A-Za-z]+)?           # опц. буквы сразу после цифр (10A, 10AB)
    (?:[\/\-]\d+[A-Za-z]*)*  # опц. блоки: /1, -12B
)
"""

# РАСШИРЕННЫЙ токен: как базовый, но разрешает "склеенные" хвосты (напр. Halle E3)
EXTENDED_TOKEN = r"""
(?:
    (?:No\.?|Nr\.?|N|№)\s*
)?
(
    \d+
    (?:[A-Za-z]+)?
    (?:[\/\-]\d+[A-Za-z]*)*
    (?:[ ]?(?:[A-Za-z]+[A-Za-z0-9]*))*   # хвосты типа "Halle E3", "BIS", "BLDG2"
)
"""

BASE_RE = re.compile(BASE_TOKEN, re.IGNORECASE | re.VERBOSE)
EXT_RE  = re.compile(EXTENDED_TOKEN, re.IGNORECASE | re.VERBOSE)


def extract_street_and_number(addr: str) -> Tuple[str, str]:
    """
    Извлекает номер дома из адресной строки (латиница).
    Возвращает: (адрес_без_номера, номер). Если номер не найден — (исходный_адрес, '').

    Правило:
      - если номер стоит в начале строки -> берём ТОЛЬКО базовый номер (без хвостов)
      - если номер не в начале -> пытаемся расширить до склеенных хвостов (напр. 'Halle E3')
    """
    if not addr:
        return "", ""

    s = addr.strip()
    matches = list(BASE_RE.finditer(s))
    if not matches:
        return s, "-"

    # Берём самый "содержательный" матч: по длине числа/диапазона (при равенстве — более правый)
    m = max(matches, key=lambda m: (len(m.group(1)), m.start()))
    start, end = m.span(0)
    number = m.group(1).strip()

    # Если номер НЕ в начале — пробуем расширить матч, чтобы подцепить "склеенные" хвосты (Halle E3 и т.п.)
    if start > 0:
        m2 = EXT_RE.match(s[start:])
        if m2:
            number = m2.group(1).strip()
            end = start + m2.end(0)

    before = s[:start].rstrip(",; \t")
    after  = s[end:].lstrip(",; \t")

    # Собираем новую адресную строку без номера
    new_addr = (before + (" " if before and after else "") + after).strip()
    new_addr = re.sub(r"\s{2,}", " ", new_addr)

    return new_addr, number



