import random
import time

animal_names = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]

input("준비되셨으면 엔터를 입력해주세요.")

random.shuffle(animal_names)   # 순서를 랜덤으로 섞어줌.

begin_time = time.time()

ok_counter = 0


# 횟수 5회로 제한
# for count in range(5):
#     random_name = random.choice(animal_names)

for random_name in animal_names[0:5]:    # 리스트를 슬라이싱해서 
    print(random_name)
    line = input(">>> ")
    if random_name == line:
        ok_counter += 1
        print("정확합니다.")
    else:
        print("오타가 있어요.")

end_time = time.time()

print(f"{ok_counter}번 성공하셨습니다.")
print(f"총{end_time - begin_time}초가 걸리셨어요.")
