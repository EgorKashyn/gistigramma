import matplotlib.pyplot as plt
with open('Уэллс_-_Война_миров.txt') as file:
    text = file.read()
    print(f'количество символов с пробелами:{len(text)}')
    print(f'количество символов без пробелов:{len(text.replace(" ", ""))}')
    a=text.split("\n")
    print(f'количество строк:{len(a)}')
    text = text.replace("\n", " ").replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace(":", "").replace(";", "").replace("«", "").replace("»", "").replace("°", "").replace("-", "").replace("–", "").replace("…", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "")
    text = text.lower()
    words = text.split()
print(f'количество слов:{len(words)}')

d_words={}
for i in words:
    if i in d_words:
        d_words[i]+=1
    else:
        d_words[i]=1


sorted_d_words=dict(sorted(d_words.items(), key=lambda item: item[1]))
words20=list(sorted_d_words.keys())[-20:]
values20=[sorted_d_words[i] for i in words20]


plt.bar(words20,values20)
plt.show()
