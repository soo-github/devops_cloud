
from random import randint

number = randint(1, 100)

for retry in range(1, 11):
    line = input(f"[{retry}] Try guess number : ")
    answer = int(line.strip() or 0)   # strip 문자열의 좌우 공백을 없애줌

    if answer == number:
        print(f"{retry}회 시도에 성공했습니다.")
        break
    elif answer < number:
        print("더 큰 수를 입력해주세요.")
    elif answer > number:
        print("더 작은 수를 입력해주세요.")
else:
    print("다음 기회에....")
