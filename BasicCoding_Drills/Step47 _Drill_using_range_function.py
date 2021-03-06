'''
Python Course - Step 47 - Programming Drills using Range()

Start IDLE and use the Python range() function with one parameter to display the
following:
0
1
2
3
'''
for i  in range(4):
    print(str(i), end='\n')
print(end='\n\n\n')

'''
When this is working show it to your instructor.
Use the Python range() function with 3 parameters to display the following:
3
2
1
0
'''
for i in range(3, -1, -1):
    print(i, end='\n')
print(end='\n\n\n')

'''
Use the Python range() function with 3 parameters to display the following:
8
6
4
2
'''
for  i in range(8, 0, -2):
    print(i, end='\n')
