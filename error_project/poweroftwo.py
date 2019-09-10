def power_of_two():
    user_input = input('Please enter a number : ')
    try:
        n = float(user_input)
        n_sq = n ** 2
        return n_sq
    except ValueError:
        print('Your inputs was invalid, using default value 0')
        return 0


print(power_of_two())