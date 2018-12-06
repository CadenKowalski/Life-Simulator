import random
def Life_Simulator():
    global Money
    global player_info
    global Suicide
    global Sickness
    global Last_P_Situation
    global P_Situation
    global money
    print('Project Info: Made by Caden Kowalski, Project Start Date: 12/3/18, Time for completion: 3:09:21')
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
        mom = [] # [First Name, Last Name, Age, Relationship, Generosity, Money]
        dad = []
        gender = random.randint(1,2)
        if gender == 1:
            player_info.append('Boy')
            select_name = random.randint(1, len(boy_f_names) - 1)
            player_info.append(boy_f_names[select_name])
        else:
            player_info.append('Girl')
            select_name = random.randint(1, len(girl_f_names) - 1)
            player_info.append(girl_f_names[select_name])
        select_name = random.randint(1, len(l_names) - 1)
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
        select_name = random.randint(1, len(girl_f_names) - 1)
        mom.append(girl_f_names[select_name])
        select_name = random.randint(1, len(l_names) - 1)
        mom.append(l_names[select_name])
        Age = random.randint(25, 50)
        mom.append(Age)
        Relationship = 100
        mom.append(Relationship)
        Generosity = random.randint(1, 100)
        mom.append(Generosity)
        money = random.randint(1, 100)
        mom.append(money)
        select_name = random.randint(1, len(boy_f_names) - 1)
        dad.append(boy_f_names[select_name])
        select_name = random.randint(1, len(l_names) - 1)
        dad.append(l_names[select_name])
        Age = random.randint(25, 50)
        dad.append(Age)
        Relationship = 100
        dad.append(Relationship)
        Generosity = random.randint(1, 100)
        dad.append(Generosity)
        money = random.randint(1, 100)
        dad.append(money)
    def Relationship(gender):
        relationship = [] #[gender, First Name, Last Name, Age, Looks, Smarts, Money]
        if gender == 'Boy':
            relationship.append('Girl')
            select_name = random.randint(1, len(boy_f_names) - 1)
            relationship.append(boy_f_names[select_name])
        else:
            relationship.append('Boy')
            select_name = random.randint(1, len(boy_f_names) - 1)
            relationship.append(boy_f_names[select_name])
        select_name = random.randint(1, len(l_names) - 1)
        relationshi.append(l_names[select_name])
        if player_info[3] >= 13 and player_info[3] < 18:
            age = random.randint(13, 17)
            relationship.append(age)
            looks = random.randint(50, 100)
            relationship.append(looks)
            smarts = random.randint(1, 75)
            relationship.append(smarts)
            money = random.randint(1, 50)
            relationship.append(money)
            return relationship
        elif player_info[3] >= 18 and player_info[3] <= 30:
            age = random.randint(18, 30)
            relationship.append(age)
            looks = random.randint(50, 85)
            relationship.append(looks)
            smarts = random.randint(50, 75)
            relationship.append(smarts)
            money = random.randint(50, 75)
            relationship.append(money)
            return relationship
        elif player_info[3] >= 30 and player_info[3] <= 60:
            age = random.randint(30, 60)
            relationship.append(age)
            money = random.randint(50, 100)
            relationship.append(money)
            looks = random.randint(25, 75)
            relationship.append(looks)
            smarts = random.randint(50, 100)
            relationship.append(smarts)
            return relationship
        else:
            print('You are too old to get into a relationship')
    def Prints(Situation):
        if Situation == 'Sick':
            print('You are sick')
        if Situation == 'Child':
            print('You started elementary school')
    def Get_Action(Situation):
        global player_info
        global Suicide
        global Sickness
        global Last_P_Situation
        global P_Situation
        global money
        if Situation == 'Baby':
            print('1.) Age')
            print('2.) Go to the doctor')
            print('3.) End life')
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
        elif Situation == 'Child':
            print('1.) Age')
            print('2.) Go to the doctor')
            print('3.) End life')
            print('4.) Study harder in school')
            Action = input('Choose an action: ')
            while Action != '1' and Action != '2' and Action != '3' and Action != '4' and Action != '5':
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
            elif Action == '3':
                Suicide = True
            else:
                Effort_In_School += 1
        elif Situation == 'Teenager':
            print('1.) Age')
            print('2.) Go to the doctor')
            print('3.) End life')
            print('4.) Study harder in school')
            print('5.) Drop out of high school')
            print('6.) Love')
            print('7.) Mind and Body')
            print('8.) Ask your parents for money')
            Action = input('Choose an action: ')
            while Action != '1' and Action != '2' and Action != '3' and Action != '4' and Action != '5' and Action != '6' and Action != '7':
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
            elif Action == '3':
                Suicide = True
            elif Action == '4':
                Effort_In_School += 1
            elif Action == '5':
                print('You dropped out of high school')
                A_Situation = 'Teenager Drop'
                Effor_In_School = 0
                High_Degree = False
                player_info[6] -= 25
            elif Action == '6':
                look_again = 'yes'
                while look_again == 'yes':
                    print(Relationship(player_info[0]))
                    accept = input('Do you want to ask the out')
                    while accept != 'yes' and accpet != 'no':
                        print('Invalid input')
                        accept = input('Do you want to ask the out')
                    if accept == 'yes':
                        print('They said yes!')
                    else:
                        look_again = input('Do you want to look for another date?: ')
                        while look_again != 'yes' and accpet != 'no':
                            print('Invalid input')
                            look_again = input('Do you want to look for another date?: ')
                        
            elif Action == '7':
                print('1.) Go to the gym')
                print('2.) Go to the library')
                action = input('Choose an action: ')
                while action != '1' and action != '2' and action != '3':
                    print('Invalid input')
                    action = input('choose an action" ')
                if action == '1':
                    if money > 19:
                        print('You went to the gym')
                        player_info[5] += 3
                        player_info[7] += 1
                        money -= 20
                    else:
                        print('You do not have enough money to go to the gym')
                elif action == '2':
                    print('You went to the library')
                    player_info[6] += 3
            elif Action == '8':
                parent = random.randint(1, 2)
                if parent == 1:
                    print('Your mom gave you: ', end = '')
                    if mom[4] > 50:
                        if mom[5] <= 25:
                            print('$100')
                            money += 100
                        elif mom[5] > 25 and mom[5] <= 50:
                            print('$200')
                            money += 200
                        elif mom[5] > 50 and mom[5] <= 75:
                            print('$500')
                            money += 500
                        else:
                            print('$1,000')
                            money += 1000
                    else:
                        print('Your parents did not give you any money')
                else:
                    print('Your dad gave you: ', end = '')
                    if dad[4] > 50:
                        if dad[5] <= 25:
                            print('$100')
                            money += 100
                        elif dad[5] > 25 and mom[5] <= 50:
                            print('$200')
                            money += 200
                        elif dad[5] > 50 and mom[5] <= 75:
                            print('$500')
                            money += 500
                        else:
                            print('$1,000')
                            money += 1000
                    else:
                        print('Your parents did not give you any money')
    Suicide = False
    Sickness = False
    Effort_In_School = 0
    money = 0
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
            if player_info[3] > 6 and player_info[3] < 13:
                A_Situation = 'Child'
                P_Situation = 'Child'
            elif player_info[3] > 13 and player_info[3] < 18:
                A_Situation = 'Teenager'
                P_Situation = 'Teenager'
            Get_Action(A_Situation)
    print('You Died at the age of: ' + str(player_info[3]))
Life_Simulator()
