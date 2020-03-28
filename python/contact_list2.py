import csv
import collections

def create(x):
    while True:
        print('To create new entry enter the person\'s last name, first name, email, and phone number.')
        last_name = input('Last name: ')
        first_name = input('First name: ')
        email = input('e-mail: ')
        phone_number = input('Phone number: ')
        x.append({f'Last_Name:{last_name},First_Name:{first_name},email:{email},Phone_Number:{phone_number}'})
        
        cont_input = input('Would you like to create another contact? Y/N: ')
        if cont_input in ('Y','y'):
            continue
        else:
            break

def retrieve(x):
    while True:
        print('To retrieve a contact, please enter last name and first name.')
        last_name = input('Last name: ')
        first_name = input('First name: ')
        for item in x:
            if item['Last Name'] == last_name:
                if item['First Name'] == first_name:
                    fname = item['First Name']
                    lname = item['Last Name']
                    email = item['email']
                    phone = item['Phone Number']
                    print(f'Contact info:\nLast name: {lname}\nFirst name: {fname}\nemail: {email}\nPhone number: {phone}')
                    break
                else:
                    continue
            else:
                continue
        
        cont_input = input('Would you like to retrieve another contact? Y/N: ')
        if cont_input in ('Y','y'):
            continue
        else:
            print('Only enter Y/y or N/n.')
           

def update():
    while True:
        cont_input = input('Would you like to retrieve another contact? Y/N: ')
        if cont_input in ('Y','y'):
            continue
        elif cont_input in ('N','n'):
            break
        else:
            print('Only enter Y/y or N/n.')
    pass 
    

def delete():
    while True:
        cont_input = input('Would you like to retrieve another contact? Y/N: ')
        if cont_input in ('Y','y'):
            continue
        elif cont_input in ('N','n'):
            break
        else:
            print('Only enter Y/y or N/n.')
    pass

def main():
    dict_list = []

    with open('contacts.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        contact_list = [r for r in reader]
        x = 0
        y = 0
        for rows in reader:
            y = rows
        while x <= y:
            for i in contact_list:
                dict_list.append(dict(collections.OrderedDict(i)))
            x += 1
    
    while True:
        while True:            
            user_input1 = input('Would you like to [C]reate, [R]etrieve, [U]pdate, or [D]elete a record?: ')
            if user_input1 == 'C' or user_input1 == 'c':
                create(dict_list)
                break
            elif user_input1 == 'R' or user_input1 == 'r':
                retrieve(dict_list)
                break
            elif user_input1 == 'U' or user_input1 == 'u':
                update(dict_list)
                break
            elif user_input1 == 'D' or user_input1 == 'd':
                delete(dict_list)
                break
            else:
                print('Please enter only C/c, R/r, U/u, or D/d.')
        
        cont_input = input('Do you wish to continue? Y/N: ')
        if cont_input in ('Y','y'):
            continue 
        else:
            break
   
main()