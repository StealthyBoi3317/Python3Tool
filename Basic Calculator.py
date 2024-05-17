
print('Basic Calculator: Made By Owen M.')
print('')

typeOfCalc = input('What type of calculator? (Division, Multiplication, Addition, Exponents, Subtraction): ')

if typeOfCalc == 'Division':
    print('Welcome to Division Calculator!')
    print('')
    divNum1 = float(input('Enter Number 1: '))
    divNum2 = float(input('Enter Number 2: '))
    divAnswer = str(divNum1 / divNum2)

    print('Your answer is: ' + divAnswer + '.')

if typeOfCalc == 'Multiplication':
    print('Welcome to Multiplication Calculator!')
    print('')
    multNum1 = float(input('Enter Number 1: '))
    multNum2 = float(input('Enter Number 2: '))
    multAnswer = str(multNum1 * multNum2)

    print('Your answer is: ' + multAnswer + '.')

if typeOfCalc == 'Addition':
    print('Welcome to Addition Calculator!')
    print('')
    addNum1 = float(input('Enter Number 1: '))
    addNum2 = float(input('Enter Number 2: '))
    addAnswer = str(addNum1 + addNum2)

    print('Your answer is: ' + addAnswer + '.')

if typeOfCalc == 'Exponents':
    print('Welcome to Exponent Calculator!')
    print('')
    expNum1 = float(input('Enter Number: '))
    expNum2 = float(input('Enter Exponent: '))
    expAnswer = str(expNum1 ** expNum2)
    

    print('Your answer is: ' + expAnswer + '.')

if typeOfCalc == 'Subtraction':
    print('Welcome to Subtraction Calculator!')
    print('')
    subNum1 = float(input('Enter Number: '))
    subNum2 = float(input('Enter Number 2: '))
    subAnswer = str(subNum1 - subNum2)
    

    print('Your answer is: ' + subAnswer + '.')

