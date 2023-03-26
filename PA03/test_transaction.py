'''test_transaction.py tests the methods of the transactions.py file
These tests will all  pass when the database passed in is empty or does not exist'''

from transaction import to_dict, Transaction

A = Transaction('transaction.db')

def test_init():
    '''tests the initialization of the db
    Nathan Weiss'''
    assert A.show_transactions() == []

def test_add():
    '''tests the add function
    checks that items are added properly
    Nathan Weiss'''
    A.add_transaction(to_dict((1,56.30,"test", "2023-01-01","testing")))
    A.add_transaction(to_dict((4,60.75,"textbook", "2023-03-25","purchased textbook")))
    l = [to_dict(t) for t in A.show_transactions()]
    assert l[len(l)-2]['item #'] == 1
    assert l[len(l)-2]['amount'] == 56.30
    assert l[len(l)-2]['category'] == 'test'
    assert l[len(l)-2]['date'] == '2023-01-01'
    assert l[len(l)-2]['description'] == 'testing'
    assert l[len(l)-1]['item #'] == 4
    assert l[len(l)-1]['amount'] == 60.75
    assert l[len(l)-1]['category'] == 'textbook'
    assert l[len(l)-1]['date'] == '2023-03-25'
    assert l[len(l)-1]['description'] == 'purchased textbook'

def test_show():
    '''tests that showTransactions shows all transactions
    Nathan Weiss'''
    x = to_dict((1,56.30,"test", "2023-01-01","testing"))
    y = to_dict((4,60.75,"textbook", "2023-03-25","purchased textbook"))
    assert [to_dict(t) for t in A.show_transactions()] == [x, y]

def test_delete():
    '''deletes the added transactions and checks that the database is empty
    Nathan Weiss'''
    A.delete_transaction(1)
    A.delete_transaction(4)
    assert [to_dict(t) for t in A.show_transactions()] == []

def test_sum():
    '''tests each summary by date function, adds a few transactions
      to db then checks that summaries are accurate
      Nathan Weiss'''
    A.add_transaction(to_dict((1,13,'test1', '2023-02-12', 'testing')))
    A.add_transaction(to_dict((2,101,'test2', '2022-01-10', 'testing')))
    A.add_transaction(to_dict((3,45,'test3', '2022-01-01', 'testing')))
    A.add_transaction(to_dict((4,39,'test3', '2023-03-27', 'testing')))
    A.add_transaction(to_dict((19,23,'test3', '1989-01-27', 'testing')))
    A.add_transaction(to_dict((20,3,'test2', '2022-01-10', 'testing')))
    date = [('1989-01-27',1,23),('2022-01-01',1,45),
            ('2022-01-10',2,104),('2023-02-12',1,13),('2023-03-27',1,39)]
    assert date == A.summarize_by_date()
    month = [('1989-01',1,23),('2022-01',3,149),('2023-02',1,13),('2023-03',1,39)]
    assert month == A.summarize_by_month()
    year = [('1989',1,23),('2022',3,149),('2023',2,52)]
    assert year == A.summarize_by_year()
    cats = [('test1', 1, 13), ('test2', 2, 104), ('test3', 3, 107)]
    assert cats == A.summarize_by_category()

def test_clear():
    '''tests that the clear_transactions method
      removes all transactions from the db
      Nathan Weiss'''
    A.clear_transactions()
    assert A.show_transactions() == []
