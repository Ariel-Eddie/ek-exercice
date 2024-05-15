import pytest
from src.get_price import is_back_to_the_future, count_dvd_types, get_final_price


@pytest.mark.parametrize(
    "name, expected",
    [
        ("back to The FUture", True),
        ("BACK   to the FUTURE", True),
        ("back tt future", False),
        ("back other", False),
    ],
)
def test_is_back_to_the_future(name, expected):
    assert is_back_to_the_future(name) is expected


input_1 = """

Back to the Future 1
Back to the Future 2
Back to the Future 3
"""

input_2 = """
Back to the Future 1
Back to the Future 3
"""

input_3 = """
Back to the Future 1
"""

input_4 = """
Back to the Future 1
Back to the Future 2
Back to the Future 3
Back to the Future 2
"""

input_5 = """
Back to the Future 1
Back to the Future 2
Back to the Future 3
La chèvre
"""


def test_count_dvd_types():

    expected_1 = {
        "n_back_to_the_future": 3,
        "nunique_back_to_the_future": 3,
        "n_others": 0,
    }
    expected_5 = {
        "n_back_to_the_future": 3,
        "nunique_back_to_the_future": 3,
        "n_others": 1,
    }
    assert count_dvd_types(input_1) == expected_1
    assert count_dvd_types(input_5) == expected_5


def test_get_final_price():
    assert get_final_price(input_1) == 36
    assert get_final_price(input_2) == 27
    assert get_final_price(input_3) == 15
    assert get_final_price(input_4) == 48
    assert get_final_price(input_5) == 56
