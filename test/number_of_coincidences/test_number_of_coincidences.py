from solution.functions import number_of_coincidences
from test.number_of_coincidences import constants as const
from pytest import mark


@mark.parametrize(
    "input_a, input_b, expected",
    [
        (const.COINCIDENCES_INPUT1, const.COINCIDENCES_INPUT2,
         const.COINCIDENCES_EXPECT1),
        (const.COINCIDENCES_INPUT2, const.COINCIDENCES_INPUT1,
         const.COINCIDENCES_EXPECT1),
        (const.COINCIDENCES_INPUT2, const.COINCIDENCES_INPUT3,
         const.COINCIDENCES_EXPECT2),
        (const.COINCIDENCES_INPUT3, const.COINCIDENCES_INPUT2,
         const.COINCIDENCES_EXPECT2),
        (const.COINCIDENCES_INPUT1, const.COINCIDENCES_INPUT3,
         const.COINCIDENCES_EXPECT3),
        (const.COINCIDENCES_INPUT3, const.COINCIDENCES_INPUT1,
         const.COINCIDENCES_EXPECT3),
    ]
)
def test_frecuency_meet_employees(input_a, input_b, expected):
    assert number_of_coincidences(input_a, input_b) == expected
