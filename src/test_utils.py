import pytest
import utils


def test_existing_outdoor_table_lookups():
    assert utils.temp_to_kilo_ohm(-35, "outdoor") == 64.2
    assert utils.temp_to_kilo_ohm(-30, "outdoor") == 47.0
    assert utils.temp_to_kilo_ohm(-25, "outdoor") == 34.7
    assert utils.temp_to_kilo_ohm(-20, "outdoor") == 25.9
    assert utils.temp_to_kilo_ohm(-15, "outdoor") == 19.5
    assert utils.temp_to_kilo_ohm(-10, "outdoor") == 14.8
    assert utils.temp_to_kilo_ohm(-5, "outdoor") == 11.4
    assert utils.temp_to_kilo_ohm(0, "outdoor") == 8.8
    assert utils.temp_to_kilo_ohm(5, "outdoor") == 6.8
    assert utils.temp_to_kilo_ohm(10, "outdoor") == 5.3
    assert utils.temp_to_kilo_ohm(15, "outdoor") == 4.2
    assert utils.temp_to_kilo_ohm(20, "outdoor") == 3.4
    assert utils.temp_to_kilo_ohm(25, "outdoor") == 2.7
    assert utils.temp_to_kilo_ohm(30, "outdoor") == 2.2


def test_calculated_positive_outdoor_table_lookups():
    assert utils.temp_to_kilo_ohm(2, "outdoor") == 8.0
    assert utils.temp_to_kilo_ohm(7, "outdoor") == 6.2
    assert utils.temp_to_kilo_ohm(14, "outdoor") == 4.42
    assert utils.temp_to_kilo_ohm(23, "outdoor") == 2.98
    assert utils.temp_to_kilo_ohm(32, "outdoor") == 2.2


def test_calculated_negative_outdoor_table_lookups():
    assert utils.temp_to_kilo_ohm(-2, "outdoor") == 9.84
    assert utils.temp_to_kilo_ohm(-7, "outdoor") == 12.76
    assert utils.temp_to_kilo_ohm(-14, "outdoor") == 18.56
    assert utils.temp_to_kilo_ohm(-23, "outdoor") == 31.18
    assert utils.temp_to_kilo_ohm(-32, "outdoor") == 53.88
    assert utils.temp_to_kilo_ohm(-38, "outdoor") == 64.2
