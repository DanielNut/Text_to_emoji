import demoji
import requests
import json
import os


def reverse_dict(input: dict) -> dict:
    res = {}
    for k, v in input:
        if v in res:
            continue
        else:
            res[v] = k


with open('emojis.json', 'r') as emojis_file:
    emojis = dict(json.load(emojis_file))
    emojis = dict(sorted(emojis.items(), key=lambda x: len(x[1]), reverse=True))


def is_seq_in_text(text, seq):
    is_in_sentence = text.find(' ' + seq + ' ') != -1
    is_start_of_sentence = text.find(seq + ' ') != -1
    if_end_of_sentence = text.find(' ' + seq) != -1
    return is_in_sentence or is_start_of_sentence or if_end_of_sentence


text = input()
text_words = text.split(' ')
for i in emojis.keys():
    if emojis[i] in text_words or is_seq_in_text(text, emojis[i]):
        text = text.replace(emojis[i], i)
print(text)
