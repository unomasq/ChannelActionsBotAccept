n = 4

with open("russian_nouns.txt", "r", encoding="utf-8") as f:
    words = f.read().split()

for i, word_i in enumerate(words):
    for j, word_j in enumerate(words):
        if i != j and word_i[-n:] == word_j[:n] and word_i[:-n] + word_j not in words:
            print(word_i[:-n] + word_j)
            break
