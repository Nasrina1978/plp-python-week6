# plp-python-week6

- safe_tools.py - Three safe functions using try/except to handle ZeroDivisionError, ValueError, and KeyError without crashing.
- unbreakable.py - A loop that keeps asking for a number until valid input is entered.

Why can the if check not catch abc on its own? Because if checks a condition before, but int("abc") raises ValueError during conversion. We need try/except to catch the exception.