
import Transactions
import pickle


acc_list = []

"""Accounts
>>> a = Accounts("username")
>>> a.id
1
>>> a.name
username
>>> a.name = "asd"
Traceback (most recent call last):
...
AssertionError: len of 'name' must be more than 4
>>> a.name = "new_name"
>>> a.name
new_name
"""



class Accounts():


    def __init__(self, name):
        self.__id = len(acc_list)+1
        self.__name = name
        self.__transactions = list()
        acc_list.append(self)
        
    
    @property
    def id(self):
        return self.__id


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        assert len(name) > 4, "len of 'name' must be more than 4"


    def __len__(self):
        """Count transactions by len(Accounts-object)
        >>> a = Accounts("username")
        >>> len(a)
        0
        """
        return len(self.__transactions)


    @property
    def balance(self):
        balance = 0
        for i in self.__transactions:
            balance += i.amount
        return balance


    @property
    def all_usd(self):
        for tr in self.__transactions:
            if tr.currency != "USD":
                return False
        return True


    def apply(self, other):
        """
        >>> t = Transactions.Transaction(5, "date")
        >>> a = Accounts("username")
        >>> a.apply(t)
        >>> a.balance
        5
        >>> len(a)
        1
        """
        assert isinstance(other, Transactions.Transaction), "this object is not Transaction example"
        self.__transactions.append(other)


    def save(self, name):
        """
        >>> t = Transactions.Transaction(5, "date")
        >>> a = Accounts("username")
        >>> a.save('test')
        Traceback (most recent call last):
        ...
        AssertionError: file must be .acc
        >>> a.save('account1.acc')
        True
        """
        assert name.endswith('.acc'), "file must be .acc"
        with open(name, 'wb') as f:
            pickle.dump(self, f)
            return True

    @staticmethod
    def load(name):
        """
        >>> a = Accounts.load('Accounts.py')
        Traceback (most recent call last):
        ...
        AssertionError: file must be .acc
        >>> a = Accounts.load('account1.acc')
        >>> a.name
        'username'
        """
        assert name.endswith('.acc'), "file must be .acc"
        with open(name, 'rb') as f:
            return pickle.load(f)


if __name__ == "__main__":
    import doctest
    doctest.testmod()