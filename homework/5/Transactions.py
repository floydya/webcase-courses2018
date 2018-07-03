
"""Transaction
>>> a = Transaction(5, "date")
>>> a.amount = 7
>>> a
Transaction(7, date, USD, 1, None)
>>> a.date = "date_now"
>>> a
Transaction(7, date_now, USD, 1, None)
>>> a.currency = "RUB"
>>> a
Transaction(7, date_now, RUB, 1, None)
>>> a.usd_conversion_rate = 3
>>> a
Transaction(7, date_now, RUB, 3, None)
>>> a.usd
21
"""
#>>> a = Transaction(5, "date")
#>>> a.amount = -2
#>>> a
#Traceback (most recent call last):
#...
#AssertionError: amount must be nonzero and non-negative

class Transaction():

    def __init__(self, amount, date, currency="USD",
                 usd_conversion_rate=1, description=None):
        """Init class example
        >>> a = Transaction(5, "date")
        >>> a
        Transaction(5, date, USD, 1, None)
        """
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        self.__description = description
        self.__usd = amount * usd_conversion_rate


    @property
    def amount(self):
        """Amount of transaction
        >>> a = Transaction(5, "date")
        >>> a.amount
        5
        """
        return self.__amount
        self.__usd = self.__amount * self.__usd_conversion_rate

    @amount.setter
    def amount(self, amount):
        assert amount > 0, "amount must be nonzero and non-negative"
        self.__amount = amount

    @property
    def date(self):
        """Date of transaction
        >>> a = Transaction(5, "date")
        >>> a.date
        'date'
        """
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def currency(self):
        """Currency of transaction
        >>> a = Transaction(5, "date")
        >>> a.currency
        'USD'
        """
        return self.__currency

    @currency.setter
    def currency(self, currency):
        self.__currency = currency

    @property
    def usd_conversion_rate(self):
        """Conversion of transaction
        >>> a = Transaction(5, "date")
        >>> a.usd_conversion_rate
        1
        """
        return self.__usd_conversion_rate
    
    @usd_conversion_rate.setter
    def usd_conversion_rate(self, usd_conversion_rate):
        assert usd_conversion_rate > 0, "usd_conversion_rate must be nonzero and non-negative"
        self.__usd_conversion_rate = usd_conversion_rate
        self.__usd = self.__amount * self.__usd_conversion_rate

    @property
    def description(self):
        """Desc of transaction
        >>> a = Transaction(5, "date")
        >>> a.description
        
        """
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def usd(self):
        """USD of transaction
        >>> a = Transaction(5, "date")
        >>> a.usd
        5
        """
        return self.__usd

    def __repr__(self):
        return ("{0.__class__.__name__}({0.amount}, {0.date}, {0.currency}, {0.usd_conversion_rate}, {0.description})".format(self))

    def __str__(self):
        return "{0.__currency}(amount: {0.__amount}). Date: {0.__date}".format(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()