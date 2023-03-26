
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

    def run_query(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con = sqlite3.connect(self.database)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        #return [to_dict(t) for t in tuples]
        return tuples

    def show_transactions(self):
        '''show the transactions in the database'''
        return self.run_query("SELECT * FROM transactions", ())

    def add_transaction(self, transaction):
        '''creates and adds a transaction to the database'''
        self.run_query("INSERT INTO transactions VALUES (?,?,?,?,?)", 
                        (transaction['item #'], transaction['amount'],
                          transaction['category'], transaction['date'], transaction['description']))

    def delete_transaction(self, itemNum):
        '''deletes the transaction with the specified item number'''
        return self.run_query('DELETE FROM transactions WHERE "item #"=(?)', (itemNum,))

    def summarize_by_date(self):
        '''summarizes the transactions by date'''
        return self.run_query('''SELECT strftime('%Y-%m-%d', date) as day, COUNT(*) as count,
          TOTAL(amount) FROM transactions GROUP BY day ORDER BY day''', ())

    def summarize_by_month(self):
        '''summarize the transactions by month'''
        return self.run_query('''SELECT strftime('%Y-%m', date) as month, COUNT(*) as count,
          TOTAL(amount) FROM transactions GROUP BY month ORDER BY month''', ())

    def summarize_by_year(self):
        '''summarize the transactions by year'''
        return self.run_query('''SELECT strftime('%Y', date) as year, COUNT(*) as count,
          TOTAL(amount) FROM transactions GROUP BY year ORDER BY year''', ())

    def summarize_by_category(self):
        '''summarize the transactions by category'''
        return self.run_query('''SELECT category, COUNT(*) as count,
          TOTAL(amount) FROM transactions GROUP BY category''', ())

    def clear_transactions(self):
        self.run_query("DELETE FROM transactions", ())
