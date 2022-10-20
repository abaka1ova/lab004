<<<<<<< Updated upstream
import test


def repeat(lists):
    i = 0
    index = 0
    min = len(lists)
    for list in lists:
        if len(list) > min:
            min = len(list)
            index = i
        i += 1
    rep = list
    run = True
    j = 0
    i = 0
    while run:
        try:
            for i in range(len(lists)):
                for j in range(len(lists[i])):
                    if lists[i][j] in lists[i+1]:
                        if lists[i] in rep:
                            None
                        else:
                            rep.append(lists[i][j]) #массив с повтор. элементами
        except IndexError:
            run = False
    if len(rep) > 0:
        print('Количество одинаковых элементов: ', len(rep))
    else:
        print('Одинаковых элементов нет')


repeat(test.my_input())
=======
def repeat(l):
        lists = l
        i = 0
        index = 0
        min = len(lists)
        for list in lists:
            if len(list) > min:
                min = len(list)
                index = i
            i += 1
        rep = []
        run = True
        j = 0
        i = 0
        while run:
            try:
                for i in range(len(lists)):
                    for j in range(len(lists[i])):
                        if lists[i][j] in lists[i + 1]:
                            if lists[i] in rep:
                                None
                            else:
                                rep.append(lists[i][j])  # массив с повтор. элементами
            except IndexError:
                run = False
        if len(rep) > 0:
            print('Количество одинаковых элементов: ', len(rep))
            print('Oдинаковыe элементы: ', rep)
        else:
            print('Одинаковых элементов нет')
>>>>>>> Stashed changes
