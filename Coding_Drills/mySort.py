'''
Step 49 DRILL:

Write your own version of the sorted() method in Python. This method should take a list as an argument and return a list that is sorted in ascending order. Call your method passing in the following lists as arguments and print out each sorted list to the shell. This should be an algorithm that you write. Do not use .sort() or the sorted() methods in your method.

[67, 45, 2, 13, 1, 998]

[89, 23, 33, 45, 10, 12, 45, 45, 45]

Your sorted lists should look like this when displayed:

[1, 2, 13, 45, 67, 998]

[10, 12, 23, 33, 45, 45, 45, 45, 89]

Your specific algorithm does not need to match the solution your Instructor has. It simply needs to work.

Once you've designed a program that meets the above qualifications, add it to your GitHub account. 
'''
def mySort(aList):
        print (aList, end=' is the list to be sorted\n\n')  # show the list we want to sort
        stop = len(aList)-1 			# since index start is 0 stop is length - 1
        while (stop>0):			# while we still have 2 items to compare
                for i in range(stop):	                # iterate until current stop
                        a,b=aList[i],aList[i+1]	                # assign two items from the list
                        if (a>b):			# if the first is bigger
                                aList[i],aList[i+1]=b,a	# then swap the values
                stop = stop -  1                                      # decrement stop
                # print (aList, end='...\n\n')	# debug
                
        return (aList)			# we're at the end

inputList = [67, 45, 2, 13, 1, 998]
outputList=mySort(inputList)
print(outputList,end=' this is what you get from mySort\n')
print("\nlet's try again with some tricky new input\n")
inputList = [89, 23, 33, 45, 10, 12, 45, 45, 45]
outputList=mySort(inputList)
print(outputList,end=' this is what you get from mySort\n')
