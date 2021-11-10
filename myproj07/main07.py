import time

# 인자에 대한 리턴값을 저장
# - Key: 인자 값에 대한 튜플
# - value: 그 인자로 함수를 수행했을 때의 리턴값

cached = {}   # 전역변수(코드 관리성이 좋지않아서 가급적 지양해야 합니다.)


def mysum2(x, y):
    key = (x, y)
    if key not in cached:
        time.sleep(1)  # 1초간 대기
        cached[key] = x + y + 10
    return cached[key]


cached2 = {}


def mymultiply2(x, y):
    key = (x, y)
    if key not in cached2:
        time.sleep(1)
        cached2[key] = x * y + 10
    return cached2[key]


print(mysum2(1, 2))
print(mysum2(1, 3))
print(mysum2(1, 3))
print(mysum2(1, 2))
print(mysum2(1, 2))

print(mymultiply2(1, 2))
print(mymultiply2(1, 2))
print(mymultiply2(1, 3))
print(mymultiply2(1, 3))

# def base(base_number):
#     # number = 10
#     def fn(x, y):
#         return x + y + base_number
#     return fn


# base_10 = base(10)
# base_20 = base(20)
# print(base_10(1, 2))
# print(base_20(1, 2))

#a = base_10

# name = 'Tom'
# other_name = name

# def fn(x):
#     pass

# fn(name)
