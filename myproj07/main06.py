"""
방탄소년단의 좋아요 총 합은?
"""

from collections import defaultdict, Counter
from pprint import pprint
import pandas as pd

# List Comprehension whit if statement
like_sum_for_bts = sum([song_dict["like"]
                        for song_dict in song_list
                        if song_dict["artist"] == "방탄소년단"])
print(like_sum_for_bts)
