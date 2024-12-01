string = input('Введите слова, разделённые пробелами: ')

words = string.split()

reversed_words = [word[::-1] for word in words]

sorted_words = sorted(reversed_words)

print('\nСлова с реверсированными буквами в алфавитном порядке: ')

for word in sorted_words:
    print(word)

