# Smart Expense Tracker

## Overview
Smart Expense Tracker is a menu-driven Python application for recording and analyzing personal expenses without requiring a database or external libraries.

## Features
1. Add an expense with date, description, category and amount.
2. View all recorded expenses.
3. Calculate total expenditure.
4. Group expenditure by category.
5. Search by description or category.
6. Find the highest expense.
7. Generate a monthly summary with count, total and average.
8. Delete an expense.
9. Exit safely.

## Technologies
- Python 3
- Lists
- Dictionaries
- Functions
- Loops and conditional statements
- Exception handling
- String processing

No external packages or database are required.

## How to Run
1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:
   `python main.py`

## Testing
The project should be tested for:
- Valid expense entry
- Empty date/description
- Invalid category
- Zero/negative amount
- Non-numeric amount
- Search with matching and non-matching text
- Monthly summary with and without results
- Valid and invalid deletion numbers
- Invalid menu choices

## Storage Note
Expenses are stored in memory using a Python list. Data is therefore cleared when the program terminates. This is intentional for the current database-free scope.

## Project Structure
- `main.py` - complete application
- `statement.md` - problem statement, scope and users
- `requirements.txt` - environment requirements
- `docs/project_report.pdf` - submission-ready report
- `docs/workflow.png` - workflow diagram
- `docs/use_case.png` - use-case diagram
- `docs/component.png` - component/module diagram
- `tests/test_plan.md` - testing plan

## Future Enhancements
Persistent file/JSON storage, stronger date validation, CSV export, charts, budgets and a graphical interface can be added later.

## Modular Version
For the VITyarthi technical expectation regarding meaningful modules/files, a modular implementation is included in `modular_version/`:
- `main.py` - application controller/menu
- `data.py` - expense data and categories
- `input_helpers.py` - input/category/amount handling
- `expense_operations.py` - add/view/delete operations
- `reports.py` - total/category/highest/monthly reports
- `search.py` - search functionality

Run the modular version with:
`python modular_version/main.py`

The original `main.py` at the project root is retained exactly as the final code supplied for the project.
