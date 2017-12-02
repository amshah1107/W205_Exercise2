import csv
import matplotlib.pyplot as plt
import numpy as np


with open("top20.txt") as csvfile:
    wordlist = []
    word_count = []
    reader = csv.reader(csvfile,delimiter=":")
    for row in reader:
        wordlist.append(row[0].strip())
        word_count.append(int(row[1]))
    y_pos = np.arange(len(wordlist))
    plt.bar(y_pos, word_count, align = 'center', alpha=0.5)
    plt.xticks(y_pos, wordlist)
    plt.ylabel('frequency')
    plt.title('Top 20 words')
    plt.show()

