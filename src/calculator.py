def calculator():
    options = ['1', '2', '3', '4']
    print('Selecione o n° da operação matemática: \n')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Divisão')
    print('4 - Multiplicação\n')
    selectedOption = input('Digite uma opção (1/2/3/4): ')
    if selectedOption in options:
        firstValue = int(input('Digite o primeiro valor: '))
        secondValue = int(input('Digite o segundo valor: '))
        if selectedOption == '1':
            print(str(firstValue) + " + " + str(secondValue) + " = " + str(int(firstValue + secondValue)))
        elif selectedOption == '2':
            print(str(firstValue) + " - " + str(secondValue) + " = " + str(int(firstValue - secondValue)))
        elif selectedOption == '3':
            print(str(firstValue) + " / " + str(secondValue) + " = " + str(int(firstValue / secondValue)))
        else:
            print(str(firstValue) + " * " + str(secondValue) + " = " + str(int(firstValue * secondValue)))
    else:
        print('Opção inválida.')

calculator()