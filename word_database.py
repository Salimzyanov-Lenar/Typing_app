file_path = "words_data.txt"

with open (file_path,"r", encoding='UTF-8') as file:
    word_database = file.read().split()