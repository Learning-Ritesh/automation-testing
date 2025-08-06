# MedTransGo UI Automation

This project automates login functionality for the MedTransGo Admin Portal using Selenium.

It tests redirection, email/password input, and successful login.

## Setup

1. Create virtual environment: `python3 -m venv selenium_env`
2. Activate it: `source selenium_env/bin/activate` (or `.\selenium_env\Scripts\activate` on Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run test: `python login.py`

Test completes when browser closes and "Logged in successfully." is printed.
