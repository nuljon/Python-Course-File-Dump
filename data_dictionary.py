# Create programmer dictionary
epic_programmer_dict = {'Tim Berners-Lee' : 'tbl@gmail.com',
                        'Guido van Rossum' : 'gvr@gmail.com',
                        'Linus Torvalds': 'lt@gmail.com' }

# Check dictionary
# print epic_programmer_dict

# Check we can retrieve Tim's email 
# print epic_programmer_dict['Tim Berners-Lee']

# Changes email address
epic_programmer_dict['Tim Berners-Lee'] = 'tim@gmail.com'
# Check it changed correctly
# print 'New email for Tim: ' + epic_programmer_dict['Tim Berners-Lee']

# Add Larry Page and his email to the dictionary
epic_programmer_dict['Larry Page'] = 'lp@gmail.com'
# Delete Sergey Brin from the dictionary
# del epic_programmer_dict['Sergey Brin'] -- was an ERROR
del epic_programmer_dict['Linus Torvalds']
