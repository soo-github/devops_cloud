
# 과제 문제 풀이


def myfilter(filter_fn, alter_value):
    def wrap(fn):
        def inner(*args):
            # TODO : new_args를 적절히 구성해주세요.
            # new_args는 리스트 및 튜플 자료구조가 가능합니다.
            new_args = []
            # 1번째 방법
            # for arg in args:
            #     if filter_fn(arg):
            #         new_args.append(alter_value)
            #     else:
            #         new_args.append(arg)

            # 2번째 방법
            for arg in args:
                new_args.append(
                    alter_value if filter_fn(arg) else arg
                )

            return fn(*new_args)
        return inner
    return wrap


@myfilter(lambda i: i % 2 == 0, 0)
def mysum(a, b, c, d, e):
    return a + b + c + d + e


@myfilter(lambda i: i % 2 == 0, 1)
def mymultiply(a, b, c, d, e):
    return a * b * c * d * e


print(mysum(1, 2, 3, 4, 5))  # 9
print(mymultiply(1, 2, 3, 4, 5))  # 15
