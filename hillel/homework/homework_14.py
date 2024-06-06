# Author: Maksim Derevianko

import os

path_file = 'files/romeo.txt'

with open(path_file, mode='r') as file:
    text_file = file.read()
    text_file = text_file.replace('\n', ' ')
    punctuation = '!,.:;?'
    for char in punctuation:
        text_file = text_file.replace(char, "")
    words = text_file.split(' ')
    alpha_words = []
    for word in words:
        if word.isalpha():
            alpha_words.append(word)
    longest_alpha_word = ''
    for alpha_word in alpha_words:
        if len(alpha_word) > len(longest_alpha_word):
            longest_alpha_word = alpha_word
    print(f'Найдовше слово у тексті: {longest_alpha_word}')
    print(f'Кількість літер у найдовшому слові: {len(longest_alpha_word)}')
