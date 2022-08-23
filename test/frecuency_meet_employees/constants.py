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

# Permutation Expects

PERMUTATION_EXPECT1 = 'RENE-ASTRID: None\nRENE-ANDRES: None\nASTRID-ANDRES: None'
PERMUTATION_EXPECT2 = 'RENE-ASTRID: None'
PERMUTATION_EXPECT3 = 'ANDERSON-DARWIN: None\nANDERSON-FELIX: None\nANDERSON-ANTHONY: None\nDARWIN-FELIX: None\nDARWIN-ANTHONY: None\nFELIX-ANTHONY: None'
PERMUTATION_EXPECT4 = 'ASTRID-RENE: None'
PERMUTATION_EXPECT5 = 'MARCO-PEPE: None\nMARCO-FRANCISCO: None\nMARCO-MAURICIO: None\nPEPE-FRANCISCO: None\nPEPE-MAURICIO: None\nFRANCISCO-MAURICIO: None'
