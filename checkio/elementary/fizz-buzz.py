def checkio(number):
   if 0 < number <= 1000:
       if number % 3 == 0 and number % 5 == 0:
           return 'Fizz Buzz'
       elif number % 3 == 0 and number % 5 != 0:
           return 'Fizz'
       elif number % 3 != 0 and number % 5 == 0:
           return 'Buzz'
       else:
           return str(number)
