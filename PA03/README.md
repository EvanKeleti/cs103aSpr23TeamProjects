# Transaction Tracker in Python using SQL
### about

This program implements persistent memory of Transaction objects (tuples holding an item#, an amount, a category, a date, and a
description) using SQL. Features capability to add and delete transactions, as well as display all transactions summarized by year,
month, date, or category.

### transcript of pylint and pytest
```
C:\Users\Simon\Documents\GitHub\cs103aSpr23TeamProjects\PA03>pylint tracker.py
************* Module tracker
tracker.py:54:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:25:37: C0103: Argument name "x" doesn't conform to snake_case naming style (invalid-name)
tracker.py:66:8: R1722: Consider using 'sys.exit' instead (consider-using-sys-exit)
tracker.py:59:0: R0912: Too many branches (15/12) (too-many-branches)

-----------------------------------
Your code has been rated at 9.46/10
C:\Users\Simon\Documents\GitHub\cs103aSpr23TeamProjects\PA03>pylint transaction.py
************* Module transaction
transaction.py:6:12: C0103: Argument name "t" doesn't conform to snake_case naming style (invalid-name)
transaction.py:4:0: W0611: Unused import os (unused-import)

-----------------------------------
Your code has been rated at 9.38/10
C:\Users\Simon\Documents\GitHub\cs103aSpr23TeamProjects\PA03>pylint test_transaction.py
************* Module test_transaction
test_transaction.py:19:4: C0103: Variable name "l" doesn't conform to snake_case naming style (invalid-name)
test_transaction.py:34:4: C0103: Variable name "x" doesn't conform to snake_case naming style (invalid-name)
test_transaction.py:35:4: C0103: Variable name "y" doesn't conform to snake_case naming style (invalid-name)

-----------------------------------
Your code has been rated at 9.32/10
C:\Users\Simon\Documents\GitHub\cs103aSpr23TeamProjects\PA03>pytest test_transaction.py
================================================= test session starts =================================================
platform win32 -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\Simon\Documents\GitHub\cs103aSpr23TeamProjects\PA03
plugins: anyio-3.6.2
collected 6 items

test_transaction.py ......                                                                                       [100%]

================================================== 6 passed in 0.22s ==================================================
```

### transcript of tracker.py features
```
C:\Users\Simon\Documents\GitHub\cs103aSpr23TeamProjects\PA03>python tracker.py
usage:
            quit
            show
            add item# amount category date(YYYY-MM-DD) description
            delete item#
            summarize_by_date
            summarize_by_month
            summarize_by_year
            summarize_by_category
            clear_transactions

command> add 1 300 apples 2020-07-18 crispy
----------------------------------------



command> add 2 450 mangos 2021-01-01 scrumptious
----------------------------------------



command> add 3 50 pies 2022-04-20 savory
----------------------------------------



command> show


('item #', 'amount', 'category', 'date', 'description')
----------------------------------------
(1, 300.0, 'apples', '2020-07-18', 'crispy')
(2, 450.0, 'mangos', '2021-01-01', 'scrumptious')
(3, 50.0, 'pies', '2022-04-20', 'savory')
----------------------------------------



command> summarize_by_date


('date', 'item #', 'amount')
----------------------------------------
('2020-07-18', 1, 300.0)
('2021-01-01', 1, 450.0)
('2022-04-20', 1, 50.0)
----------------------------------------



command> summarize_by_category


('category', 'item #', 'amount')
----------------------------------------
('apples', 1, 300.0)
('mangos', 1, 450.0)
('pies', 1, 50.0)
----------------------------------------



command> summarize_by_year


('year', 'item #', 'amount')
----------------------------------------
('2020', 1, 300.0)
('2021', 1, 450.0)
('2022', 1, 50.0)
----------------------------------------



command> summarize_by_month


('month', 'item #', 'amount')
----------------------------------------
('2020-07', 1, 300.0)
('2021-01', 1, 450.0)
('2022-04', 1, 50.0)
----------------------------------------



command> clear_transactions
no transactions to print
----------------------------------------



command> show
no transactions to print
----------------------------------------



command> add 1 300 apples 2020-07-18 oops
----------------------------------------



command> show


('item #', 'amount', 'category', 'date', 'description')
----------------------------------------
(1, 300.0, 'apples', '2020-07-18', 'oops')
----------------------------------------



command> delete 1
----------------------------------------



command> show
no transactions to print
----------------------------------------



command>quit

C:\Users\Simon\Documents\GitHub\cs103aSpr23TeamProjects\PA03>
```