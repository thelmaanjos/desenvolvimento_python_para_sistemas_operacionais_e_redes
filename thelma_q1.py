import os

def printUserName():
    user = os.getlogin()
    try:
        print(f'Computer user\'s name is: {user}')
    except OSError:
        print('There was an error getting the user\'s name')

printUserName()