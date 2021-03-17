# page 115

# ord("A") -> 문자에 해당하는 아스키 코드 return
# chr(65) -> 숫자에 대응하는 문자 return

input_data = input()
c = ord(input_data[0]) - ord("a") + 1
r = int(input_data[1])

move = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2)]

result = 0

for n in move:
    next_c = n[0] + c
    next_r = n[1] + r
    if 1 <= next_c <= 8 and 1 <= next_r <= 8:
        result += 1

print(result)
