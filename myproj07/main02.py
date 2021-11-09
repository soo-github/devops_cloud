
df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def pic_word_count_for_title(song_dict):
    title: str = song_dict["like"]
    word_list = title.split()
    return len(word_list)


sorted_song_list = sorted(
    song_list, key=pic_word_count_for_title, reverse=True)
top10_song_list = sorted_song_list[:10]

for song_dict in top10_song_list:  # sorted의 결과는 항상 리스트
    print("{like} {title}".format(**song_dict))
