

container = {}
xtodict = {'KEY': ''}


def creator(a):
    container.update({a: []})
    print('your list has been added to the program.')
    return


def turntodict(x):              # challenge 2
    xtodict['KEY'] = x
    return xtodict


def turntostr(x):               # challenge 2
    return str(x)


def my_add(a,x):
    x = turntodict(x)
    x = turntostr(x)

    if container[a] == []:
        container[a].append(x)
    elif len(container[a]) == 1:
        container[a] = container[a] + [container[a]+[x]]

    else:
        container[a] = container[a] + [container[a][-1]+[x]]
    print('value added to the list successfully.')
    print('you will be redirected to the main menu!')
    print()
    print()
    return


def containertolist():
    j = 1
    listoflists = []
    for i in container:
        j += 1
        listoflists.append(i)
    return listoflists


def show_container():
    if container == {}:
        print()
        print('There are no list in here... lets add some first')
        print()
        creator(input("ok enter your list's name here >>> "))
        print()
    else:
        print('here are your lists in the program: ')
        j = 1
        listoflists = []
        for i in container:
            print('{}_{}'.format(j, i))
            j += 1
            listoflists.append(i)
        return listoflists


def show_list(a):
    listoflists = containertolist()
    if a.isdigit():
        print(container[listoflists[int(a)-1]])
    else:
        print(container[a])
    return


def greetings():
    print()
    print("HELLOOOOO... \n" +
          "I Hope You're doing well today.\n" +
          "If you know the purpose of this program then lets start by adding a list by typing 'add'.\n" +
          "(by the way you can have multiple lists here ;)) )\n" +
          "and if you want me to walk you through the program type 'guide': ")
    a = input('>>> ')
    if a == 'add' or a == 'Add':
        creator(input("ok enter your list's name here >>> "))
        menu()
    elif a == 'guide' or a == 'Guide':
        print()
        print('so this is an awesome super program that adds any given variable to any given list.\n'
              'The program does this task in a special way.\n'
              'It creates another list containing the last data of the list and the data we want to add to it,'
              ' then adds the new list as the last element.\n'
              'start by adding a list. ')
        creator(input("ok enter your list's name here >>> "))
        menu()
    else:
        print()
        print('PLEASE enter a valid command...!!!!!')
        print('you will be redirected to the main menu!')
        menu()


def menu():
    a = 0
    while a != 5 or a != 'quit':
        print()
        print('so what do you please now???\n'+\
              'enter the name or the number of the desired command: ')
        print('1_ add list')
        print('2_ add to list')
        print('3_ show lists')
        print('4_ print a list')
        print('5_ quit')

        a = input('>>> ')
        if a.isdigit():
            a = int(a)

        if a == 1 or a == 'add list':
            print()
            creator(input("ok enter your list's name here >>> "))
            print()
            print('you will be redirected to the main menu!')
            print()
            print()

        elif a == 2 or a == 'add to list':
            print()
            print('what list do you want to add to?')
            print('enter the name or the number of the desired list: ')
            print()
            print()
            listoflists = show_container()
            print()
            b = input('>>> ')
            if b.isdigit():
                # print(container[listoflists[0]])
                # print (container[listoflists[int(b)-1]])
                my_add(listoflists[int(b)-1],(input('enter the variable you want to add >>> ')))
            else:
                my_add(container[b],input('enter the variable you want to add >>> '))
        elif a == 3 or a == 'show lists':
            print()
            show_container()
            print()
        elif a == 4 or a == 'print a list':
            print()
            show_container()
            print()
            inp = input('enter list name or number >>> ')
            if inp.isdigit():
                if int(inp) > len(containertolist()):
                    print()
                    print('PLEASE enter a valid command...!!!!!')
                    print('you will be redirected to the main menu!')
                    continue
                if int(inp) < len(containertolist()):
                    print()
                    print('PLEASE enter a valid command...!!!!!')
                    print('you will be redirected to the main menu!')
                    continue
                else:
                    show_list(inp)
            else:
                if inp in container:
                    show_list(inp)
                else:
                    print()
                    print('PLEASE enter a valid command...!!!!!')
                    print('you will be redirected to the main menu!')
                    continue
            print()
            print(' ;)) ')
            print()
            print('you will be redirected to the main menu!')
            print()
            print()

        elif a == 5 or a == 'quit':
            print()
            print('Good Bye :(( ')
            break

        else:
            print()
            print('PLEASE enter a valid command...!!!!!')
            print('you will be redirected to the main menu!')


greetings()
