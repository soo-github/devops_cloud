# map
# 멜론 Top100 리스트에서 "곡명" 단어수 출력
# 멜론 Top100 리스트에서 "곡명" 단어수로 TOP10 곡명 출력

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# new_list = []
# for song_dict in song_list:
#     new_list.append(song_dict["title"])
#     result = len(new_list.split())
#     print(new_list + "->" + result)


# new_list = []
# def songTitle_fn():
#     for s in song_list:
#         new_list.append(s["title"])
#     return new_list


# song_count = input(songTitle_fn()).split()
# print(len(song_count))


# title_list = []
# title_list = df.title.tolist()

# result = title_list[37].split()   # 리스트를 인덱스로 가져와야해서 포기.

# print(result)


# 곡명 단어수
def songTitle_fn(s):
    return s["title"]


print("=== 멜론 Top100 리스트에서 '곡명' 단어수 출력 ===\n")
for s in map(songTitle_fn, song_list):
    print(s, "=>", len(s.split()))


# 곡명 단어수 top10
print("=== 멜론 Top100 리스트에서 '곡명' 단어수 TOP10 출력 ===\n")
# sorted_song_list = sorted(song_list, reverse=1, key=songTitle_fn)
# for s in map(songTitle_fn, song_list):
# for s in sorted_song_list:
# print("{title}".format(**s))

sorted_song_list = sorted(song_list, key=songTitle_fn)
for s in map(songTitle_fn, song_list):
    s, "=>", len(s.split())
