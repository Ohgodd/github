import time
import pygame

pygame.mixer.init()


def elephant_swims(name):
    elephant_trumpenting = pygame.mixer.Sound('ElephantTrumpeting.mp3')
    footsteps_on_grass = pygame.mixer.Sound('Footsteps(grass).mp3')
    ocean = pygame.mixer.Sound('ocean(3sec).mp3')
    footsteps = pygame.mixer.Sound('Footsteps2.mp3')
    ocean2 = pygame.mixer.Sound('ocean(1.5sec).mp3')
    while True:
        elephant_trumpenting.play()
        elephant_trumpenting.set_volume(0.3)
        yes_or_no = input(f'🏠🐘 <--- This is elephant named {name} \n'
                          f'Do you want him to swim? (y/n) ')
        if yes_or_no == 'y':
            time.sleep(1)
            print(f'Please wait the {name} is trying to get to the ocean ....')
            footsteps_on_grass.play()
            footsteps_on_grass.set_volume(0.5)
            time.sleep(2)
            print('🏝 🌊 🌊🐘🌊 🌊 🏝')
            elephant_trumpenting.play()
            ocean.play()
            ocean.set_volume(0.5)
            time.sleep(3)
            print(f'🏝 🌊 🌊🐘🌊 🌊 🏝<--{name} is bored ')
            ocean.play()
            time.sleep(2)
            b = input('Should he go home? (y/n) ')
            if b == 'y':
                time.sleep(0.5)
                print('The elephant is running to home currently...')
                elephant_trumpenting.play()
                time.sleep(1)
                footsteps.play()
                print('☀')
                print('🏠____________🐘💦___🌴🌊🌊🏄‍🌊🌊 ️')
                print('Please wait...')
                time.sleep(5)
            elif b == 'n':
                elephant_trumpenting.play()
                print('🏝 🌊 🌊🐘🌊 🌊 🏝')
                ocean.play()
                ocean.set_volume(0.5)
                time.sleep(3)
                print(f'🏝 🌊 🌊🐘🌊 🌊 🏝<--{name} is REALLY bored now and he won\'t listen to you ')
                ocean2.play()
                ocean2.set_volume(0.5)
                elephant_trumpenting.play()
                time.sleep(2)
                print('The elephant is running to home currently...')
                elephant_trumpenting.play()
                time.sleep(1)
                footsteps.play()
                print('☀')
                print('🏠____________🐘💦___🌴🌊🌊🏄‍🌊🌊 ️')
                print('Please wait...')
                time.sleep(5)
            else:
                print('Something went wrong ;(')
        elif yes_or_no == 'n':
            quit1 = input('So you want to quit? (y/n) ')
            if quit1 == 'y':
                break
            elif quit1 == 'n':
                do_you_love_elephants_swim = input('So you just don\'t want an elephant to swim? (y/n) ')
                if do_you_love_elephants_swim == 'y':
                    print('That\'s cute ^_^ ❤')
                elif do_you_love_elephants_swim == 'n':
                    print('You are weird, wdyw? ')
                else:
                    print('Something went wrong ;(')
            else:
                print('Something went wrong ;(')
        else:
            print('Something went wrong ;(')


elephant_swims(input('How do you want to name an elephant?\n > '))