from itertools import combinations as cb
from sys import stdin
input = stdin.readline

common_alphabet = {'a','c','i','n','t'}
input_word = []

input_alphabet_set = set()
n, k = map(int, input().split())
k -= 5

for nn in range(n):
    # anta [필요한 것들] tica, 그리고 필요한 것들에서 a c i n t 제거
    word = set(input().rstrip()[4:-4]).difference(common_alphabet)
    # a c i n t를 제외하고 나타난 알파벳 목록들 (중복 X)
    input_alphabet_set.update(word)
    # a c i n t를 소거한 단어 리스트
    input_word.append(list(word))

if k < 0:
    print(0)
    exit()

# a c i n t를 소거한 단어 리스트를 비트연산 할 수 있도록 변경 
input_word_bit = []
for ii in input_word:
    current_bit = 0
    for alpha in ii:
        current_bit |= 1 << ord(alpha) - ord('a')
    input_word_bit.append(current_bit)

combi = cb(input_alphabet_set, min(k, len(input_alphabet_set)))
max_count = 0
for cc in combi:
    count = 0
    alphabet_bit = 0
    for alpha in cc:
        alphabet_bit |= 1 << ord(alpha) - ord('a')
    for ii in input_word_bit:
        if alphabet_bit & ii == ii:
            count +=1
    max_count = max(max_count, count)

print(max_count)
