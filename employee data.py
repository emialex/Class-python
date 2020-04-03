import random
import string


def id_generator(size=5, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(5))


def password():
    first_name = str((input('What is your first name? ')))
    last_name = str((input('what is your last name? ')))
    email = input('Input your email address: ')

    fname = first_name[0:2]
    lname = last_name[-2:]
    pword = fname + lname + id_generator(size=5, chars=string.ascii_uppercase)
    user_details = [first_name, email, last_name, pword]
    return user_details


def user():
    last_user = 'no'
    users = dict()
    while last_user == 'no':
        new_user = password()
        email = new_user[1]
        print(new_user[3])

        pword_acceptance = str(input('Is this suggested password okay by you? [yes/no] '))

        if pword_acceptance.lower() == 'yes':
            users[email] = new_user
            last_user = input('Are you the last user? [yes/no]: ')
            continue
        else:
            user_password = str(input('Okay then, input a valid password(not less than seven letters): '))

        while len(user_password) < 7:
            user_password = input('Input a valid password(not less than seven letters): ')
        else:
            new_user[3] = user_password
            users[email] = new_user

        last_user = input('Are you the last user? [yes/no]: ')
        continue

    return users


users_details = user()
for value in users_details.values():
    print()
    print(f'Name= {value[0]} {value[2]}')
    print(f'email= {value[1]}')
    print(f'password= {value[3]}')
    print()
    print()