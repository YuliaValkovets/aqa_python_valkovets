# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

word = ''
letter = 'h'
while letter not in word.lower():
    word = input("Enter any words that contain the character 'h' or 'H': ")
print("Excellent, this word contains the required character")

