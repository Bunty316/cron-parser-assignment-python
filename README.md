# cron-parser-assignment-python

Introduction
This is a command-line application that parses a cron string and expands each field to show the times at which it will run. It only considers the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command. Special time strings such as "@yearly" are not handled.

Installation
This project requires Python to run. Ensure you have Python installed on your computer before proceeding. If not, you can download it from Python's official website.

Running The Application
To run the application, open your terminal and navigate to the project directory.

Then type:
python cron_parser_2.py "<Your Cron String>"

Replace <Your Cron String> with any valid cron string. For example:

python cron_parser_2.py "*/15 0 1,15 * 1-5 /usr/bin/find"
Running The Tests
To run the tests, you need to have pytest installed. You can install pytest via pip:
pip install pytest

Then, navigate to the project directory and type:
pytest test.py

Examples
Here are some sample cron strings and the expected application outputs:

Cron String: */15 0 1,15 * 1-5 /usr/bin/find

Output:

apache
Copy
minute         0 15 30 45
hour           0
day of month   1 15
month          1 2 3 4 5 6 7 8 9 10 11 12
day of week    1 2 3 4 5
command        /usr/bin/find
Limitations
This parser is designed to work with standard cron formats and does not support special time strings such as "@yearly" or "@monthly".

