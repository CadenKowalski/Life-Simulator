import random
def Life_Simulator():
    global Money
    global player_info
    global Suicide
    global Sickness
    global Last_P_Situation
    global P_Situation
    print('Project Info: Made by Caden Kowalski, Project Start Date: 12/3/18')
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
        player_info = [] #[Gender, First Name, Last Name, Age, Happiness, Health, Smarts, Looks] 
        gender = random.randint(1,2)
        if gender == 1:
            player_info.append('Boy')
            select_name = random.randint(1, len(boy_f_names))
            player_info.append(boy_f_names[select_name])
        else:
            player_info.append('Girl')
            select_name = random.randint(1, len(girl_f_names))
            player_info.append(girl_f_names[select_name])
        select_name = random.randint(1, len(l_names))
        player_info.append(l_names[select_name])
        Age = 0
        player_info.append(Age)
        Happiness = random.randint(1, 100)
        player_info.append(Happiness)
        Health = random.randint(1, 100)
        player_info.append(Health)
        Smarts = random.randint(1, 100)
        player_info.append(Smarts)
        Looks = random.randint(1, 100)
        player_info.append(Looks)
    def Prints(Situation):
        if Situation == 'Sick':
            print('You are sick')
    def Get_Action(Situation):
        global player_info
        global Suicide
        global Sickness
        global Last_P_Situation
        global P_Situation
        if Situation == 'Baby':
            print('1.) Age')
            print('2.) Go to the doctor')
            print('3.) End Life')
            Action = input('Choose an action: ')
            while Action != '1' and Action != '2' and Action != '3':
                print('Invalid input')
                Action = input('Choose an action: ')
            if Action == '1':
                player_info[3] += 1
                if Sickness == True:
                    player_info[5] -= 2
                Sick = random.randint(1,2)
                if Sick == 1:
                    Sickness = True
                    P_Situation = 'Sick'
                print('Age: ' + str(player_info[3]))
                print('Happiness: ' + str(player_info[4]) + '%')
                print('Health: ' + str(player_info[5]) + '%')
                print('Smarts: ' + str(player_info[6]) + '%')
                print('Looks: ' + str(player_info[7]) + '%')
            elif Action == '2':
                if Sickness == True:
                    print('You have been cured')
                    Sickness = False
                    P_Situation = Last_P_Situation
                else:
                    print('You are not sick')
            else:
                Suicide = True
    Suicide = False
    Sickness = False
    print('1.) Start a new life')
    action = input('Choose an action: ')
    while action != '1':
        print('Invalid input')
        action = input('Choose an action: ')
    if action == '1':
        New_Life()
        print('My name is: ' + player_info[1] + ' ' + player_info[2])
        P_Situation = 'Baby'
        A_Situation = 'Baby'
        Last_P_Situation = 'Baby'
    print('Age: ' + str(player_info[3]))
    print('Happiness: ' + str(player_info[4]) + '%')
    print('Health: ' + str(player_info[5]) + '%')
    print('Smarts: ' + str(player_info[6]) + '%')
    print('Looks: ' + str(player_info[7]) + '%')
    while Suicide != True:
        Prints(P_Situation)
        if Suicide == False:
            Get_Action(A_Situation)
    print('You Died at the age of: ' + str(player_info[3]))
Life_Simulator()
