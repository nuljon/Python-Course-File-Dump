'''
Python Course step 38 Drill: write a python 2.7 program that demonstrates the following 12 requirements:
'''
# 12. Define a function that returns a string variable
def matchMadeInHeaven(myNumber,myInteger):
    myString=("\nNow that is a match made in heaven. Your number is " + str(myNumber) + " and " + str(myInteger))
    return myString
if __name__ == "__main__":

    #1. Assign an integer to a variable
    myInteger = 7

    #2. Assign a string to a variable
    myString = "Hello"

    #4. Use the print function and .format() notation to print out the variable you assigned
    print("{}, how nice to meet you. Your number is {}.".format(myString,myInteger))
    # 5. Use each of these operators
    myNumber = myInteger + 7 - 4 * 3 / 3 % 2
    print("\n Now your number is: {}".format(myNumber))
    myNumber += myNumber
    print("\n And now your number is: {}".format(myNumber))

    # 6. Use of logical operators: and, or, not
    # 7. Use of conditional statements: if, elif, else
    # 8. Use of a while loop
    stop = False
    while not stop:
        if myNumber < myInteger:
            stop = True
            print("\n And guess what? Now it is {}".format(myNumber))
            myInteger += myInteger
        elif myNumber == myInteger:
            stop = True
            # 13. Call the function you defined above and print the result to the shell
            myString = matchMadeInHeaven(myNumber,myInteger)
            print(myString)
            myInteger += myInteger
        else:
            print("\nYour number must feel large compared to {}\n".format(myInteger))
            # 9. Use of a for loop
            # 10. Create a list and iterate through that list using a for loop to print each item out on a new line
            myList = [myInteger, 2, 4, 6, 8, "feeling great"]
            for i in myList:
                print(" {} ... ".format(i))
            #11. Create a tuple and iterate through it using a for loop to print each item out on a new line
            myInteger = myInteger + 1
            myTupleList = [("my integer",myInteger),("your number",myNumber)]
            for item in myTupleList:
                print("\n What happened to our numbers?", item)

    quit()
