f = ['привет чурка также дурак любить чурка также', 
     'водосточный труба окрасить требоваться окрасить чурка']
# s1 = len(set(f[0].split()))
# s2 = len(set(f[1].split()))
# print(s1, s2)
# print(len(f))

abc = set((' '.join(f).split()))
#приплести сюда индекс слова
word_to_ix = {word: i for i, word in enumerate(abc)}
print(word_to_ix)
a = max(word_to_ix.values()) + 1
matrica = [[0] * a for _ in range(a)]
# print(words)
for k in range(0, len(f)):
    # s1 = len(set(f[k].split()))
    b = len(f[k].split())
    words = f[k].split()
    for i in range(b):
        # print("I", i)
        for j in range(i+1, b):
            if words[i] + " " + words[j] in f[k] and (abs(i - j) == 1):
                print(words[i], " ", words[j])
                print(word_to_ix[words[i]], " ", word_to_ix[words[j]])

                matrica[word_to_ix[words[i]]][word_to_ix[words[j]]] += 1

for row in matrica:
    print(row)


# print(word_to_ix[words[0]])
# lookup = {value: key for key, value in word_to_ix.items()}
# print(lookup)
# print(lookup[0])