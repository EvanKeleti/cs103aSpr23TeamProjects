'''This file contains code for the Transaction class
and a to_dict() function that is used in the class and in its testing'''
import sqlite3
import os

def to_dict(t):
    ''' t is a tuple (item #, amount. category, date, description)'''
    return {'item #':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}

class Transaction():
    '''Class that alters the database, this class has no direct contact with user input
    is interfaced by tracker.py'''
    def __init__(self, filename):
        self.database = filename
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                        ("item #" integer, amount real, category text,
                          date text, description text)''',())

    def run_query(self,query,tup):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute(query,tup)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        #return [to_dict(t) for t in tuples]
        return tuples

    def show_transactions(self):
        '''show the transactions in the database - Evan Keleti'''
        return self.run_query("SELECT * FROM transactions", ())

    def add_transaction(self, transaction):
        '''creates and adds a transaction to the database - Evan Keleti'''
        self.run_query("INSERT INTO transactions VALUES (?,?,?,?,?)",
                        (transaction['item #'], transaction['amount'],
                          transaction['category'], transaction['date'], transaction['description']))

    def delete_transaction(self, item_num):
        '''deletes the transaction with the specified item number - Evan Keleti'''
        return self.run_query('DELETE FROM transactions WHERE "item #"=(?)', (item_num,))

    def summarize_by_date(self):
        '''summarizes the transactions by date - Evan Keleti'''
        return self.run_query('''SELECT strftime('%Y-%m-%d', date) as day, COUNT(*) as count,
          TOTAL(amount) FROM transactions GROUP BY day ORDER BY day''', ())

    def summarize_by_month(self):
        '''summarize the transactions by month - Evan Keleti'''
        return self.run_query('''SELECT strftime('%Y-%m', date) as month, COUNT(*) as count,
          TOTAL(amount) FROM transactions GROUP BY month ORDER BY month''', ())

    def summarize_by_year(self):
        '''summarize the transactions by year - Evan Keleti'''
        return self.run_query('''SELECT strftime('%Y', date) as year, COUNT(*) as count,
          TOTAL(amount) FROM transactions GROUP BY year ORDER BY year''', ())

    def summarize_by_category(self):
        '''summarize the transactions by category - Evan Keleti'''
        return self.run_query('''SELECT category, COUNT(*) as count,
          TOTAL(amount) FROM transactions GROUP BY category''', ())

    def clear_transactions(self):
        '''clears all transactions from the database - Evan Keleti'''
        self.run_query("DELETE FROM transactions", ())
