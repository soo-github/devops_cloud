import pytest
from main01 import get_word_count, get_ch_count_except_space, get_rounded_number

@pytest.mark.parametrize("sentence, expected", [
    ("우리는 파이썬을 즐겨요",3),
    ("Python Family", 2)
    ]
    )
def test_get_word_count(sentence, expected):
    assert get_word_count("우리는 파이썬을 즐겨요") == 3
    assert get_word_count("Python Family") == 2

@pytest.mark.parametrize("sentence, expected", [
    ("우리는 파이썬을 즐겨요" , 10),
    ("Python Family", 12),
    ("Hello World", 10)
])

def get_ch_count_except_space(sentence, expected):
    assert get_ch_count_except_space(sentence) == expected
    # assert get_ch_count_except_space("우리는 파이썬을 즐겨요") == 10
    # assert get_ch_count_except_space("Python Family") == 12


@pytest.mark.parametrize(
    "number, expected",
    [
        (123456, 1234000),
        (1234, 1000)
    ]
)

def get_rounded_number(number, expected):
    assert get_rounded_number(number) == expected




