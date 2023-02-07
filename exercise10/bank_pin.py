# This program emulates the high-street bank mechanism for checking a pin.

actual_pin = '9632'

chances = 0
attempts = 3
pinCheck = 0

while chances < attempts and pinCheck == 0:
    supplied_pin = input('Enter your PIN: ')
    if supplied_pin == actual_pin:
        pinCheck = 1
    else:
        chances += 1
        attemptsMade = (attempts-chances)
        print('Incorrect PIN: you have ' + str(attemptsMade) + ' attempts remaining')
if pinCheck == 1:
    print('Pin entered successfully')
else:
    print('Maximum tries exceeded. Your account has been locked. Please contact your card issuer for further details.')
