N = int(input())

B = list()
S = list()
D = list()

int_to_char = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for _ in range(N):
    temp = list(map(str, input().split()))
    B.append(int(temp[0]))
    S.append(temp[1])
    D.append(temp[2])


def cal(b, s, d):
    signed = 1
    if s == '0' or d == '0':
        return 0

    if '-' in s:
        signed *= -1
        s = s.lstrip('-')

    if '-' in d:
        signed *= -1
        d = d.lstrip('-')

    if signed == -1:
        print('-', end='')

    result = [0] * (len(s)+len(d)-1)
    s_int = list()
    d_int = list()
    for c in s:
        if '0' <= c <= '9':
            s_int.append(int(ord(c)-ord('0')))
        else:
            s_int.append(int(ord(c)-ord('A'))+10)

    for c in d:
        if '0' <= c <= '9':
            d_int.append(int(ord(c)-ord('0')))
        else:
            d_int.append(int(ord(c)-ord('A'))+10)

    for i in range(len(s_int)):
        for j in range(len(d_int)):
            result[i+j] += s_int[i]*d_int[j]

    for i in range(len(result)-1, 0, -1):
        if result[i] >= b:
            result[i-1] += result[i]//b
            result[i] %= b

    if result[0] >= b:
        print(int_to_char[result[0]//b], end='')
        result[0] %= b

    str_result = list()
    for i in range(len(result)):
        str_result.append(int_to_char[result[i]])

    return ''.join(str_result)


for i in range(N):
    print(cal(B[i], S[i], D[i]))
