from FileService import sentences_counter
from FileService import average_sent
from FileService import average_word
from FileService import read_file
from FileService import repeats

f = open('text.txt', 'r')
sentencesAmount = [0, 0]
text = read_file(f)

sentencesAmount[0] = sentences_counter(text)[0]
sentencesAmount[1] = sentences_counter(text)[1]

print("amount of sentences in the text: ", sentencesAmount[0])
print("amount of non-declarative sentences in the text: ", sentencesAmount[1])
print("average length of the sentence: ", average_sent(text))
print("average length of the word: ", average_word(text))
print("Enter K and N for count top-K repeated N-grams in the text: ")
K = int(input())
N = int(input())
print("top-K repeated N-grams in the text: ", repeats(text, N, K))