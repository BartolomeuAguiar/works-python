# This app creates a TO-DO list in pure python 3
# Author: Bartolomeu Aguiar
# Início do Projeto: 11/2022

# Print a Header App
def printHeader():
    msgIntroApp = '###This app creates a TO-DO list in pure python 3###'
    msgIntroAppDecorate = '###################################################'
    print(msgIntroAppDecorate)
    print(msgIntroApp)
    print(msgIntroAppDecorate)


# Define and print the options menssages
def printOptions():
    msgAskActionHead = 'Please select an option:'
    msgAction1CreateTask = '1 - Create New Task'
    msgAction2ListTasks = '2 - List Tasks'
    msgAction3ListTasks = '3 - Exit'
    print(msgAskActionHead)
    print(msgAction1CreateTask)
    print(msgAction2ListTasks)
    print(msgAction3ListTasks)


def selectOption():
    print('______________________________________________')
    optionSelected = input('Insert a Option Code: ')

    match optionSelected:
        case '1':
            tempTask = input('Insert a task description: ')
            tasksList.append(tempTask)
            printOptions()
            selectOption()
        case '2':
            if len(tasksList) != 0:
                print('#########################################')
                print('Your To-Do List: ', tasksList)
                print('\n#########################################')
                printOptions()
                selectOption()
            else:
                print('\n#########################################')
                print('          YOUR LIST IS EMPTY')
                print('#########################################\n')
                printOptions()
                selectOption()
        case _:
            print('Thank You')


tasksList = []
printHeader()
printOptions()
selectOption()
