#############################################################
#   Python 2.7 
#   Step 62 - Programming Drill from Python Course at The Tech Academy
#   by Jon Nuljon
#   December, 2016
#############################################################
#   What follows is quoted from the original drill description
#
#   Title:  'Datetime' – Python 2.7 – IDLE
#   Scenario:
#   The company you work for just opened two new branches. One is in New York City, the 
#   other in London. They need a very simple program to find out if the branches are open or
#   closed based on the current time of the Headquarters here in Portland. The hours of both
#   branches are 9:00AM - 9:00PM in their own time zone.
#   What is asked of you:
#   Create code that will use the current time of the Portland HQ to find out the time in the NYC &
#   London branches, then compare that time with the branches hours to see if they are open or
#   closed.
#   Print out if each of the two branches are open or closed.
#   Guidelines:
#	● Use Python 2.7 IDLE
#	● Use Datetime Module
#	● Execute program on the Shell
#############################################################
from datetime import *

# define a function that calculates status (Open|Closed) based on datetime in hours of operation (9am to 9pm)
def HOOstatus(dt):
	# if 9 am <= the hour < 10 pm
	if dt.hour in range(9,20,1):
		# store is open
		return ('Open')
	# otherwise
	else:
		# store is closed
		return('Closed')

# define a function that prints formatted output  given city and time zone offset relative to headquarters
def printOutput(city, offset):
	# calculate the current datetime with offset
	dt = datetime.now() + timedelta(hours=offset) 
	# pass the datetime to function to calculate operational status
	status = HOOstatus(dt)
	# format datetime and assign
	timeString = dt.strftime("  %I:%M %p %A")
	# print the  current time, day of week and operational status to console in the city we were given
	print "Right now, the time in {place} is: {time} and the store is {opStatus}".format(
		place=city, time=timeString, opStatus=status)

if __name__ == '__main__':
# assume we are running the code on a system located at Portland HQ
# initialize input
	STDinput=''
# prompt user for input from console
	STDinput = raw_input('Would you like to know operational status of our stores? (yes or no)')
# if user enters anything except no
	if (STDinput != 'no'):
		#print the status for each store including HQ
		printOutput("Portland",0) 
		printOutput('New York',3)
		printOutput('London',8)
	# otherwise exit 
	else:
		exit()