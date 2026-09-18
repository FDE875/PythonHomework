word = input("Enter a word: ")
unlilar = "aeiou"
result = word
for harf in word:
    if harf in unlilar:result = result.replace(harf, "*")
print(result)