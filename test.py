
N = 5


with open('russian_nouns.txt', 'r', encoding="utf-8") as f:
    # Создаем список слов из файла
    words = [line.strip() for line in f.readlines()]


word_dict = {}
for word in words:
    suffix = word[-N:]
    if suffix in word_dict:
        word_dict[suffix].append(word)
    else:
        word_dict[suffix] = [word]


for word in words:
    prefix = word[:N]
    if prefix in word_dict:
        for match in word_dict[prefix]:
            if match != word:
                print(match[:-N] + word)


