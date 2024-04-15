import demoji
import requests
import json
import os
import re

ENDERS = ['.', ',', ';', ':']
CAPITAL_PRE_ENDERS = ['.', ';']
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


def is_seq_in_text(text, seq, emoji):
    is_in_sentence = text.find(' ' + seq + ' ') != -1
    is_start_of_sentence = text.find(seq + ' ') != -1
    is_end_of_sentence = False
    for ender in ENDERS:
        if_end_of_sentence = text.find(' ' + seq + ender) != -1
        if is_end_of_sentence:
            break
    return is_in_sentence or is_start_of_sentence or is_end_of_sentence

def replace_seq_in_text(text, seq, emoji):
    text = text.replace(' ' + seq + ' ', ' ' + emoji + ' ')
    seq_capital = ''
    if len(seq.split(' ')) > 1:
        seq_capital = ' '.join([seq.split(' ')[0].capitalize()] + seq.split(' ')[1:])
    else:
        seq_capital = seq.capitalize()
    text = text.replace(' ' + seq + ' ', ' ' + emoji + ' ')
    for ender in ENDERS:
        text = text.replace(ender + seq + ' ', ender + emoji + ' ')
        text = text.replace(ender + seq + ender, ender + emoji + ender)
        text = text.replace(ender + seq + ' ', ender + emoji + ' ')
        text = text.replace(' ' + seq + ender, ' ' + emoji + ender)
    if seq_capital:
        for pre_ender in CAPITAL_PRE_ENDERS:
            for ender in ENDERS:
                text = text.replace(pre_ender + seq_capital + ' ', pre_ender + emoji + ' ')
                text = text.replace(pre_ender + seq_capital + ender, pre_ender + emoji + ender)
    return text

text = input()
text_words = text.split(' ')
for i in emojis.keys():
        substr = emojis[i]
        substr_capital = ' '.join([substr.split(' ')[0].capitalize()] + substr.split(' ')[1:])
        text = replace_seq_in_text(text, substr, i)


print(text)
