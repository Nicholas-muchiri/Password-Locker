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
        print("Enter your username and password:")
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
        file = open("password_keeper.txt", "a")
        file.write("\n" + accountFor+':'+password)
        print(f"password for account {accountFor} generated")
        file.close()
    # generate_password()

    def show_generatedPass(self):
        inputted_username = str(input('Enter your Accounts name:').lower())
        with open('password_keeper.txt') as f:
            for line in f:
                line2= line.split(':')
                if inputted_username in line2:
                    print(line)
                    break
            else:
                print(' SORRY This Account doesn\'t exists')
                controllers.access_controller()
    # show_generatedPass()

    def copy_credentials(self):
        '''
        function copies passwords for account to piperclip
        '''
        print("please specify account name to copy password:")
        name = str(input())
        f = open('password_keeper.txt', 'r')
        for line in f.readlines():
            tag, key = line.strip().split(":")
            if (name in tag):
                key = key.strip()
                # print(key)
                pyperclip.copy(key)
                print(f"password for account {name} copied")
        print('your now exiting...')        
        exit()
    # copy_credentials()

credentials = Credentials()



class Controllers():
    def selector(self):
        '''
        function that controls the flow of the application
        '''
        print('please use the codes below to continue:')
        print("log-for registered users\n", "\nnew-for new user\n")
        selector_call = str(input())
        if selector_call == "new":
           userdata.create_user()
            # selector()
        elif selector_call == "log":
            controllers.login()
        else:
            print("illegal code input")
            controllers.selector()


    def access_controller(self):
        '''
        Gives options after login function is True
        '''
        print('genpass-for generate passwords or viewc-view saved credentials')
        access_call = str(input())
        if access_call == 'genpass':
            credentials.generate_password()
            print("*"*35)
            print('to continue, choose option')
            controllers.access_controller()
        elif access_call == 'viewc':
            credentials.show_generatedPass()
            print("copy credentials?:y or n")
            called = input().lower()
            if called == 'y':
               credentials.copy_credentials()

            else:
                print('thanks for your time.your are now exiting')
                print('*'*30)
                exit()
        else:
            print('illegal input')


    def login(self):
        '''
        function that enables access to the system
        '''
        print('Logging in........')
        username = str(input('Please enter username: '))
        upass = getpass.getpass('Please enter password: ')
        udata = {username: upass}
        if str(udata) in open('login.txt').read():
            # print("true")
            print(f'correct credentials: Your are now logged in as {username}')
            print('*'*30)
            if True:
              controllers.access_controller()
        else:
            print('incorrect credentials')

controllers = Controllers()
controllers.selector()

