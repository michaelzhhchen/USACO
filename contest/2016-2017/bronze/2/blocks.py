fin = open ('blocks.in', 'r')
fout = open ('blocks.out', 'w')

letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = int(fin.readline())

for i in range(num):
    word1, word2 = fin.readline().strip().split()
    for i in range(26):
        x = word1.count(letterList[i])
        y = word2.count(letterList[i])
        if x >= y:
            letters[letterList[i]] += x
        else:
            letters[letterList[i]] += y

for i in range(26):
    x = letters.get(letterList[i])
    fout.write (str(x) + '\n')

fout.close()
