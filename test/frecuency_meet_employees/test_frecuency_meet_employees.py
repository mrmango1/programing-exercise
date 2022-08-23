from solution.functions import frecuency_meet_employee
from test.frecuency_meet_employees import constants as const
from unittest.mock import Mock
from pytest import mark


@mark.parametrize(
    "input_a,expected",
    [
        (const.DICT_EXPECT1, const.PERMUTATION_EXPECT1),
        (const.DICT_EXPECT2, const.PERMUTATION_EXPECT2),
        (const.DICT_EXPECT3, const.PERMUTATION_EXPECT3),
        (const.DICT_EXPECT4, const.PERMUTATION_EXPECT4),
        (const.DICT_EXPECT5, const.PERMUTATION_EXPECT5),
    ]
)
def test_frecuency_meet_employees(monkeypatch, input_a, expected):
    monkeypatch.setattr(
        "solution.functions.number_of_coincidences", Mock(return_value=None))
    assert frecuency_meet_employee(input_a) == expected
