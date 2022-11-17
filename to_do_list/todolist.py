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
    msgAction3DeleteTask = '3 - Delete Task'
    msgAction0Exit = '0 - Exit'
    print(msgAskActionHead)
    print(msgAction1CreateTask)
    print(msgAction2ListTasks)
    print(msgAction3DeleteTask)
    print(msgAction0Exit)


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
                print('################### TO-DO-LIST ###################')
                for i in range(len(tasksList)):
                    print(i+1, '-', tasksList[i])

                # print('Your To-Do List: ', tasksList)
                print('\n################# END-OF-LIST ###################')
                printOptions()
                selectOption()
            else:
                print('\n#########################################')
                print('          YOUR LIST IS EMPTY')
                print('#########################################\n')
                printOptions()
                selectOption()
        case '3':
            print('################### TO-DO-LIST ###################')
            for i in range(len(tasksList)):
                print(i+1, '-', tasksList[i])

            print('\n################# END-OF-LIST ###################')
            taskToDelete = int(input('Task to Delete: '))
            tasksList.pop(taskToDelete-1)
            print('Task Removed')
            printOptions()
            selectOption()
        case _:
            print('Thank You')


tasksList = []
printHeader()
printOptions()
selectOption()
