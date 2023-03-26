from transaction import Transaction
import sys

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            transation quit
            transaction show
            transaction add item# amount category date description
            transaction delete item#
            transaction summarize_by_date
            transaction summarize_by_month
            transaction summarize_by_year
            transaction summarize_by_category
            transcation clear_transactions
            '''
            )
    
def print_transactions(transactions):
    ''' print the transaction items '''
    if transactions is None:
        print('no transactions to print')
        return
    if len(transactions)==0:
        print('no transactions to print')
        return
    print('\n')
    print(('item #', 'amount', 'category', 'date', 'description'))
    print('-'*40)
    for item in transactions:
        values = tuple(item) #(item #, amount, category, date, description)
        print(values)

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction()'''
    transaction = Transaction("transactions.db")
    if arglist==[]:
        print_usage()
    elif arglist[0]=="quit":
        exit()
    elif arglist[0]=="show":
        print_transactions(transaction.show_transactions())
    elif arglist[0]=="summarize_by_date":
        print_transactions(transaction.summarize_by_date())
    elif arglist[0]=="summarize_by_month":
        print_transactions(transaction.summarize_by_month())
    elif arglist[0]=="summarize_by_year":
        print_transactions(transaction.summarize_by_year())
    elif arglist[0]=="summarize_by_category":
        print_transactions(transaction.summarize_by_category())
    elif arglist[0]=="clear_transactions":
        print_transactions(transaction.clear_transactions())
    elif arglist[0]=='add':
        if len(arglist)!=6:
            print_usage()
        else:
            trans = {'item #':arglist[1],'amount':arglist[2],'category':arglist[3],'date':arglist[4],'description':arglist[5]}
            transaction.add_transaction(trans)
    elif arglist[0]=='delete':
        if len(arglist)!=6:
            print_usage()
        else:
            trans = {'item #':arglist[2]}
            transaction.delete_transaction(trans)
    else:
        print(arglist,"is not implemented")
        print_usage()

def toplevel():
    ''' read the command args and process them'''
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

    

toplevel()