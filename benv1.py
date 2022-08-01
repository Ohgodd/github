# pocket ben v1
import random

gay = False
command = ''


def ben_generator():
    print('You are currently talk to Ben')
    while True:
        command2 = input('Input your question: ')
        list2 = ['Yes', 'No', 'HOHOHO', 'Ugh...']
        if command2 == 'quit':
            print('The Ben is coming for you ')
            break
        ben_answer = random.choice(list2)
        print(ben_answer)


ben_generator()