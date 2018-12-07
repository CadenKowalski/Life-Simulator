import random
def Life_Simulator():
    global Money
    global player_info
    global Suicide
    global Sickness
    global A_Situation
    global Effort_In_School
    global money
    global relationship
    print('Project Info: Made by Caden Kowalski, Project Start Date: 12/3/18, Days spent: 4, Actual time for completion: 3:09:21')
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
        global mom
        global dad
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
    def Relationship():
        global relationship
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
        relationship.append(l_names[select_name])
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
    def Age():
        global player_info
        global Sickness
        global A_Situation
        announcement = False
        player_info[3] += 1
        if player_info[3] > 5:
            A_Situation = 'Child'
        if player_info[3] > 12:
            A_Situation = 'Teenager'
        if player_info[3] > 17:
            A_Situation = 'College'
        if Sickness == True:
            player_info[5] -= 2
        Sick = random.randint(1,10)
        if Sick == 4:
            Sickness = True
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('Stats:')
        print()
        print('Age: ' + str(player_info[3]))
        print('Happiness: ' + str(player_info[4]) + '%')
        print('Health: ' + str(player_info[5]) + '%')
        print('Smarts: ' + str(player_info[6]) + '%')
        print('Looks: ' + str(player_info[7]) + '%')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        if player_info[3] == 6:
            print('Announcement:')
            print()
            print('You started elementary school')
            announcement = True
        if Sickness == True:
            if announcement == True:
                print('You are sick')
            else:
                print('Announcement:')
                print()
                print('You are sick')
            announcement = True
        if announcement == True:
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    def Doctor():
        global Sickness
        global money
        if player_info[3] < 17:
            if Sickness == True:
                print('You have been cured')
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                Sickness = False
            else:
                print('You are not sick')
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        else:
            if Sickness == True:
                if money >= 100:
                    print('You have been cured')
                    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                    Sickness = False
                    money -= 100
                elif money < 100:
                    print('You do not have enough money to go to the doctor')
                    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            else:
                print('You are not sick')
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    def Commit_Suicide():
        global Suicide
        Suicide = True
    def Study():
        global Effort_In_School
        Effort_In_School += 1
        print('You studied in school')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    def Drop_Out():
        global High_School_Diploma
        global College_Diploma
        if A_Situation == 'Teenager':
            High_School_Diploma = False
            print('You dropped out of High School')
        elif A_Situation == 'College':
            College_Diploma = False
            print('You dropped put of College')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    def Mind_Body():
        global player_info
        global money
        print('1.) Go to the gym')
        print('2.) Go to the library')
        action = input('Choose an action: ')
        while action != '1' and action != '2' and action != '3':
            print('Invalid input')
            action = input('choose an action" ')
        if action == '1':
            if money > 19:
                print('You went to the gym')
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                player_info[5] += 3
                player_info[7] += 1
                money -= 20
            else:
                print('You do not have enough money to go to the gym')
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        elif action == '2':
            print('You went to the library')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            player_info[6] += 3
    def Ask_For_Money():
        global money
        if mom[4] > 50 or dad[4] > 50:
            print('Your parents gave you: ', end = '')
            if mom[5] <= 25 or dad[5] <= 25:
                print('$100')
                money += 100
            elif mom[5] <= 50 or dad[5] <= 50:
                print('$200')
                money += 200
            elif mom[5] <= 75 or dad[5] <= 75:
                print('$500')
                money += 500
            else:
                print('$1,000')
                money += 1000
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        else:
            print('Your parents did not give you any money')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    def Get_Action(Situation):
        if Situation == 'Baby':
            print('Actions:')
            print()
            print('1.) Age')
            print('2.) Go to the doctor')
            print('3.) End life')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            Action = input('Choose an action: ')
            while Action != '1' and Action != '2' and Action != '3':
                print('Invalid input')
                Action = input('Choose an action: ')
            if Action == '1':
                Age()
            elif Action == '2':
                Doctor()
            else:
                Commit_Suicide()
        elif Situation == 'Child':
            print('Actions:')
            print()
            print('1.) Age')
            print('2.) Go to the doctor')
            print('3.) Study harder in school')
            print('4.) End life')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            Action = input('Choose an action: ')
            while Action != '1' and Action != '2' and Action != '3' and Action != '4' and Action != '5':
                print('Invalid input')
                Action = input('Choose an action: ')
            if Action == '1':
                Age()
            elif Action == '2':
                Doctor()
            elif Action == '3':
                Study()
            else:
                Commit_Suicide()
        elif Situation == 'Teenager':
            print('Actions:')
            print()
            print('1.) Age')
            print('2.) Go to the doctor')
            print('3.) Study harder in school')
            print('4.) Drop out of high school')
            print('5.) Love') # Need to fix
            print('6.) Mind and Body')
            print('7.) Ask your parents for money')
            print('8.) End life')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            Action = input('Choose an action: ')
            while Action != '1' and Action != '2' and Action != '3' and Action != '4' and Action != '5' and Action != '6' and Action != '7' and Action != '8':
                print('Invalid input')
                Action = input('Choose an action: ')
            if Action == '1':
                Age()
            elif Action == '2':
                Doctor()
            elif Action == '3':
                Study()
            elif Action == '4':
                Drop_Out()
            elif Action == '5':
                Relationship()
            elif Action == '6':
                Mind_Body()
            elif Action == '7':
                Ask_For_Money()
            elif Action == '8':
                Commit_Suicide()
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
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print('Stats:')
    print()
    print('Age: ' + str(player_info[3]))
    print('Happiness: ' + str(player_info[4]) + '%')
    print('Health: ' + str(player_info[5]) + '%')
    print('Smarts: ' + str(player_info[6]) + '%')
    print('Looks: ' + str(player_info[7]) + '%')
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    while Suicide != True:
        Get_Action(A_Situation)
    print('You Died at the age of: ' + str(player_info[3]))
Life_Simulator()
