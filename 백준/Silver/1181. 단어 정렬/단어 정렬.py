N= int(input())
words = []
for i in range(N):
    word = input()
    words.append(word)
words = list(dict.fromkeys(words))
words.sort()
words.sort(key=len)

print(*words, sep = "\n")