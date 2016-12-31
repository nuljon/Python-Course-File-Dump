# epic programmer data dictionary
epic_programmer_dict = {
    'tim berners-lee' : ['tbl@gmail.com', 111],
    'guido van rossum' : ['gvr@gmail.com', 222],
    'linus torvalds': ['lt@gmail.com', 333],
    'larry page' : ['lp@gmail.com', 444],
    'sergey brin' : ['sb@gmail.com', 555]
    }
def searchPeople(personsName):
    # finds name in dictionary
    # lets change to try method so we can catch bad input
    try:
        personsInfo = epic_programmer_dict[personsName]
        print 'Name: ' + personsName.title()
        print 'Email: ' + personsInfo[0]
        print 'Number: ' + str(personsInfo[1])
    except:
        # If there are errors, then this code gets run.
        print 'No information found for that name'

userWantsMore = True
while userWantsMore == True:
    # get user input
    personsName = raw_input('Please enter a name: ').lower()

    # lets see if we got the dude
    searchPeople(personsName)

    # more?
    searchAgain = raw_input('Search again? (y/n)')

    # if yes flag = true
    if searchAgain == 'y':
        userWantsMore = True
    #else if no flag = false
    elif searchAgain == 'n':
        userWantsMore = False
    # anything else flag = false
    else:
        print "That wasn't a Yes or No response. Bye!"
        userWantsMore = False
