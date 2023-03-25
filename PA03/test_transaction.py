'''test_transaction.py tests the methods of the transactions.py file'''
import pytest
from transaction import Transaction

A = Transaction('transaction.db')

def test_init():
    '''tests the initialization of the db'''
    assert A.showTransactions() == []

def test_add():
    '''tests the add function
    checks that items are added properly'''
    list =A.addTransaction((1, 56.30, "grocery", "2023-01-01", "grocery shop"))
    assert list[1]['item #'] == 1
    assert list[1]['amount'] == 56.30
    assert list[1]['category'] == 'grocery'
    assert list[1]['date'] == '2023-01-01'
    assert list[1]['description'] == 'grocery shop'

    list = A.addTransaction((4, 60.75, "textbook", "2023-03-25", "purchased textbook"))
    assert list[2]['item #'] == 4
    assert list[2]['amount'] == 60.75
    assert list[2]['category'] == 'textbook'
    assert list[2]['date'] == '2023-03-25'
    assert list[2]['description'] == 'purchased textbook'

