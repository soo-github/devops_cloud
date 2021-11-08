
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

"""
멜론TOP100 리스트에서 "곡명 / 단어수" 리스트 만들기
총 100줄 중에 한 줄 출력 의 예 : Dynamite ➡ 1
"""
# for song_dict in song_list:
#     title: str = song_dict["title"]
#     title_length = len(title)
#     print(title, title_length)

# map 어떤 값을 변환하는 것
# 함수 사용해서 출력


def get_title_for_song(song_dict):
    return song_dict["title"]

# for song_dict in song_list:
#     # 변환을 담당하는 함수
#     print(get_title_for_song(song_dict))


# title_list = list(map(get_title_for_song, song_list))
# print(title_list)

# for title in map(get_title_for_song, song_list):
#     print(f"{title}) - {len(title)}")


def get_title_and_length_for_song(song_dict):
    title: str = song_dict["title"]
    return [title, len(title)]


for title, length in map(get_title_and_length_for_song, song_list):
    print(title, length)


# 방탄소년단의 노래에 대해서만, 곡명과 곡명의 글자수를 출력
# if와 for문으로
# bts_list = []
# for song_dict in song_list:
#     if song_dict["artist"] == "방탄소년단":
#         title: str = song_dict["title"]
#         bts_list.append([title, len(title)])

# for title, length in bts_list:
#     print(title, length)

# filter, map 버전
def check_bts_song(song_dict):
    return song_dict["artist"] == "방탄소년단"


for title, length in map(
    get_title_and_length_for_song,
    filter(check_bts_song, song_list)
):
    print(title, length)

# 문제
# artist 글자수가 3글자 이상인 곡에 대해서 filter를 걸고
# 각 곡의 좋아요 수와 제목 글자수의 곱을 출력

# 1) for/if로 구현
# new_list = []
# for song_dict in song_list:
#     if int(song_dict["artist"]) >= 3:
#         new_list.append([title])
#         print(new_list)

new_song_list: List[dict] = []
for song_dict in song_list:
    artist: str = song_dict["artist"]
    if len(artist) >= 3:
        value: int = song_dict["like"] * len(song_dict["title"])
        new_song_list.append(dict(song_dict, value=value))
        # new_song_list.append(
        #     {
        #         "title": song_dict["title"],
        #         "artist": song_dict["artist"],
        #         "like": song_dict["like"],
        #         "album": song_dict["album"],
        #         "rank": song_dict["rank"],
        #         "value": value,
        #     }
        # )

for song_dict in new_song_list:
    print("{title} / {value}".format(**song_dict))


# 2) filter/map으로 구현
def

"""
멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 출력
단어수가 제일 큰 노래가 우선순위가 가장 높겠죠.
"""
