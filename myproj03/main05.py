# 구구단 2~9단 (break 없이)

for number in range(2, 10):
    for i in range(1, 10):
        if number >= i:
            print(f"{number} * {i} = {number*i}")
