from sys import stdin
input = stdin.readline

bomb_string = input().rstrip()
bomb = list(input().rstrip())

# 주석 해제 시 조금 더 빠름
# last_character = bomb[-1]
bomb_len = len(bomb)
no_bomb = []

for bb in bomb_string:
    no_bomb.append(bb)
    # if bb != last_character:
    #     continue
    if no_bomb[-bomb_len:] == bomb:
        for _ in range(0, bomb_len):
            no_bomb.pop()

print(''.join(no_bomb) if no_bomb else 'FRULA')
