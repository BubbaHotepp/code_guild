import csv
 

def create(x):
    print('To create new entry enter the person\'s last name, first name, email, and phone number.')
    last_name = input('Last name: ')
    first_name = input('First name: ')
    email = input('e-mail: ')
    phone_number = input('Phone number: ')
    x = x + {f'Last_Name:{last_name},First_Name:{first_name},email:{email},Phone_Number:{phone_number}'}

def retrieve(x):
    print('To retrieve a contact, please enter last name and first name.')
    last_name = input('Last name: ')
    first_name = input('First name: ')
    items_list = x.items()
    for i in items_list:
        if item[i] == last_name:
            if item[i] == first_name:
                y = item[i]
    print(y)

def update():
    stuff

def delete():
    more 


def main():
    with open('contacts.csv') as f:
        reader = csv.DictReader(f)
        contact_dict = [r for r in reader]

    user_input1 = input('Would you like to [C]reate, [R]etrieve, [U]pdate, or [D]elete a record?: ')
    if user_input1 == 'C' or user_input1 == 'c':
        create(contact_dict)
    elif user_input1 == 'R' or user_input1 == 'r':
        retrieve(contact_dict)
    elif user_input1 == 'U' or user_input1 == 'u':
        update(contact_dict)
    elif user_input1 == 'D' or user_input1 == 'd':
        delete(contact_dict)
    else:
        print('only cru or d')
    
    
    print(user_input1)    

main()