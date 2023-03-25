'''test_transaction.py tests the methods of the transactions.py file'''
import pytest
from transaction import Transaction

A = Transaction('transaction.db')

def test_init():
    '''tests the initialization of the db
    Nathan Weiss'''
    assert A.showTransactions() == []

def test_add():
    '''tests the add function
    checks that items are added properly
    Nathan Weiss'''
    tr1 = {'item #':1, 'amount':56.30,'category':"test", 'date':"2023-01-01", 'description':'testing'}
    A.addTransaction(tr1)
    l = A.showTransactions()
    assert l[len(l)-1]['item #'] == 1
    assert l[len(l)-1]['amount'] == 56.30
    assert l[len(l)-1]['category'] == 'test'
    assert l[len(l)-1]['date'] == '2023-01-01'
    assert l[len(l)-1]['description'] == 'testing'

    tr2 = {'item #':4, 'amount':60.75,'category':"textbook", 'date':"2023-03-25", 'description':'purchased textbook'}
    A.addTransaction(tr2)
    l = A.showTransactions()
    assert l[len(l)-1]['item #'] == 4
    assert l[len(l)-1]['amount'] == 60.75
    assert l[len(l)-1]['category'] == 'textbook'
    assert l[len(l)-1]['date'] == '2023-03-25'
    assert l[len(l)-1]['description'] == 'purchased textbook'
def test_show():
    '''tests that showTransactions shows all transactions'''
    assert A.showTransactions() == [{'item #': 1, 'amount': 56.3, 'category': 'grocery', 'date': '2023-01-01', 'description': 'grocery shop'}, {'item #': 4, 'amount': 60.75, 'category': 'textbook', 'date': '2023-03-25', 'description': 'purchased textbook'}]
