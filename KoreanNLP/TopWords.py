import csv
from random import randint


class TopWords:

    def __init__(self):
        self.words = self.get_word_list()

    def get_word_list(self):
        file = 'top_1000_words.csv'
        word_list = []
        with open(file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                word_list.append(list(row.values()))

        return word_list

    def generate_random_word(self):
        rand_idx = randint(0, len(self.words)-1)
        return self.words[rand_idx][1]
