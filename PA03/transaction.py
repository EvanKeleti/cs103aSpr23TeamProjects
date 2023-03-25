
import sqlite3
import os

<<<<<<< HEAD
def to_dict(t):
    ''' t is a tuple (item #, amount. category, date, description)'''
    return {'item #':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
=======
def toDict(t):
    ''' t is a tuple (item #, amount, category, date, description)'''
    print('t='+str(t))
    transactions = {'item #':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transactions
>>>>>>> refs/remotes/origin/main

class Transaction():

    def __init__(self, filename):
        self.database = filename
        self.run_query(f'''CREATE TABLE IF NOT EXISTS transactions
                        ("item #" integer, amount real, category text, date text, description text)''',())

    def run_query(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
<<<<<<< HEAD
        con = sqlite3.connect(self.database)
=======
        con= sqlite3.connect(os.getenv('HOME', default='~')+f'/{self.database}')
>>>>>>> refs/remotes/origin/main
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
                        (transaction['item #'], transaction['amount'], transaction['category'], transaction['date'], transaction['description']))

    def delete_transation(self, itemNum):
        '''deletes the transaction with the specified item number'''
        return self.run_query("DELETE FROM transactions WHERE item #=(?)", (itemNum))
    
    def summarize_by_date(self):
        '''summarizes the transactions by date'''
        return self.run_query("SELECT * FROM transactions WHERE date = ")

    def summarize_by_month(self):
        '''summarize the transactions by month'''
        return self.run_query('''SELECT strftime('%Y-%m', date) as month, COUNT(*) as count, TOTAL(amount) FROM transactions
                                 GROUP BY month ORDER BY month''', ())

    def summarize_by_year(self):
        '''summarize the transactions by year'''
        return self.run_query('''SELECT strftime('%Y', date) as year, COUNT(*) as count, TOTAL(amount) FROM transactions
                                 GROUP BY year ORDER BY year''', ())
    
    def summarize_by_category(self):
        '''summarize the transactions by category'''
        return self.run_query("SELECT * FROM transactions WHERE category=(?)", ())
    
    def clear_transactions(self):
        self.run_query("DELETE FROM transactions", ())

if __name__ == "__main__":
    transactions = Transaction('test.db')
    transactions.clear_transactions()
    transactions.add_transaction(to_dict((5, 23.61, 'test1', '2004-03-30', 'testing')))
    transactions.add_transaction(to_dict((5, 19.72, 'test2', '2004-02-25', 'testing')))
    transactions.add_transaction(to_dict((5, 24.00, 'test3', '2004-03-03', 'testing')))
    transactions.add_transaction(to_dict((5, 24.00, 'test3', '2002-03-03', 'testing')))
    transactions.add_transaction(to_dict((5, 24.00, 'test3', '2005-03-03', 'testing')))
    print(transactions.show_transactions())
    print(transactions.summarize_by_month())
    print(transactions.summarize_by_year())
