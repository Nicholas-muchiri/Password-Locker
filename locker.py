import pyperclip
import secrets

import getpass
import string

class Userdata:
    '''
    Class that generates new instances of userdata class
    '''
    def create_user(self):
        '''
        function that creates new users
        '''
        print("Input your username and password:")
        username = str(input())
        print("input password:")
        upass = getpass.getpass()
        udata = {username: upass}
        file = open("login.txt", "a")
        file.write("\n" + str(udata))
        file.close()
        print(f" You have successfully created  an account for {username}")
        print(' Would you want to go on with this awesome program? Yes or No')
        opt = input().lower()
        if opt == 'Yes':
            controllers.login()
        elif opt== 'No':
            print('Thank you {username} login later.')
        exit()

userdata = Userdata()

class Credentials:
    '''
    Class that generates new instances of credentials class
    '''
    def generate_password(self):
        '''
        function generating passwords
        '''
        print('Enter the accounts name.(don\'t space)')
        accountFor = str(input())
        cnt = int(input('Input the lenght of password you want:'))
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(cnt))
        file = open("password store.txt", "a")
        file.write("\n" + accountFor+':'+password)
        print(f"password for account {accountFor} generated")
        file.close()
    # generate_password()

    def show_generatedPass(self):
        inputted_username = str(input('Enter your Accounts name:').lower())
        with open('passwordstore.txt') as f:
            for line in f:
                line2= line.split(':')
                if inputted_username in line2:
                    print(line)
                    break
            else:
                print(' SORRY but this Account doesn\'t exists')
                controllers.access_controller()
    # show_generatedPass()

    def copy_credentials(self):
        '''
         this function copies passwords for account to piperclip
        '''
        print("Which account do you want to copy password?:")
        name = str(input())
        f = open('password store.txt', 'r')
        for line in f.readlines():
            tag, key = line.strip().split(":")
            if (name in tag):
                key = key.strip()
                # print(key)
                pyperclip.copy(key)
                print(f" {name}s password has been copied")
        print('Program shutting down...')        
        exit()
    # copy_credentials()

credentials = Credentials()

class Controllers():
    def selector(self):
        '''
        function that controls the flow of the application
        '''
        print("login \n", "\n new user\n")
        selector_call = str(input())
        if selector_call == "new user":
           userdata.create_user()
            # selector()
        elif selector_call == "login":
            controllers.login()
        else:
            print("Naah {username}...You cant input that")
            controllers.selector()

    def access_controller(self):
        '''
        Gives options after  the login function is True
        '''
        print('generate password or view passwords')
        access_call = str(input())
        if access_call == 'generate password':
            credentials.generate_password()
            print("*"*35)
            print('Choose either to continue...')
            controllers.access_controller()
        elif access_call == 'viewpasswords':
            credentials.show_generatedPass()
            print("Do you want to copy the credentials?:YES or NO")
            called = input().lower()
            if called == 'YES':
               credentials.copy_credentials()

            else:
                print('Program shutting down')
                print('*'*30)
                exit()
        else:
            print('Ooh hell naah {username}...dont do that')


    def login(self):
        '''
        function that enables access to the system
        '''
        print('Logging in........')
        username = str(input('Input username; '))
        upass = getpass.getpass('Enter password; ')
        udata = {username: upass}
        if str(udata) in open('login.txt').read():
            # print("true")
            print(f'As{username}  you have successfully logged in lets have some fun...')
            print('*'*30)
            if True:
              controllers.access_controller()
        else:
            print('Bruh...input your correct shit manh')
controllers = Controllers()
controllers.selector()

