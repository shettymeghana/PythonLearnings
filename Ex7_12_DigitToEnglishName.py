#Write a function named "digit_name" that takes an integer argument in the range from 1 to 9, Inclusive,
#and Prints the English name for that integer on the computer screen

digit_dictionary = {1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five', 6 : 'Six',
                    7 : 'Seven',  9 : 'Nine', 10 : 'Ten'}

def digit_name(user_number):
    if digit_dictionary.has_key(user_number):
        print "English name of user entered digit %d is \'%s\' " %(user_number,digit_dictionary[user_number])
    else:
        print " English value of %d is not found on the digit_dictionary. Please add it" %user_number
        exit(1)
if __name__ == '__main__':
    user_number1 = int(raw_input("Enter digit range between 1 - 9 -> "))
    if user_number1 <= 0 or user_number1 >= 10:
        print "Invalid user input"
        exit(1)
    else:
        digit_name(user_number1)
