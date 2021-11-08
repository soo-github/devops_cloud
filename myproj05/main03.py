# def check_even_number(number):
#     return number % 2 == 0


# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in filter(check_even_number, numbers):
#     print(number)


# melon top100 곡 리스트로 3가지 조건의 필터링을 해봅시다.

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


print('"방탄소년단" 곡명만 출력하기')

# TODO


def filter_fn1(song_dict):
    return song_dict["artist"] == "방탄소년단"


for song_dict in filter(filter_fn1, song_list):
    print(song_dict["title"])


print('곡명에 "사랑"이 포함된 곡명만 출력하기')

# TODO


def filter_fn2(song_dict):
    return "사랑" in song_dict["title"]


for song_dict in filter(filter_fn2, song_list):
    print(song_dict["title"])


print('"좋아요" 수가 200,000 이상인 곡명만 출력하기')

# TODO


def filter_fn3(song_dict):
    return song_dict["like"] > 200_000


for song_dict in filter(filter_fn3, song_list):
    print(song_dict["like"], song_dict["title"])
