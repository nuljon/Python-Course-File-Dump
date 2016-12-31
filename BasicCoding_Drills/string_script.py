
date ="12/05/2016"
# Go through string and split
# where there s a '/'
date_manip = date.split('/')
# show the outcome
print {'Month: ' + date_manip[0] +
       ' Day: ' + date_manip[1]
       + ' Year: ' + date_manip[2]}


