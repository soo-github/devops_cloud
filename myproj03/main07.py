# 1이상 100미만 범위에서 3과 5의 공배수를 합을 출력하기

sum = 0

for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        sum += num
print(sum)
