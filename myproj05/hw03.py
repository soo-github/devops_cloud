# 리스트에 랭크된 가수는 총 몇 팀인가요?(중복 제거한 가수명 리스트의 크기)
# 2곡 이상 랭크된 가수는 몇 팀인가요?
# "방탄소년단"의 좋아요 총 합은?

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 방탄소년단 좋아요 총 합 구하는 방법 1.
# def filter_fn3(song_dict):
#     return song_dict["artist"] == "방탄소년단"

# for song_dict in filter(filter_fn3, song_list):
#     bts_like = song_dict["like"]
#     print(bts_like)


# 방탄소년단 좋아요 총 합 구하는 방법 2.
total = 0

for song in song_list:
    if song["artist"] == "방탄소년단":
        total += song["like"]
print('방탄소년단 "좋아요" 총 합계는?')
print(total)
