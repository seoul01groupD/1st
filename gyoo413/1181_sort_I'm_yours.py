n = int(input())
word_list = []
for i in range(n):
    word_list.append(input())

word_with_len = []
for word in word_list:
    if word not in word_with_len:
        word_with_len.append(word)
for i in range(len(word_with_len)):
    word_with_len[i] = [word_with_len[i], len(word_with_len[i])]

#word_with_len.sort(key = lambda word_with_len: (word_with_len[1], word_with_len[0]))

for word in word_with_len:
    print(word[0])
