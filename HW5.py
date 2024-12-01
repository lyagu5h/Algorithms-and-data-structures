def reverse_words_in_string() -> str:
    s: str = input('Enter a string: ')
    words: list = s.split(' ')
    reversed_words: list = []

    for word in words:
        letters_only: list = [char for char in word if char.isalnum()]
        reversed_word: list = [];

        for char in word: 
            if char.isalnum():
                reversed_word.append(letters_only.pop())
            else:
                reversed_word.append(char)

        reversed_words.append(''.join(reversed_word))

    return ' '.join(reversed_words)

print('Слова в обратном порядке: ', reverse_words_in_string())
print('Слова в обратном порядке: ', reverse_words_in_string())