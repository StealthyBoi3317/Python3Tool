#Made by StealthyBoi3317.

whileTrue = True

#While loop that forever loops the calculator after you use a calculator.
while whileTrue:
    print('Angle Calculator - Version 1')
    print('')
    typeOfCalc = input('What type of Calculator would you like to use? (Angle Addition Postulate, Angle Subtraction Postulate, Supplementary Angles Theorem) ')

    if typeOfCalc == "Angle Addition Postulate":
        angleNum1 = float(input('Enter first angle number: '))
        angleNum2 = float(input('Enter second angle number: '))

        print('Both of these angles add up to ' + str(angleNum1 + angleNum2) + ' degrees.')

    if typeOfCalc == "Angle Subtraction Postulate":
        angleNum1 = float(input('Enter first angle number: '))
        angleNum2 = float(input('Enter second angle number: '))

        print('Both of these angles subtract into ' + str(angleNum1 - angleNum2) + ' degrees.')

    if typeOfCalc == "Supplementary Angles Theorem":
        angleNum1 = float(input('Enter first angle number: '))
        angleNum2 = float(input('Enter second angle number: '))
        addsTo180 = None

    if angleNum1 + angleNum2 == 180:
        addsTo180 = True
        print('Angles 1 and 2 add up to 180 degrees where the total is ' + str(angleNum1 + angleNum2) + ' degrees.')
    else:
        addsTo180 = False
        print('Angles 1 and 2 do not add up to 180 degrees, where the total is ' + str(angleNum1 + angleNum2) + ' degrees.')

