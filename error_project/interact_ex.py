def interact():
    while True:
        try:
            user_input = int(input('Please input an integer : '))
        except ValueError:
            print('Please enter integer only ')
        else:
            print(f"{user_input} is {'even' if user_input % 2 == 0 else 'odd'}.")
        finally:
            user_input = input('Do you want to play again : ')
            if user_input != 'y':
                print('Goodbye')
                break


interact()