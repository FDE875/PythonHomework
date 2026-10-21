import os
import re
from collections import Counter

filename = "sample.txt"
report_filename = "word_count_report1.txt"

if not os.path.exists(filename):
    print("sample.txt fayli mavjud emas.")
    text = input("Matn kiriting: ")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

with open(filename, "r", encoding="utf-8") as file:
    text = file.read()

text = text.lower()

words = re.findall(r"\b[^\W\d_]+\b|\b\d+\b", text)

total_words = len(words)

word_counts = Counter(words)

top_words = word_counts.most_common(5)

print(f"\nTotal words: {total_words}")
print("Top 5 most common words:")

for word, count in top_words:
    print(f"{word} - {count} times")

with open(report_filename, "w", encoding="utf-8") as file:
    file.write("Word Count Report\n")
    file.write(f"Total Words: {total_words}\n")
    file.write("Top 5 Words:\n")

    for word, count in top_words:
        file.write(f"{word} - {count}\n")

print(f"\nHisobot '{report_filename}' fayliga saqlandi.")