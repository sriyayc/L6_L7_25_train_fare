import pytest
from train_fare import base_fare, concession, tatkal_charge

# Test cases written to execute every line of train_fare.py (line coverage).


# ---------- base_fare ----------
def test_sleeper_fare():
    assert base_fare("SL", 500) == 500

def test_ac_class_fare():
    assert base_fare("2A", 100) == 300

def test_unknown_class_raises():
    with pytest.raises(ValueError, match="unknown class"):
        base_fare("GN", 100)

def test_invalid_distance_raises():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", 0)

def test_minimum_fare_applied():
    assert base_fare("SL", 10) == 50


# ---------- concession ----------
def test_adult_no_concession():
    assert concession(30, "M", False) == 0

def test_tatkal_no_concession():
    assert concession(3, "F", True) == 0

def test_infant_concession():
    assert concession(3, "M", False) == 100

def test_child_concession():
    assert concession(10, "F", False) == 50

def test_senior_female_concession():
    assert concession(65, "F", False) == 50

def test_senior_male_concession():
    assert concession(65, "M", False) == 40


# ---------- tatkal_charge ----------
def test_tatkal_sleeper_capped_at_max():
    assert tatkal_charge("SL", 5000) == 400

def test_tatkal_ac_raised_to_min():
    assert tatkal_charge("3A", 100) == 100
