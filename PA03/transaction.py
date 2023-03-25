
import sqlite3
import os

def toDict(t):
    ''' t is a tuple (rowid, title, desc, completed)'''
    print('t='+str(t))
    todo = {'rowid':t[0], 'title':t[1], 'desc':t[2], 'completed':t[3]}
    return todo

class Transaction():

    def __init__(self, filename):
        self.database = filename
        self.runQuery(f'''CREATE TABLE IF NOT EXISTS transactions
                        (item # integer, amount real, category text, date text, description text)''',())

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+f'/{self.database}')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
    
    def showTransactions(self):
        ''''''
        return self.runQuery()

    def addTransaction(self, transaction):
        '''creates and adds a transaction to the database'''
        return self.runQuery("INSERT INTO transactions VALUES (?,?,?,?,?)", 
                            (transaction['item #'], transaction['amount'], transaction['category'], transaction['date'], transaction['description']))

    def deleteTransation(self, itemNum):
        '''deletes the transaction with the specified item number'''
        return self.runQuery("DELETE FROM transactions WHERE item # = (?)", (itemNum))
    
