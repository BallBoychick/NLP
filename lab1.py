import numpy as np
import pandas as pd
ambit = 2
f = ['привет чурка также дурак любить чурка игры', 'bet boom 2drots amkal chisp']

count_vocab = set((' '.join(f).split()))
word_to_ix = {word: i for i, word in enumerate(count_vocab)}
print(word_to_ix)

def get_context_words(data, m):
    central_words = []
    context_words = []
    s = []
    print("m", m)
    for k in range(0, len(data)):
        for i in range(m, (len(data[k].split()) - (m * 2)) + (m)):
            # print(i)
            central_word = data[k].split()[i]
            central_words.append(word_to_ix[central_word])

            context_word = []
            for j in range(i - m, i + m + 1):
                if j != i:
                    context_word.append(word_to_ix[data[k].split()[j]])
            context_words.append(context_word)

    s = list(zip(central_words, context_words))

    return s

print(get_context_words(f, m=2))

# df = pd.DataFrame(s[0], columns=['Central_words'])
# df["Context_words"] = s[1]
# print(df)
# print(list(zip(s[0], s[1])))

# def get_ambit_of_word_by_id(word_id):
#     ambit_of_word = np.array([])
#     for i in range(word_id - ambit, word_id + ambit):
#         if i == word_id - ambit:
#             ambit_of_word = word_to_ix[c_v_2[i]]
#         if i != word_id:
#             w = word_to_ix[c_v_2[i]]
#             ambit_of_word = np.append(ambit_of_word, w(1, w), axis=0)
#     t = np.zeros(len(c_v_2))
#     t[word_to_ix[c_v_2[word_id]]] = 1
#     return ambit_of_word, t


# x, y = [], []
# start = ambit
# end = 100
# # end = len(corpus_of_text)-ambit
# for i in range(start, end):
#     x_i, y_i = get_ambit_of_word_by_id(i)
#     x.append(x_i)
#     y.append(y_i)

# print("X", x)
# print("Y", y)

# def generate_context_word_pairs(corpus, window_size, vocab_size):
#     context_length = window_size*2
#     # (prepro_text[0].split())[0]
#     for words in corpus:
#         print(words)
#         sentence_length = len(corpus)
#         print(sentence_length)
#         for index, word in enumerate(corpus):
#             context_words = []
#             label_word = []
#             start = index - window_size

#             end = index + window_size + 1
#             context_words.append([corpus[i] for i in range(start, end) if 0 <= i < sentence_length and i != index])
#             label_word.append(word)
#             print(context_words)
#             print(label_word)
#             # x = context_words
#             # y = label_word, vocab_size
#             # yield (x, y)
#             return 0
        
# generate_context_word_pairs(f, 4, len(count_vocab))
