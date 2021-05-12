import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from TopWords import TopWords
from tweetGenerator import TweetGenerator
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)
window = tk.Tk()
window.title("Korean Tweet Generator")
window.geometry('630x750')
window.resizable(False, False)

title_label = tk.Label(window, text="Top 1000 Most Frequently Used Korean Words on Twitter")
title_label.grid(row=0, column=0)

tg = TweetGenerator()

columns = ('#1', '#2', '#3')
tree = tk.ttk.Treeview(window, columns=columns, show='headings')
tree.heading('#1', text='Rank')
tree.heading('#2', text='Name')
tree.heading('#3', text='Frequency')
top_words = TopWords()
for item in top_words.words:
    tree.insert('', tk.END, values=item)
tree.grid(row=1, column=0, sticky='nsew')
scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=1, sticky='ns')
s = ttk.Style()
s.configure('Treeview', rowheight=40)


def set_random_word():
    word = top_words.generate_random_word()
    random_word_label.configure(text=word)
    random_word_label.update()


def set_random_tweet():
    tweet = tg.generate_tweet()
    count = 0
    text = ''
    for character in tweet:
        if (character == ' ' and count > 20) or (count > 30):
            text += '\n'
            count = 0
        text += character
        count += 1
    random_tweet_label.configure(text=text)


random_word_button = tk.Button(window, text='Random Word', command=set_random_word)
random_word_button.grid(row=2, column=0)

random_word_label = tk.Label(window, text='', font=tkFont.Font(size=20))
random_word_label.grid(row=3, column=0)

random_tweet_button = tk.Button(window, text='Generate a Tweet', command=set_random_tweet)
random_tweet_button.grid(row=4, column=0)

random_tweet_label = tk.Label(window, text='')
random_tweet_label.grid(row=5, column=0)

window.mainloop()
