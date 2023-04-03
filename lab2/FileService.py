import re
from collections import Counter
def read_file(file):
    text = ""
    for line in file:
        text += line
    return text


def sentences_counter(text):
    result = [0, 0]
    reg_ex_non_dec = r"[^a-zA-Z0-9\s]*(?:\.{3}|\.)"
    # reg_ex_non_dec = r"[^.!?]*(?:\.{3}|\.)"
    reg_ex_dec = r"[^.!?]*(?:[!?])"

    result[0] = len(re.findall(reg_ex_non_dec, text))+len(re.findall(reg_ex_dec, text))
    result[1] = len(re.findall(reg_ex_non_dec, text))
    return result


def average_sent(text):
    reg_ex_sent = r"[^.!?]*[\w']+[^.!?]*[.!?]"
    print(re.findall(reg_ex_sent, text))
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


def repeats(text, n, k):
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    words = cleaned_text.split()
    ngrams = [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]
    ngram_counts = Counter(ngrams)
    return ngram_counts.most_common(k)



