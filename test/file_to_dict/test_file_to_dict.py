import pytest
from solution.functions import file_to_dict
from test.file_to_dict import constants as const


@pytest.mark.parametrize(
    "input_a,expected",
    [
        (const.TEST_FILE1, const.DICT_EXPECT1),
        (const.TEST_FILE2, const.DICT_EXPECT2),
        (const.TEST_FILE3, const.DICT_EXPECT3),
        (const.TEST_FILE4, const.DICT_EXPECT4),
        (const.TEST_FILE5, const.DICT_EXPECT5),
    ]
)
def test_file_to_dict(input_a, expected):
    assert file_to_dict(input_a) == expected
