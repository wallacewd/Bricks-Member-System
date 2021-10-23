# Brick's SMS (Simple Membership System)
# Author  :: Dan Wallace 
# Website :: www.brick.technology
# Requires python >= 3.10

# Import libraries
import hashlib
import json

# Method to complete registration and save hashed passwords
def complete_registration(username:str,password:str):
    ''' 
        >> Loads the member list json file
        >> After loading, check if the user already exists
        >> If the user doesn't exist, hash their password and store it
    '''
    # Load members json file into python dict
    data = json.load(open('members.json', 'r', encoding='utf-8'))

    # If username already exists in dict, try again
    if username in data.keys():
        print('Username allready exists. Try again.')

        # Returns with True to continue the while loop in register()
        return 'True'

    # Else hash the password provided and store username/password in members.json
    else:
        hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        data[username] = hashed 

        with open('members.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f'Hashed password saved: {hashed}')
        # Returns with False to stop the while loop in register()
        return 'False'

# Method to create login inputs
# Completes login process
def login():
    while True:
        ''' 
            >> Check if username exists and if hashed input matches hashed password
            >> If user/pass match, allow login
        '''
        # Grab user inputs
        username = input('Username  :: ')
        password = input('Password  :: ')

        # Load member json and hash password attempt
        data = json.load(open('members.json', 'r', encoding='utf-8'))
        password_attempt = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Check if user exists else try again
        try:
            if username in data.keys():
                if data[username] == password_attempt:
                    print(f'Hello {username}! Welcome to Brick\'s SMS!')
                    break
                else:
                    print('Invalid password. Try again.')
            else:
                print(f'User: {username} does not exist')
        except KeyboardInterrupt:
            break

# Create registration inputs
def register(status='True'):
    while status=='True':
        username = input('Pick your username :: ')
        password = input('Pick your password :: ')
        re_check = input('Re-enter password  :: ')
        status = complete_registration(username,password) if password == re_check else print('Password does not match, try again.')

# Create registration inputs
def startup(command:str):
    match command.split():
        case ['login'|'log in'|'Login'|'l']:
            login()
        case ['register'|'signup'|'s'|'join'|'Register']:
            register()
        case other:
            print(f'Unrecognized command: {other}')

# Main function
def main():
    start = input('Login or Register? ')
    startup(start)

if __name__ == "__main__":
    main()
