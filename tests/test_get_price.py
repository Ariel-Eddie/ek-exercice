import pytest
from src.get_price import (
    is_back_to_the_future, 
    count_dvd_types, 
    get_final_price
)


@pytest.mark.parametrize("name, expected", [
    ("back to The FUture", True),
    ("BACK   to the FUTURE", True),
    ("back tt future", False),
    ("back other", False)
])
def test_is_back_to_the_future(name, expected):
    assert is_back_to_the_future(name) is expected
    

input_1 = """

Back to the future 1
Back to the future 1
Godzilla
"""

input_2 = """

Back to the future 1
Back to the future 2
Back to the future 2

Godzilla
"""

input_3 = """    
Godzilla
"""


def test_count_dvd_types():
    
    expected_1 = {
        "n_back_to_the_future": 2,
        "nunique_back_to_the_future": 1,
        "n_others": 1
    }
    expected_2 = {}
    assert count_dvd_types(input_1) == expected_1
    assert count_dvd_types("") == expected_2
    

def test_get_final_price():
    assert get_final_price(input_1) == 50
    assert get_final_price(input_2) == 60.5
    assert get_final_price(input_3) == 20
    assert get_final_price(input_2, price_only=False) == {"price": 60.5, "discount": 0.9}
