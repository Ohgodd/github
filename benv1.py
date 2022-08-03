# pocket ben v1
import random
import pygame
pygame.mixer.init()
command = ''


def ben_generator():
    pygame.mixer.music.load('Ben.mp3')
    pygame.mixer.music.play()
    print('You are currently talk to Ben')
    while True:
        command2 = input('Input your question: ')
        list2 = ['Yes', 'No', 'HOHOHO', 'Ugh...']
        if command2 == 'quit':
            print('The Ben is coming for you ')
            break
        ben_answer = random.choice(list2)
        if ben_answer == 'Yes':
            pygame.mixer.music.load('Yes.mp3')
            pygame.mixer.music.play()
        elif ben_answer == 'No':
            pygame.mixer.music.load('No.mp3')
            pygame.mixer.music.play()
        elif ben_answer == 'Ugh...':
            pygame.mixer.music.load('Ugh.mp3')
            pygame.mixer.music.play()
        elif ben_answer == 'HOHOHO':
            pygame.mixer.music.load('Hohoho.mp3')
            pygame.mixer.music.play()
        print(ben_answer)


ben_generator()