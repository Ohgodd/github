import time


def elephant_swims(name):
    while True:
        yes_or_no = input(f'🏠🐘 <--- This is elephant named {name} \n'
                          f'Do you want him to swim? (y/n) ')
        if yes_or_no == 'y':
            time.sleep(1)
            print(f'Please wait the {name} is trying to get to the ocean ....')
            time.sleep(2)
            print('🏝 🌊 🌊🐘🌊 🌊 🏝')
            time.sleep(3)
            print(f'🏝 🌊 🌊🐘🌊 🌊 🏝<--{name} is bored ')
            time.sleep(0.5)
            b = input('Should he go home? (y/n) ')
            if b == 'y':
                time.sleep(0.5)
                print('The elephant is running to home currently...')
                time.sleep(1)
                print('☀')
                print('🏠____________🐘💦___🌴🌊🌊🏄‍🌊🌊 ️')
                print('Please wait...')
                time.sleep(5)
            elif b == 'n':
                print('🏝 🌊 🌊🐘🌊 🌊 🏝')
                time.sleep(3)
                print(f'🏝 🌊 🌊🐘🌊 🌊 🏝<--{name} is REALLY bored now and he won\'t listen to you ')
                time.sleep(1.5)
                print('The elephant is running to home currently...')
                time.sleep(1)
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
