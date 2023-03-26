from transaction import Transaction
import sys

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            transation quit #whatever params here
            transaction show
            transaction add 
            transaction delete 
            transaction summarize_by_date
            transaction summarize_by_month
            transaction summarize_by_year
            transaction summarize_by_category
            '''
            )
    
def print_transactions(transactions):
    ''' print the transaction items '''
    if len(transactions)==0:
        print('no transactions to print')
        return
    print('\n')
    print("%-10s %-10s %-30s %-10s"%('item #', 'amount', 'category', 'date', 'description'))
    print('-'*40)
    for item in transactions:
        values = tuple(item.values()) #(item #, amount, category, date, description)
        print("%-10s %-10s %-30s %2d"%values)

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction()'''
    transaction = Transaction()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show":
        print_transactions(transaction.showTransactions())
    elif arglist[0]=="summarize_by_date":
        print_transactions(transaction.summarize_by_date())
    elif arglist[0]=="summarize_by_month":
        print_transactions(transaction.summarize_by_month())
    elif arglist[0]=="summarize_by_year":
        print_transactions(transaction.summarize_by_year())
    elif arglist[0]=="summarize_by_category":
        print_transactions(transaction.summarize_by_category())
    elif arglist[0]=='add':
        if len(arglist)!=6:
            print_usage()
        else:
            trans = {'item #':arglist[2],'amount':arglist[3],'category':arglist[4],'date':arglist[5],'description':arglist[6]}
            transaction.addTransaction(trans)
    else:
        print(arglist,"is not implemented")
        print_usage()

