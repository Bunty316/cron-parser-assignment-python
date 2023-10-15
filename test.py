import pytest
from cron_parser_2 import parse_cron # Assuming your original script is named cron_parser.py

def test_parse_cron():
    # Test case: Each field is '*'
    assert parse_cron('* * * * * /usr/bin/find') == (
        "minute         0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59\n"
        "hour           0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23\n"
        "day of month   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31\n"
        "month          1 2 3 4 5 6 7 8 9 10 11 12\n"
        "day of week    0 1 2 3 4 5 6\n"
        "command        /usr/bin/find"
    )
    
    # Test case: Each field has a single value
    assert parse_cron('5 4 3 2 1 /usr/bin/find') == (
        "minute         5\n"
        "hour           4\n"
        "day of month   3\n"
        "month          2\n"
        "day of week    1\n"
        "command        /usr/bin/find"
    )
    
    # Test case: Field has multiple comma-separated values
    assert parse_cron('1,15 * * * * /usr/bin/find') == (
        "minute         1 15\n"
        "hour           0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23\n"
        "day of month   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31\n"
        "month          1 2 3 4 5 6 7 8 9 10 11 12\n"
        "day of week    0 1 2 3 4 5 6\n"
        "command        /usr/bin/find"
    )
    
    # Test case: Field has a range of values
    assert parse_cron('1-5 * * * * /usr/bin/find') == (
        "minute         1 2 3 4 5\n"
        "hour           0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23\n"
        "day of month   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31\n"
        "month          1 2 3 4 5 6 7 8 9 10 11 12\n"
        "day of week    0 1 2 3 4 5 6\n"
        "command        /usr/bin/find"
    )
    
    # Test case: Field has a step value
    assert parse_cron('*/15 * * * * /usr/bin/find') == (
        "minute         0 15 30 45\n"
        "hour           0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23\n"
        "day of month   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31\n"
        "month          1 2 3 4 5 6 7 8 9 10 11 12\n"
        "day of week    0 1 2 3 4 5 6\n"
        "command        /usr/bin/find"
    )