import os
import string
from collections import Counter

FILE_NAME = "sample.txt"
REPORT_FILE = "word_count_report.txt"

# 1. File Input: sample.txt mavjudligini tekshirish
if not os.path.exists(FILE_NAME):
    print(f"'{FILE_NAME}' fayli topilmadi.")
    user_text = input("Iltimos, matn (paragraf) kiriting: ")
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write(user_text)

# 2. Faylni o'qish va so'zlarni sanash
try:
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    content = ""

# Tinish belgilarini olib tashlash va barchasini kichik harfga o'tkazish
translator = str.maketrans("", "", string.punctuation)
cleaned_content = content.translate(translator).lower()

words = cleaned_content.split()
total_words = len(words)

# Eng ko'p uchraydigan so'zlarni aniqlash
word_counts = Counter(words)
top_5 = word_counts.most_common(5)

# 3. Konsolga chiqarish
print(f"\nTotal words: {total_words}")
print("Top 5 most common words:")
for word, count in top_5:
    time_str = "time" if count == 1 else "times"
    print(f"{word} - {count} {time_str}")

# 4. Natijani word_count_report.txt fayliga saqlash
report_content = [
    "Word Count Report\n",
    f"Total Words: {total_words}\n",
    "Top 5 Words:\n"
]
for word, count in top_5:
    report_content.append(f"{word} - {count}\n")

with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.writelines(report_content)

print(f"\nHisobot '{REPORT_FILE}' fayliga muvaffaqiyatli saqlandi!")
