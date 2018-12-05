print('Project Info: Made by Caden Kowalski, Project Start Date: 12/3/18')
import random
boy_f_names = ['Liam', 'Noah', 'William', 'James', 'Logan', 'Benjamin', 'Mason', 'Elijah', 'Oliver', 'Jacob', 'Lucas', 'Michael', 'Alexander', 'Ethan', 'Daniel', 'Mathew', 'Aiden', 'Henry', 'Jackson']
girl_f_names = ['Emma', 'Olivia', 'Sophia', 'Isabella', 'Ava', 'Mia', 'Emily', 'Abigail', 'Madison', 'Harper', 'Sofia', 'Avery', 'Elizabeth', 'Amelia', 'Aubrey', 'Ella', 'Chloe', 'Victoria', 'Grace']
l_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'Harris', 'Martin', 'Thompson', 'Robinson', 'Martinez', 'Clark']
own_names = input('Do you want to input some of your own names?: ').lower()
F_name = ''
while own_names != 'yes' and own_names != 'no':
    print('Invalid input')
    own_names = input('Do you want to input some of your own names?: ').lower()
if own_names == 'yes':
    while F_name != 'STOP':
        F_name = input('First Name: ')
        if F_name != 'STOP':
            F_name.capitalize()
        if F_name != 'STOP':
            gender = input('Boy or Girl?: ').capitalize()
            while gender != 'Boy' and gender != 'Girl':
                print('Invalid input')
                gender = input('Boy or Girl?: ').capitalize()
                if gender == 'Boy':
                    boy_f_names.append(F_name)
                else:
                    girl_f_names.append(F_name)
            L_name = input('Last Name: ').capitalize()
            l_names.append(L_name)
            print('Type "STOP" to start game')
def New_Life():
    global player_info
    player_info = [] #[Gender, First Name, Last Name, Happiness, Health, Smarts, Looks] 
    gender = random.randint(1,2)
    if gender == 1:
        player_info.append('Boy')
        select_name = random.randint(1, len(boy_f_names))
        player_info.append(boy_f_names[select_name])
    else:
        player_info.append('Girl')
        player_info.append(girl_f_names[select_name])
    select_name = random.randint(1, len(l_names))
    player_info.append(l_names[select_name])
    Happiness = random.randint(1, 100)
    player_info.append(Happiness)
    Health = random.randint(1, 100)
    player_info.append(Health)
    Smarts = random.randint(1, 100)
    player_info.append(Smarts)
    Looks = random.randint(1, 100)
    player_info.append(Looks)
    print(player_info)
New_Life()

