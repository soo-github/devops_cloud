# 숫자 퀴즈
# 랜덤 숫자를 맞춰보세요.

# hint: random.randint를 통해 100이하의 랜덤수를 만듭니다.
# 유저에게 10회의 기회를 줍니다. - for문 / range
# 정답을 맞췄다면, 몇 번 만에 맞췄는지 출력
# 입력한 숫자가 랜덤수보다 작다면, '더 큰 수를 입력해주세요.' 라고 출력
# 입력한 숫자가 랜덤수보다 크다면, '더 작은 수를 입력해주세요.' 라고 출력
# 횟수를 초과하면 '다음 기회에......' 라고 출력

import random

random_num = random.randint(1, 100)
count = 1

for number in range(10):
    answer = input("숫자를 입력하세요.")
    if random_num == int(answer):
        print(f"{count}번 만에 정답 입니다!")
        break

    elif random_num > int(answer):
        count += 1
        print("오답 입니다... 높은 수를 입력하세요.")

    elif random_num < int(answer):
        count +=1
        print("오답 입니다... 낮은 수를 입력하세요.")

if count == 11:
    print("다음 기회에.....")