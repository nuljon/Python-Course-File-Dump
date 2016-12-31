'''
Python 2.7

Tech Academy Drill - passing variables among functions

Author of exercise: Danial Christie

Drill taken by: Jon Nuljon 12/6/2016

'''

def start (nice =0,mean=0,name=""):
    # print (get_number()) #builin method print calls get_number function
    # print ("Hello {}!".format(get_name())) # format subs the braces fore the function
    #f_name = "Sarah"
    #l_name = "Conner"
    #age = 28
    #gender = "female"
    #get_info(f_name,l_name,age,gender)
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    #if a not a new game (existing name not empty) then thanks for playing again
    if name != "":
        print("\nThank You for playing again, {}!".format(name))
    else:                                #otherwise
        stop = False
        while stop != True:                      #until we stop
            if name == "":              #if no name
               name = get_name()         # getname
               stop = False             # dont stop
            elif name != "":         #else if we have a name
                print("\nWelcome, {}!".format(name))  # welcome and describe game
                print("\nIn this game, you will be greeted by several different people. \nYou can be nice or mean.")
                print("\nYour fate at the end of the game, will be influenced by your actions.")
                stop = True          # now stop
            else:                   # else we are out of bounds
                print ("error")         # report error
                stop = True        #Stop loop
    return name                     # return name ro start
        
def nice_mean(nice,mean,name):
    stop = False
    while stop != True:
        show_score(nice,mean,name) #call the show_score function
        pick = raw_input("\nA stranger approaches you and tries to start a conversation. Will you be nice or mean? n/m:").lower()
        if pick == "n":
            print("\nThey chat a bit, then wave goodbye and walk away smiling ...")
            nice = (nice +1)
            stop =  True
        elif pick == "m":
            print("\nThe stranger glares at you menacingly and abrubtly storms off ...")
            mean = (mean +1)
            stop = True
        else:
            print"\nThe answer needs to 'n' for nice or 'm' for mean"  # loop again
    score(nice, mean,name)          #call the score function


def show_score(nice, mean, name):
    print("\n{}, you currently have ({}, Nice) and ({}, Mean) points.".format(name,nice,mean))

def score(nice, mean,name):
    if nice > 5:
        print("\nYou are nice, {}. You will end up living happily ever after in a sweet home.".format(name))
        gameover(nice,mean,name)
    elif mean > 5:
        print("\nYou are mean, {}. You will end up living in a van down by the river.".format(name))
        gameover(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def gameover(nice,mean,name):
    stop = False
    while stop != True:
        choice = raw_input("\nWell thats it unless you want to play again? y/n").lower()
        if choice == "y":
            stop = True
            nice = 0
            mean = 0
            start (nice, mean, name)
        elif choice == "n":
            stop = True
        else:
            print("\n please reply 'y' for yes or 'n' for no.")
            stop = False
    print ("THANK YOU FOR PLAYING, {}!".format(name))
    exit()
                
def get_name():
    name = raw_input("What is your name?").capitalize() #query input from user at the console
    return name

if __name__ == "__main__":
    start()
    
