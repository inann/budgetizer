#!/usr/bin/python3

print('Hello World!')

class Budget(Object):

    def __init__(self, income=-1):
        if income < 0:
            self.get_income()
        else:
            self._income = income

    
    def get_income(self):
