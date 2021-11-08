s = "안녕하세요"

for ch in s:
    print(ch)

for idx, ch in enumerate(s, 1):
    print(idx, ch)


numbers = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],

]

for idx, [x, y] in enumerate(numbers):
    print(x, y)
