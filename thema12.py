"""
/*
* This method urges the user to insert a credit card number
* If the user enters a character which is not a number it throws
* VallueError exception. When the user inserts a number smaller
* or larger than 16 numbers it throws an error as well.
*/
"""
def inputCreditCardNumber():
    while True:
        try:
            userInput = int(input("Give the credit card number: "))
        except ValueError:
            print("Do not enter characters only integers! Try again.")
            continue
        else:
            if(len(str(userInput)) == 16):
                return userInput
                break
            else:
                print("The credit card should be exact 16 digits")
                continue

"""
/*
* This method inserts the credit card number
* into a list
* @ return creditCardList: Returns a list of the credit card numbers
*/
"""
def insert_credit_card_number_into_list(creditCardNumber):
    creditCardList = []
    convert_credit_card_into_string = str(creditCardNumber)
    for i in range(0, 16):
        creditCardList.append(int(convert_credit_card_into_string[i]))
    return creditCardList


"""
/*
* This method uses the luhn algirith and
* calculates if the card number is a valid
* credit card number or not
*/
"""
def luhn_algorithm(creditCardNumber):
    flag = False
    verificationsDigit = calculate_odd_numbers(creditCardNumber) + calculate_even_numbers(creditCardNumber)
    if(verificationsDigit%10 == 0):
        print("Valid credit card number")
        return True
    else:
        print("Not valid credit card number")
    return flag


"""
/*
* It adds the odd numbers
* @return sum_odd_numbers: It returns the sum of odd numbers
*/
"""
def calculate_odd_numbers(creditCardNumber):
    sum_odd_numbers = 0
    for i in range(1, 16, 2):
        sum_odd_numbers = sum_odd_numbers + creditCardNumber[i]
    return sum_odd_numbers

"""
/*
* It adds the even numbers
* @return sum_even_numbers: It returns the sum of even numbers
*/
"""
def calculate_even_numbers(creditCardNumber):
    sum_even_numbers = 0
    for i in range(0, 16, 2):
        sum_even_numbers = sum_even_numbers + calculate_number_larger_than_nine(creditCardNumber[i])
    return sum_even_numbers

"""
/*
* Multiplies the inserted number by two
* If the number is nine or less, it returns
* the amount otherwise it splits the numbers
* and returns the sum
* @return total_sum: Returns the sum of a split number
* @return multiplied_number: Returns the number multiplied by two
*/
"""
def calculate_number_larger_than_nine(number):
    multiplied_number = number * 2
    insert_in_list = []
    total_sum = 0
    if(multiplied_number > 9):
        convert_to_string = str(multiplied_number)
        for i in range(0, 2):
            insert_in_list.append(convert_to_string[i])
        total_sum = int(insert_in_list[0]) + int(insert_in_list[1])
        return total_sum
    else:
        return multiplied_number
"""
/**
* This method defines the credit card provider
* I made this method for two credit card providers
* Master card and Visa card. If a credit card number
* starts with '5' it's a Master card or if it starts
* with '4' it's a Visa card
*/
"""
def define_credit_card_provider(creditCardNumber):
    if(str(creditCardNumber[0]) == '5'):
        print("Master card!")
    if(str(creditCardNumber[0]) == '4'):
        print("Visa card!")

"""
This is where the program starts
"""
def main():
    flag = 'yes'
    while(flag.casefold() == 'yes'):
        creditCard = inputCreditCardNumber()
        credit_card_number_into_list = insert_credit_card_number_into_list(creditCard)
        if(luhn_algorithm(credit_card_number_into_list) == True):
            define_credit_card_provider(credit_card_number_into_list)
        flag = input("Insert 'yes' if you want to continue with other card or anything else to terminate the program: ")
    print("The program has been terminated!")

#Invokes the main method
main()
