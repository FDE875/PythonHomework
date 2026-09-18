
text = input("Enter a string: ")
start_word = input("Starts with: ")
end_word = input("Ends with: ")
if text.startswith(start_word) and text.endswith(end_word):
print("True")
else:
print("False")