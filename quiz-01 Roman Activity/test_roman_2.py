from roman_2 import roman_to_number, validate_roman_rules


def test_roman_to_number():
    assert roman_to_number("I") == 1
    assert roman_to_number("V") == 5
    assert roman_to_number("X") == 10
    assert roman_to_number("IV") == 4
    assert roman_to_number("IX") == 9
    assert roman_to_number("XIV") == 14
    assert roman_to_number("MCMXCIV") == 1994


def test_valid_roman_numerals():
    assert validate_roman_rules("I")[0] is True
    assert validate_roman_rules("IV")[0] is True
    assert validate_roman_rules("IX")[0] is True
    assert validate_roman_rules("XIV")[0] is True
    assert validate_roman_rules("XL")[0] is True
    assert validate_roman_rules("XC")[0] is True
    assert validate_roman_rules("CD")[0] is True
    assert validate_roman_rules("CM")[0] is True


def test_invalid_roman_numerals():
    assert validate_roman_rules("VV")[0] is False
    assert validate_roman_rules("LL")[0] is False
    assert validate_roman_rules("DD")[0] is False
    assert validate_roman_rules("IIII")[0] is False
    assert validate_roman_rules("XXXX")[0] is False
    assert validate_roman_rules("VX")[0] is False
    assert validate_roman_rules("IL")[0] is False
    assert validate_roman_rules("IC")[0] is False
    assert validate_roman_rules("XD")[0] is False