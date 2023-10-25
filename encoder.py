#Emily Zucker

def menu():

    # function to display the menu and gather user choice.

    print('Menu\n' +
          '-' * 13 +
          '\n1. Encode\n' +
          '2. Decode\n' +
          '3. Quit\n')

    # loop to test that the user input is a valid choice/ is a digit.
    test = True
    while test:
        try:
            # gather user choice
            user_choice = int(input('Please choose an option from the menu: '))
            # if it is a digit it will be returned to main.
            return user_choice
        except:
            # if it is not a digit the user will be prompted to try again.
            print('Error, please enter a valid option.')


def encode():

    # function to encode the password

    # loop to test that the user is actually entering an 8 DIGIT password and not an 8 character password.
    test = True
    while test:
        try:
            # gather user input
            user_password = input('Please enter an 8 digit passcode: ')
            # if user_password cannot be converted to an integer, it contains non-digit characters and the
            # except clause will commence and tell them that.
            is_digit = int(user_password)
            # if it works, the loop can be stopped.
            break
        # if the password couldn't be converted to an int... tell the user and prompt them to reenter.
        except:
            print('Error, the passcode must only contain numeric digits.')


    # loop to test the length of the password. If the password is anything other than 8 characters long,
    # the loop will proceed and prompt the user to enter an 8 digit password.
    while len(user_password) != 8:
        print('Error. That is not 8 digits, please try again.')
        user_password = input('Please enter an 8 digit passcode: ')

    # initialize the password string. I chose to make it a string and not an integer so that it may be
    # iterated upon in the future in the decode() method.
    encoded_password = ''

    # loop to read the password and encode it.
    for item in user_password:
        digit = int(item)
        digit += 3
        encoded_password += f'{digit}'

    # tell the user the password has been encoded and saved and return the string to main.
    print('\nEncoded password saved!\n')
    return encoded_password


def main():

    # gather user input
    user_choice = menu()

    # menu loop
    proceed = True
    while proceed:

        if user_choice == 1:

            password = encode()
            user_choice = menu()

        elif user_choice == 2:

            pass
            # FIXME: decoder
            # note: the encode() method will not regulate password with the number 7 or above... this will lead
            # to digits of value 7 or above to be two digit numbers in the encoded password... assume that
            # the password will only contain digits 1-6.

        elif user_choice == 3:

            print('Goodbye.')
            quit()

        # if the user entered anything that isn't 1-3...
        else:

            # tell them it is invalid...
            print("Error. That is not a valid option. Please try again")
            # then initialize loop
            test = True
            while test:
                try:
                    user_choice = int(input('Please choose an option from the menu: '))
                    # if the option is a digit, we can exit the loop and continue to the next iteration.
                    test = False
                except:
                    # if it's not, then we tell the user and repeat this loop so they reenter their option.
                    print('Error, please enter a valid option.')

if __name__ == '__main__':

    main()