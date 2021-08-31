from sys import stdin
input = stdin.readline

test_case = int(input())

# for _ in range(test_case):
#     contact = set()
#     contact_num = int(input())
#     for _ in range(contact_num):
#         contact.add(input().rstrip())
#     found = False
#     for cc in list(contact):
#         # 끝까지 볼 경우 자기 자신과 비교하게 되기 때문에 len(cc)+1이 아닌 len(cc)
#         for part in range(1, len(cc)):
#             if cc[:part] in contact:
#                 found = True
#                 break
#         if found:
#             break
#
#     print('NO' if found else 'YES')

for _ in range(test_case):
    contact = []
    contact_num = int(input())

    for _ in range(contact_num):
        contact.append(input().rstrip())

    contact.sort()
    found = False
    for ii in range(1, contact_num):
        prev = contact[ii-1]
        if contact[ii][:len(prev)] == prev:
            found = True
            break

    print('NO' if found else 'YES')
