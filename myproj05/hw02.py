# max / min
# "좋아요" 수가 가장 많은 곡은? 가장 작은 곡은?
# "곡명" 단어수가 가장 많은 곡은? 가장 작은 곡은?
# "곡명" 글자수가 가장 많은 곡은? 가장 작은 곡은?

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def song_like(song_dict):
    return song_dict["like"]


#sorted_song_list = sorted(song_list, reverse=1, key=song_like)

print('"좋아요" 수가 가장 많은 곡은? \n')
for song_dict in song_list:  # sorted_song_list:
    like_max = [{like}].format(**song_dict)
    print(max(like_max))
    #print("[{title}], {artist}, {like}".format(**song_dict))


# sorted_song_list = sorted(song_list, key=song_like)

# for song_dict in sorted_song_list[]:
#     print(max(song_dict))
