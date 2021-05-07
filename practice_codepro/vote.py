c_dict = dict()

c_cnt = int(input())

temp = input().split()

for i in range(c_cnt):
    c_dict[temp[i]] = [i, 0]

v_cnt = int(input())

for i in range(v_cnt):
    temp = input().split()
    if temp[0] in c_dict.keys():
        v = c_dict[temp[0]]
        v[1] += int(temp[1])
        c_dict[temp[0]] = v

sdict = sorted(c_dict.items(), key=lambda i: i[1][1], reverse=True)

for i in range(3):
    print(sdict[i][0], sdict[i][1][1])
