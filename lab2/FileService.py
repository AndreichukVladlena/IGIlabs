import re
from collections import Counter
def read_file(file):
    text = ""
    for line in file:
        text += line
    return text


def sentences_counter(text):
    result = [0, 0]
    flag = True
    for symbol in text:
        if symbol == "." and flag:
            flag = False
            result[0] += 1
        elif symbol == "!" or symbol == "?":
            flag = True
            result[0] += 1
            result[1] += 1
        elif symbol != ".":
            flag = True
    return result


def average_sent(text):
    amount = 0
    all_length = 0
    temp_length = 0
    for symbol in text:
        if symbol == "." or symbol == "\n" or symbol == "!" or symbol == "?":
            if temp_length != 0:
                amount += 1
                all_length += temp_length
                temp_length = 0
        elif symbol == " " or symbol == "\n":
            continue
        else:
            temp_length += 1
    if amount == 0:
        amount = 1
    return int(all_length / amount)


def average_word(text):
    amount = 0
    all_length = 0
    temp_length = 0
    for symbol in text:
        if symbol == " " or symbol == "\n" or symbol == "." or symbol == "!" or symbol == "?":
            if temp_length != 0:
                amount += 1
                all_length += temp_length
                temp_length = 0
        else:
            temp_length += 1
    if amount == 0:
        amount = 1
    return int(all_length / amount)


def repeats(text):
    reg_ex = r" *([^!?. ]+)[!|?|.| ]"
    ngrams = re.findall(reg_ex, text)
    result = Counter(ngrams).most_common(1)
    return result
