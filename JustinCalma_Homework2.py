#Import math library
import math

#Defining Main Function
def main():
    print_menu()


#Print Menu Choices
def print_menu():
    print("\n1.- Check a Palindrome")
    print("2.- Check a Word Square")
    print("3.- Quit")

    #Assigning User Input to Decision
    decision = get_menu_choice()

    #Calling Function Depending On User Choice
    if decision == 1:
        menu_check_palindrome()
        print_menu()
    elif decision == 2:
        menu_check_word_square()
        print_menu()
    elif decision == 3:
        print("Bye!")

#Get Menu Choice
def get_menu_choice():

    a = input("Select a function: ")
    run = False
    counter = 0
    while run == False:     
        for char in a:
            if char.isdigit() == False:
                print("ERROR: Enter a number between 1 and 3")
                a = input("Enter a number: ")
                break
            counter = counter + 1
        if counter == len(a):
            run = True
    decision = int(a)
    return decision

#Get the user input for phrase
def get_phrase():
    while True:
        try:
            phrase = str(input("Enter an English phrase: "))
            if not phrase:
                print("ERROR: Enter an English phrase")
                continue
            break
        except ValueError:
            print("ERROR: Enter an English phrase")
    return phrase

#check if each character in phrase is a palindrome
def is_palindrome(phrase):
    phrase = phrase.lower()

    i = 0
    j = len(phrase) - 1
    while i < j:
        while True:
            if phrase[i].isalpha():
                break
            i += 1
        while True:
            if phrase[j].isalpha():
                break
            j -= 1

        #compare i and j
        if phrase[i] != phrase[j]:
            return False

        #Incrementing and decrementing indices i and j
        i += 1
        j -= 1

    return True

#Printing if phrase is palindrome or not
def menu_check_palindrome():
    phrase = get_phrase()
    check = is_palindrome(phrase)
    if check == True:
        print('"%s"' ' is a palindrome!' % phrase)
    else:
        print('"%s"' ' is not a palindrome.' % phrase)

#Getting input for word square from user
def get_word_square():
    square = str(input("Enter the first line of the word square: "))
    for i in range(len(square) - 1):
        new_line = str(input("Enter the next line of the word square: "))
        square = square + new_line

    return square

#Checking if word square is true
def check_word_square(square):
    p = 0
    m = 0
    i = 0
    n = int(math.sqrt(len(square)))
    while i < (n * n): 
        word = square[i:n+i]
        for j in range(n):
            letter1 = word[j]
            letter2 = square[(j * n) + p]
            if letter1 != letter2:
                return False

        m = m + 1 #Go to next word in word square
        i = m * n #Change starting index to new word
        p = p + 1 #Change letters

    return True    

#Printing if the word square is true or not
def menu_check_word_square():
    square = get_word_square()
    check = check_word_square(square)

    i = 0
    n = int(math.sqrt(len(square)))
    while i < (n ** 2):
        print(square[i:i+n])
        i = i + n
        
    if check == True:
        print('is a word square!')
    else:
        print('is not a word square!')
    
main()
    
