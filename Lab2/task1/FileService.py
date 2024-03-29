import re
from collections import Counter

abbreviations = ['Mr', 'Mrs', 'Dr', 'etc', 'Prof', 'Gen', 'Sgt', 'Col', 'Capt', 'Lt', 'Rev', 'Hon', 'Pres', 'Gov',
                 'Sen']


def read_file(file):
    text = ""
    for line in file:
        text += line
    return text


def sentences_counter(text):
    result = [0, 0]
    reg_ex_all_sent = r"\s*([^.?!]+)[.?!]"
    all_sentences = re.findall(reg_ex_all_sent, text)
    amount = len(all_sentences)
    for item in all_sentences:
        if item in abbreviations:
            amount -= 1
    result[0] = amount
    result[1] = len(re.findall(r"[!?]+", text))

    return result


def average_sent(text):
    sent_reg_ex = r"\s*([^.?!]+)[.?!]"
    all_length = 0
    reg_ex = r"\W+"
    reg_ex_digit = r"\d+"
    words = re.split(reg_ex, text)
    filtered_words = [word for word in words if not re.match(reg_ex_digit, word) and len(word) > 0]
    for item in filtered_words:
        all_length += len(item)
    sentences = re.findall(sent_reg_ex, text)
    amount = len(sentences)
    for item in sentences:
        for abb in abbreviations:
            if item == abb:
                amount -= 1

    return round(all_length/amount)


def average_word(text):
    all_length = 0
    reg_ex = r"\W+"
    reg_ex_digit = r"\d+"
    words = re.split(reg_ex, text)
    filtered_words = [word for word in words if not re.match(reg_ex_digit, word) and len(word) > 0]
    for item in filtered_words:
        all_length += len(item)

    return round(all_length / (len(filtered_words)))


def repeats(text, n, k):
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    words = cleaned_text.split()
    ngrams = [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]
    ngrams_dict = {}
    for item in ngrams:
       if item not in ngrams_dict.keys():
           ngrams_dict.update({item: 1})
       else:
           ngrams_dict[item] += 1
    result_list = sorted(ngrams_dict.items(), key = lambda elem: elem[1], reverse=True)

    return tuple(result_list[0:k])