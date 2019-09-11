#!/usr/bin/python3

import sqlite3

def hello(name):
    # F format strings pls. Written in 3.5
    print('Hello {}!'.format(name))


class Transaction():

    def __init__(self, description, value):
        self.desc = description
        self.value = value


class TransactionsDAO():

    def __init__(self):
        self.connection = sqlite3.connect('transactions.db')
        self.cursor = self.connection.cursor()
        self.ensure_databases_initialize()

    def add_transaction(self, transaction):
        sql = 'INSERT INTO transactions (' \
              'descript, value_change' \
              ') VALUES (?, ?)'
        self.cursor.execute(sql, (transaction.desc, transaction.value))
        self.connection.commit()

    def ensure_databases_initialize(self):
        sql = 'CREATE TABLE IF NOT EXISTS transactions(' \
              'transaction_id INTEGER PRIMARY KEY AUTOINCREMENT, ' \
              'descript TEXT, ' \
              'value_change INTEGER)'
        self.cursor.execute(sql)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

def record_transaction(cost, description):
    # Transactions object created
    tdao = TransactionsDAO()

    # Create Transaction from arguments
    new_transaction = Transaction(description, cost)

    # use Transactions Data Access Object
    tdao.add_transaction(new_transaction)

