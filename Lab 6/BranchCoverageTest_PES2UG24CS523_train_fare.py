import pytest
from train_fare import base_fare, concession, tatkal_charge

# Test cases written so every decision in train_fare.py evaluates to both
# True and False (branch coverage), including boundary values.


# ---------- base_fare ----------
def test_sleeper_fare():
    assert base_fare("SL", 500) == 500

@pytest.mark.parametrize("travel_class, expected", [
    ("SL", 100), ("3A", 200), ("2A", 300), ("1A", 500),
])
def test_fare_for_every_class(travel_class, expected):
    assert base_fare(travel_class, 100) == expected

def test_unknown_class_raises():
    with pytest.raises(ValueError, match="unknown class"):
        base_fare("GN", 100)

def test_zero_distance_raises():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", 0)

def test_negative_distance_raises():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("1A", -5)

def test_minimum_fare_applied():
    assert base_fare("SL", 10) == 50

def test_fare_exactly_at_minimum():
    # fare == 50 -> "fare < 50" is False, fare unchanged
    assert base_fare("SL", 50) == 50

def test_fare_just_below_minimum():
    assert base_fare("3A", 24) == 50


# ---------- concession ----------
def test_adult_no_concession():
    assert concession(30, "M", False) == 0

def test_tatkal_no_concession():
    assert concession(3, "F", True) == 0

def test_tatkal_senior_no_concession():
    assert concession(70, "F", True) == 0

def test_infant_concession():
    assert concession(3, "M", False) == 100

def test_age_boundary_5_is_child():
    assert concession(5, "M", False) == 50

def test_child_concession():
    assert concession(10, "F", False) == 50

def test_age_boundary_12_is_child():
    assert concession(12, "M", False) == 50

def test_age_boundary_13_is_adult():
    assert concession(13, "F", False) == 0

def test_age_59_is_adult():
    assert concession(59, "F", False) == 0

def test_age_boundary_60_senior_female():
    assert concession(60, "F", False) == 50

def test_senior_female_concession():
    assert concession(65, "F", False) == 50

def test_senior_male_concession():
    assert concession(65, "M", False) == 40


# ---------- tatkal_charge ----------
def test_tatkal_sleeper_capped_at_max():
    assert tatkal_charge("SL", 5000) == 400

def test_tatkal_ac_capped_at_max():
    assert tatkal_charge("1A", 2000) == 400

def test_tatkal_ac_raised_to_min():
    assert tatkal_charge("3A", 100) == 100

def test_tatkal_sleeper_raised_to_min():
    assert tatkal_charge("SL", 500) == 100

def test_tatkal_sleeper_within_limits():
    # charge between 100 and 400 -> neither cap nor minimum applied
    assert tatkal_charge("SL", 2500) == 250

def test_tatkal_ac_within_limits():
    assert tatkal_charge("2A", 1000) == 300

def test_tatkal_exactly_at_max():
    assert tatkal_charge("SL", 4000) == 400

def test_tatkal_exactly_at_min():
    assert tatkal_charge("SL", 1000) == 100
