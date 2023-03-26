'''tracker.py is used to interface transaction.py
this handles all user input and performs the correct methods
based on user input'''
#written by Lucas Dia
import sys
from transaction import Transaction, to_dict


def print_usage():
    ''' print an explanation of how to use the commands
     Lucas Dia '''
    print('''usage:
            quit
            show
            add item# amount category date(YYYY-MM-DD) description
            delete item#
            summarize_by_date
            summarize_by_month
            summarize_by_year
            summarize_by_category
            clear_transactions
            '''
            )

def print_transactions(transactions, x):
    ''' print the transaction items 
    Lucas Dia'''
    if transactions is None:
        print('no transactions to print')
        return
    if len(transactions)==0:
        print('no transactions to print')
        return
    if x==1:
        print('\n')
        print(('item #', 'amount', 'category', 'date', 'description'))
        print('-'*40)
    if x==2:
        print('\n')
        print(('date', 'item #', 'amount'))
        print('-'*40)
    if x==3:
        print('\n')
        print(('month', 'item #', 'amount'))
        print('-'*40)
    if x==4:
        print('\n')
        print(('year', 'item #', 'amount'))
        print('-'*40)
    if x==5:
        print('\n')
        print(('category', 'item #', 'amount'))
        print('-'*40)
    
    for item in transactions:
        values = tuple(item) #(item #, amount, category, date, description)
        print(values)

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction()
    Lucas Dia'''
    transaction = Transaction("transactions.db")
    if arglist==[]:
        print_usage()
    elif arglist[0]=="quit":
        exit()
    elif arglist[0]=="show":
        print_transactions(transaction.show_transactions(), 1)
    elif arglist[0]=="summarize_by_date":
        print_transactions(transaction.summarize_by_date(), 2)
    elif arglist[0]=="summarize_by_month":
        print_transactions(transaction.summarize_by_month(), 3)
    elif arglist[0]=="summarize_by_year":
        print_transactions(transaction.summarize_by_year(), 4)
    elif arglist[0]=="summarize_by_category":
        print_transactions(transaction.summarize_by_category(), 5)
    elif arglist[0]=="clear_transactions":
        print_transactions(transaction.clear_transactions(), 0)
    elif arglist[0]=='add':
        if len(arglist)!=6:
            print_usage()
        else:
            transaction.add_transaction(to_dict(arglist[1:]))
    elif arglist[0]=='delete':
        if len(arglist)!=2:
            print_usage()
        else:
            transaction.delete_transaction(arglist[1])
    else:
        print(arglist,"is not implemented")
        print_usage()

def top_level():
    ''' read the command args and process them
    Lucas Dia'''
    if len(sys.argv)==1:
        # they didn't pass any arguments,
        # so prompt for them in a loop
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)


top_level()
