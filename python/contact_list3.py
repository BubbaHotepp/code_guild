import csv
import collections

def create(x):
    while True:
        print('To create new entry enter the person\'s last name, first name, email, and phone number.')
        last_name = input('Last name: ')
        first_name = input('First name: ')
        email = input('e-mail: ')
        phone_number = input('Phone number: ')
        x.append({'Last Name': last_name,'First Name': first_name, 'email': email, 'Phone Number': phone_number})

        with open('contacts.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                row = [f'{last_name}',f'{first_name}',f'{email}',f'{phone_number}']
                writer.writerows(row)
        
        # with open('contacts.csv') as csv_file:
        #     writer = csv.writer(csv_file)
        #     row = [f'{last_name}',f'{first_name}',f'{email}',f'{phone_number}']
        #     writer.writerows(row)

        while True:
            cont_input = input('Would you like to create another contact? Y/N: ')

            if cont_input.lower() == 'y':
                continue
            elif cont_input.lower() == 'n':
                break
            else:
                print('Please enter only y or n')
        
        if cont_input.lower() == 'n':
            break
        else:
            continue

def retrieve(x):
    while True:
        print('To retrieve a contact, please enter last name and first name.')
        last_name = input('Last name: ')
        first_name = input('First name: ')
        fname = ''
        
        for item in x:
            contact_lname = item['Last Name']
            contact_fname = item['First Name']
        
            if contact_lname.lower() == last_name.lower():
        
                if contact_fname.lower() == first_name.lower():
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
        
        if fname == '':
            print('Contact by that name not found.')
        
        else:
            continue

        while True:
            cont_input = input('Would you like to retrieve another contact? Y/N: ')

            if cont_input.lower() == 'y':
                continue
            elif cont_input.lower() == 'n':
                break
            else:
                print('Please enter only y or n')
        
        if cont_input.lower()== 'n':
            break
        else:
            continue

def update(x):
    while True:
        cont_input = ''
        print('Enter the last name and first name of the contact to update: ')
        last_name = input('Last Name: ')
        first_name = input('First Name: ')
        fname = ''
        
        for item in x:
            contact_lname = item['Last Name']
            contact_fname = item['First Name']
        
            if contact_lname.lower() == last_name.lower():
        
                if contact_fname.lower() == first_name.lower():
                    fname = item['First Name']
                    lname = item['Last Name']
                    email = item['email']
                    phone = item['Phone Number']
                    print(f'Contact info:\nLast name: {lname}\nFirst name: {fname}\nemail: {email}\nPhone number: {phone}')
                    
                    update_choice = input('Which part of contact do you wish to update?\n[F]irst name, [L]ast name, [e]mail, or [P]hone number? : ')
        
                    if update_choice.lower() == 'f':
                        update_edit = input(f'Please enter new first name: ')
                        item['First Name'] = update_edit
        
                    elif update_choice.lower() == 'l':
                        update_edit = input(f'Please enter new last name: ')
                        item['Last Name'] = update_edit
        
                    elif update_choice.lower() == 'e':
                        update_edit = input(f'Please enter new email address: ')
                        item['email'] = update_edit
        
                    else:
                        update_edit = input(f'Please enter new phone number: ')
                        item['Phone Number'] = update_edit
        
                elif fname == '':
                    print('Contact by that name not found.')
                
                else:
                    continue
        
            else:
                continue
        
        while True:
            
            cont_input = input('Would you like to update another contact? Y/N: ')

            if cont_input.lower() == 'y':
                break
            elif cont_input.lower() == 'n':
                break
            else:
                print('Please enter Y or N only.')
        
        if cont_input.lower() == 'y':
            continue 
        elif cont_input.lower() == 'n':
            break
        else:
            continue
    
def delete(x):
    
    while True:
        print('Enter the last name and first name of the contact to delete: ')
        last_name = input('Last Name: ')
        first_name = input('First Name: ')
        fname = ''
        
        for item in x:
            lname_temp = item['Last Name']
            fname_temp = item['First Name']
            
            if lname_temp.lower() == last_name.lower():
        
                if fname_temp.lower() == first_name.lower():
                    fname = item['First Name']
                    y = x.index(item)
                    affirm = input(f'Are you sure you want to delete contact\n{item}\nY or N? ')
                    
                    if affirm.lower() == 'y':
                        del x[y]
                    
                    else:
                        continue
                else:
                    list_indice += 1
                    continue

            else:
                list_indice += 1
                continue
        
        if fname == '':
            print('Contact by that name not found.')

        while True:
            cont_input = input('Would you like to delete another contact? Y/N: ')
            
            if cont_input.lower() == 'y':
                continue
            elif cont_input.lower() == 'n':
                break
            else:
                print('Please enter only y or n')

        if cont_input.lower() == 'n':
            break
        else:
            continue
        
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
            print(dict_list)
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
