""" 멜론 Top100 데이터 리스트
1. 방탄소년단의 곡명만 출력
2. 곡명에 가을이 들어가는 곡명만 출력
3. 좋아요 수가 200000이 넘는 곡수 출력
4. 가수별 곡수를 출력"""


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list

# 1.방탄소년단의 곡명만 출력
for song in song_list:
    if song["artist"] == "방탄소년단":
        print(song["title"])


# 2.곡명에 가을이 들어가는 곡명만 출력
for song in song_list:
    if "가을" in song["title"]:
        print(song["title"])


# 3.좋아요 수가 200000이 넘는 곡수 출력
result = 0

for song in song_list:
    if song["like"] > 200000:
        result += 1
print(result)


# 4.가수별 곡수를 출력
artist_dict = {}

for song in song_list:
    if song["artist"] in artist_dict:
        artist_dict[song["artist"]] += 1
    else:
        artist_dict[song["artist"]] = 1
print(artist_dict)
