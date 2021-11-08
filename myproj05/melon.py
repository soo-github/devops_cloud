import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
# print(song_list)


for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        print(song_dict["title"])


for song_dict in song_list:
    if "가을" in song_dict["title"]:
        print(song_dict["title"])


song_count = 0
for song_dict in song_list:
    if song_dict["like"] > 200000:
        song_count += 1
print(f"좋아요가 200,000이 넘는 곡은 {song_count}곡 입니다.")


artist_dict = {}
for song_dict in song_list:
    artist: str = song_dict["artist"]     # 타입 힌트 : str 문자열이라는 뜻
    if artist not in artist_dict:
        artist_dict[artist] = 0
    artist_dict[artist] += 1

print(artist_dict)
#     artist_list.append(artist)

# print(artist_list)

# {
#     "방탄소년단": "값",
#     "소미": 3,
# }
