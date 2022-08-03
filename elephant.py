def elephant_swims(name):
    while True:
        yes_or_no = input(f'🐘 <--- This is elephant named {name} \n'
                          f'Do you want him to swim? (y/n) ')
        # не забудь про else
        if yes_or_no == 'y':
            print('🏝 🌊 🌊🐘🌊 🌊 🏝')
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
