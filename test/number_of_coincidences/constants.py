# Number of Coincidences
# Inputs

COINCIDENCES_INPUT1 = {
    "MO": ["1000", "1400"],
    "TU": ["1100", "1400"],
    "TH": ["0100", "0300"],
    "SA": ["1400", "1800"],
    "SU": ["2000", "2100"]
}
COINCIDENCES_INPUT2 = {
    "MO": ["1100", "1200"],
    "TH": ["0200", "0500"],
    "WE": ["1200", "1400"],
    "SU": ["1900", "2200"]
}
COINCIDENCES_INPUT3 = {
    "MO": ["1400", "1500"],
    "TU": ["1015", "1200"],
    "WE": ["1100", "1500"],
    "TH": ["1300", "1600"],
    "FR": ["1520", "1745"],
    "SA": ["1400", "1800"],
    "SU": ["2000", "2100"]
}

# Expects

# INPUT1-INPUT2
COINCIDENCES_EXPECT1 = 3

# INPUT2-INPUT3
COINCIDENCES_EXPECT2 = 2

# INPUT1-INPUT3
COINCIDENCES_EXPECT3 = 4
