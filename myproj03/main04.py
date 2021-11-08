# 구구단 3단, 6단, 9단만 출력

for number in range(2, 10):
    for i in range(1, 10):
        if number % 3 == 0:
            print(f"{number} * {i} = {number*i}")
