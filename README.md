# Expense Tracker

A simple command-line expense tracker. A [project](https://roadmap.sh/projects/expense-tracker) from Roadmap.sh

## Prerequisites

- Python 3.10+
- pipx

## Installation

To install the Expense Tracker, you can use `pipx` to isolate the environment:

```sh
pipx install git+https://github.com/itsukuna/expense_tracker.git
```

If you don't have pipx installed, you can install it first:

```sh
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

## Usage

```sh
expense_tracker add --description "Lunch" --amount 12.50
expense_tracker update --id 1 --description "Dinner" --amount 15.00
expense_tracker delete --id 1
expense_tracker list
expense_tracker summary --month 9
```

## Running Tests

To run the tests, use the following command:

```sh
python -m unittest /home/ryo/expense_tracker/test_expense_tracker.py
```
