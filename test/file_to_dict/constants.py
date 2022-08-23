import os


# File path

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
FILE_PATH = os.path.join(BASE_PATH, 'files')
TEST_FILE1 = os.path.join(FILE_PATH, 'example1.txt')
TEST_FILE2 = os.path.join(FILE_PATH, 'example2.txt')
TEST_FILE3 = os.path.join(FILE_PATH, 'example3.txt')
TEST_FILE4 = os.path.join(FILE_PATH, 'example4.txt')
TEST_FILE5 = os.path.join(FILE_PATH, 'example5.txt')


# Dictionary Expects

DICT_EXPECT1 = {
    "RENE": {
        "MO": ["1000", "1200"],
        "TU": ["1000", "1200"],
        "TH": ["0100", "0300"],
        "SA": ["1400", "1800"],
        "SU": ["2000", "2100"]
    },
    "ASTRID": {
        "MO": ["1000", "1200"],
        "TH": ["1200", "1400"],
        "SU": ["2000", "2100"]
    },
    "ANDRES": {
        "MO": ["1000", "1200"],
        "TH": ["1200", "1400"],
        "SU": ["2000", "2100"]
    }
}

DICT_EXPECT2 = {
    "RENE": {
        "MO": ["1015", "1200"],
        "TU": ["1000", "1200"],
        "TH": ["1300", "1315"],
        "SA": ["1400", "1800"],
        "SU": ["2000", "2100"]
    },
    "ASTRID": {
        "MO": ["1000", "1200"],
        "TH": ["1200", "1400"],
        "SU": ["2000", "2100"]
    },
}


DICT_EXPECT3 = {
    "ANDERSON": {
        "MO": ["1000", "1300"],
        "TH": ["1200", "1300"],
        "SU": ["2000", "2100"]
    },
    "DARWIN": {
        "MO": ["1100", "1200"],
        "TU": ["1000", "1400"],
        "TH": ["0100", "0300"],
        "SA": ["1400", "1800"],
        "SU": ["2000", "2100"]
    },
    "FELIX": {
        "MO": ["1000", "1200"],
        "TH": ["1200", "1400"],
        "SU": ["2000", "2100"]
    },
    "ANTHONY": {
        "MO": ["1200", "1400"],
        "TH": ["1000", "1200"],
        "SA": ["2000", "2100"]
    }
}


DICT_EXPECT4 = {
    "ASTRID": {
        "MO": ["1000", "1200"],
        "TH": ["1200", "1400"],
        "SU": ["2000", "2100"]
    },
    "RENE": {
        "MO": ["1015", "1200"],
        "TU": ["1000", "1200"],
        "TH": ["1300", "1315"],
        "SA": ["1400", "1800"],
        "SU": ["2000", "2100"]
    },
}

DICT_EXPECT5 = {
    "MARCO": {
        "MO": ["1000", "1300"],
        "TH": ["1200", "1300"],
        "SU": ["2000", "2100"]
    },
    "PEPE": {
        "MO": ["1100", "1200"],
        "TU": ["1000", "1400"],
        "TH": ["0100", "0300"],
        "SA": ["1400", "1800"],
        "SU": ["2000", "2100"]
    },
    "FRANCISCO": {
        "MO": ["1000", "1200"],
        "TH": ["1200", "1400"],
        "SU": ["2000", "2100"]
    },
    "MAURICIO": {
        "MO": ["1200", "1400"],
        "TH": ["1000", "1200"],
        "SA": ["2000", "2100"]
    }
}
