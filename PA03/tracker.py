from transaction import Transaction
import sys

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            transaction show
            transaction add name description
            transaction delete item_id
            '''
            )