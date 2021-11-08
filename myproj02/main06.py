# 구구단

def gugudan(number):  # 함수정의
    # number = 2
    print(f"### {number}단 ###")
    for i in range(1,10):
        print(f"{number} * {i} = {number * i}")


# gugudan(2)
# gugudan(3)
# gugudan(4)
# gugudan(5)
# gugudan(6)
# gugudan(7)
# gugudan(8)
# gugudan(9)

for j in range(2,10):
    gugudan(j)
