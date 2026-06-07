# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
# маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
# – все остальные. Посчитать количество полученных строк в каждом файле


import re

with open("ip_address.txt", "r", encoding="utf-8") as f:
    content = f.read()

masks_section = re.search(r"Частоупотребимые маски\s*\n([\s\S]*?)(?=\n[^\d\.])", content)
masks = masks_section.group(1).strip().splitlines() if masks_section else []

last_octet = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.0$")

file1_lines = list(filter(lambda ip: last_octet.match(ip), masks))

file2_lines = list(filter(lambda ip: not last_octet.match(ip), masks))

with open("file1.txt", "w", encoding="utf-8") as f1:
    f1.write("\n".join(file1_lines))

with open("file2.txt", "w", encoding="utf-8") as f2:
    f2.write("\n".join(file2_lines))

print(f"Количество строк в первом файле (нулевой 4-й октет): {len(file1_lines)}")
print(f"Количество строк во втором файле (остальные): {len(file2_lines)}")