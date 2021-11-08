# 구구단 3,6,9 출력
number = 3
for i in range(1,10):
    print(f"{number} * {i} = {number * i}")



# 1이상 100미안의 숫자 중 3,5의 공배수 출력
for i in range(1,100):
    if i % 3 == 0 and i % 5 ==0:
        print(i)

for i in range(15,100,15):
    print(i)

for i in range(1,100):
    if i % 15 ==0:
        


# 1이상 100미안의 숫자 중 3,5의 공배수의 합 출력
acc = 0
for i in range(1,100):
    if i % 3 == 0 and i % 5 ==0:
        acc += i
print(acc)

number_list = []
for i in range(1,100):
    if i % 3 == 0 and i % 5 ==0:
        number_list.append(i)
print(sum(number_list))



# 구구단 2*1~2*2, 3*1~3*3, 4*1~4*4 ... 출력되도록
for number in range(2,10):
    for i in range(1,10):
        if i <= number:
            print(f"{number} * {i} = {number * i}")






