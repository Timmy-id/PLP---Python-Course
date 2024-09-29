words_list = input('Enter words separated by space ').split()

odd_len_of_words = [word for word in words_list if len(word) % 2 == 1]

print(odd_len_of_words)