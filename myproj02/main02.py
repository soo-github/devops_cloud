answer = input("12 + 23 = ")

# answer를 가지고 계산할 목적이라면,
# answer 값 변환은 최대한 빠르게 수행하는 것이 좋습니다.
# answer = int(answer or 0) 값을 입력 안하고 엔터를 칠 경우 오답이 나오게 함.

# if answer == "35":
#     print("정답!")
# else:
#     print("오답!!!")


answer = int(answer or 0) 

if answer == 35:
    print("정답!")
else:
    print("오답!!!")


