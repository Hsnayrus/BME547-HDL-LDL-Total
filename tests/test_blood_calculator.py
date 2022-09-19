import pytest
import sys

sys.path.insert(0, "/home/hsnayrus/bme547/BME547-HDL-LDL-Total")


@pytest.mark.parametrize(
    "HDL_input, expected",
    [
        (99999, "Normal"),
        (85, "Normal"),
        (60, "Normal"),
        (40, "Borderline Low"),
        (59, "Borderline Low"),
        (39, "Low"),
        (-99999, "Low"),
    ],
)
def test_check_HDL(HDL_input, expected):
    from blood_calculator import check_HDL

    answer = check_HDL(HDL_input)
    assert answer == expected


@pytest.mark.parametrize("LDL_input, expected", [
    (129, "Normal"),
    (80, "Normal"),
    (130, "Borderline High"),
    (159, "Borderline High"),
    (160, "High"),
    (189, "High"),
    (190, "Very High"),
    (220, "Very High")
])
def test_check_LDL(LDL_input, expected):
    from blood_calculator import check_LDL

    answer = check_LDL(LDL_input)
    assert answer == expected


@pytest.mark.parametrize("Total_Cholestrol_input, expected", [
    (0, "Normal"),
    (199, "Normal"),
    (200, "Borderline High"),
    (239, "Borderline High"),
    (240, "High"),
    (3000, "High")
])
def test_check_Total_Cholestrol(Total_Cholestrol_input, expected):
    from blood_calculator import check_Total_Cholestrol

    answer = check_Total_Cholestrol(Total_Cholestrol_input)
    assert answer == expected
