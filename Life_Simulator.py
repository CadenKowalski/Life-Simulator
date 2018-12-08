import random
Admin = False
def Life_Simulator(Bet):
    if Admin == False:
        while Bet < 5000:
            print('Invalid input')
            print('The minimum bet for this game is $5000')
            Bet = input('Bet: ')
    global Money
    global player_info
    global Suicide
    global Sickness
    global A_Situation
    global Effort_In_School
    global money
    global relationship
    global High_School_Diploma
    global College_Diploma
    global Drivers_License
    global In_College
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
        Age = 13
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
    def Relationship_Finals():
        global Look_Again
        print(relationship[1], relationship[2])
        print('Age: ' + str(relationship[3]))
        print('Looks: ' + str(relationship[4]) + '%')
        print('Smarts: ' + str(relationship[5]) + '%')
        print('Money: ' + str(relationship[6]) + '%')
        if relationship[0] == 'Boy':
            Ask_Out = input('Do you want to ask him out?: ').lower()
            Look_Again = 'no'
        else:
            Ask_Out = input('Do you want to ask her out?: ').lower()
            Look_Again = 'no'
        while Ask_Out != 'yes' and Ask_Out != 'no':
            print('Invalid Input')
            if relationship[0] == 'Boy':
                Ask_Out = input('Do you want to ask him out?: ').lower()
                Look_Again = 'no'
            else:
                Ask_Out = input('Do you want to ask her out?: ').lower()
                Look_Again = 'no'
        if Ask_Out == 'yes':
            if relationship[0] == 'Boy':
                print('He said yes!!')
            else:
                print('She said yes!!')
        else:
            Look_Again = input('Do you want to keep looking?: ').lower()
            while Look_Again != 'yes' and Look_Again != 'no':
                print('Invalid input')
                Look_Again = input('Do you want to keep looking?: ').lower()
    def Relationship():
        global relationship
        global Look_Again
        Look_Again = 'yes'
        while Look_Again == 'yes':
            relationship = [] #[gender, First Name, Last Name, Age, Looks, Smarts, Money]
            if player_info[0] == 'Boy':
                relationship.append('Girl')
                select_name = random.randint(1, len(girl_f_names) - 1)
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
                Relationship_Finals()
            elif player_info[3] >= 18 and player_info[3] <= 30:
                age = random.randint(18, 30)
                relationship.append(age)
                looks = random.randint(50, 85)
                relationship.append(looks)
                smarts = random.randint(50, 75)
                relationship.append(smarts)
                money = random.randint(50, 75)
                relationship.append(money)
                Relationship_Finals()
            elif player_info[3] >= 30 and player_info[3] <= 60:
                age = random.randint(30, 60)
                relationship.append(age)
                money = random.randint(50, 100)
                relationship.append(money)
                looks = random.randint(25, 75)
                relationship.append(looks)
                smarts = random.randint(50, 100)
                relationship.append(smarts)
                Relationship_Finals()
            else:
                print('You are too old to get into a relationship')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    def Age():
        global player_info
        global Sickness
        global A_Situation
        global Drivers_License
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
        if player_info[3] > 6 and player_info[3] <= 13:
            player_info[6] += 1
        elif player_info[3] < 18 and player_info[3] > 13 and High_School_Diploma != False:
            player_info[6] += 2
        elif player_info[3] < 23 and player_info[3] >= 18 and College_Diploma != False:
            player_info[6] += 3
        Valid_Stats()
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('Stats:')
        print()
        print('Age: ' + str(player_info[3]))
        print('Happiness: ' + str(player_info[4]) + '%')
        print('Health: ' + str(player_info[5]) + '%')
        print('Smarts: ' + str(player_info[6]) + '%')
        print('Looks: ' + str(player_info[7]) + '%')
        print('Money: $' + str(money))
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        if player_info[3] == 6:
            print('Announcement:')
            print()
            print('You started Elementary School')
            announcement = True
        if player_info[3] == 13:
            print('Announcement:')
            print()
            print('You started High School')
            announcement = True
        if player_info[3] == 16:
            if player_info[6] > 50:
                Drivers_License = True
                print('Announcement:')
                print()
                print('You revieved your Drivers License')
                announcement = True
            else:
                Drivers_Licesne = False
                print('Announcement:')
                print()
                print('You failed you drivers test. You can try again any time')
                announcement = True
        if player_info[3] == 18 and High_School_Diploma != False:
            print('Announcement:')
            print()
            print('You graduated from High School')
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
        if player_info[3] < 18:
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
        global In_College
        if A_Situation == 'Teenager':
            High_School_Diploma = False
            print('You dropped out of High School')
        elif A_Situation == 'College':
            College_Diploma = False
            In_College = False
            print('You dropped out of College')
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
    def Drivers_Test():
        global Drivers_Test
        if player_info[6] > 50:
            Drivers_Licesne = True
            print('You recieved your drivers license')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        else:
            print('You failed your driving test. You can try again any time')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    def Valid_Stats():
        global player_info
        if player_info[4] < 0:
            player_info[4] = 0
        elif player_info[4] > 100:
            player_info[4] = 100
        if player_info[5] < 0:
            player_info[5] = 0
        elif player_info[5] > 100:
            player_info[5] = 100
        if player_info[6] < 0:
            player_info[6] = 0
        elif player_info[6] > 100:
            player_info[6] = 100
        if player_info[7] < 0:
            player_info[7] = 0
        elif player_info[7] > 100:
            player_info[7] = 100
    def Go_To_College():
        global Major
        global money
        global In_College
        if High_School_Diploma == True and player_info[6] > 50:
            print('Majors:')
            print('1.) Business')
            print('2.) Law')
            print('3.) Medical')
            print('4.) Computer Science')
            Major = input('Choose a major: ')
            while Major != '1' and Major != '2' and Major != '3' and Major != '4':
                print('Invalid input')
                Major = input('Choose a major: ')
            if Major == '1':
                print('Information:')
                print('Years: 4')
                print('Cost: $50,000')
            elif Major == '2':
                print('Information:')
                print('Years: 4')
                print('Cost: $65,000')
            elif Major == '3':
                print('Information:')
                print('Years: 7')
                print('Cost: $80,000')
            elif Major == '4':
                print('Information:')
                print('Years: 4')
                print('Cost: $45,000')
            payed_for = False
            while payed_for == False:
                print('Payments:')
                print('1.) Scholarship')
                print('2.) Ask your parents to pay')
                print('3.) Student loan')
                Payment = input('How do you want to pay?: ')
                while Payment != '1' and Payment != '2' and Payment != '3':
                    print('Invalid input')
                    Payment = input('How do you want to pay?: ')
                if Payment == '1':
                    if player_info[6] > 75:
                        payed_for = True
                        In_College = True
                        print('Your scholarship was approved')
                        print('You started College')
                        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                    else:
                        print('You did not get a scholarship')
                elif Payment == '2':
                    if mom[4] > 50 or dad[4] > 50:
                        payed_for = True
                        In_College = True
                        print('Your parents agreed to pay for your College')
                        print('You started College')
                        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                    else:
                        print('Your parents would not pay for your College')
                else:
                    print('You applied for student loans')
                    if Major == '1':
                        money -= 50000
                    elif Major == '2':
                        money -= 65000
                    elif Major == '3':
                        money -= 80000
                    elif mpney == '4':
                        money -= 45000
                    payed_for = True
                    In_College = True
                    print('You started College')
                    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        else:
            print('You were not accepted into college')
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
            print('4.) Drop out of High School')
            print('5.) Love')
            print('6.) Mind and Body')
            print('7.) Ask your parents for money')
            if Drivers_License == False and player_info[3] > 16:
                print('8.) Take drivers test')
                print('9.) End life')
            else:
                print('8.) End life')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            Action = input('Choose an action: ')
            while Action != '1' and Action != '2' and Action != '3' and Action != '4' and Action != '5' and Action != '6' and Action != '7' and Action != '8' and Action != '9':
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
            elif Drivers_License == False and player_info[3] > 16:
                if Action == '8':
                    Drivers_Test()
                elif Action == '9':
                    Commit_Suicide()
            else:
                if Action == '8':
                    Commit_Suicide()
        elif Situation == 'College':
            print('Actions:')
            print()
            print('1.) Age')
            print('2.) Go to the doctor')
            print('3.) Go to College')
            print('4.) Study harder in College')
            print('5.) Drop out of College')
            print('6.) Love')
            print('7.) Mind and Body')
            print('8.) Ask your parents for money')
            if Drivers_License == False and player_info[3] > 16:
                print('9.) Take drivers test')
                print('10.) End life')
            else:
                print('9.) End life')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            Action = input('Choose an action: ')
            while Action != '1' and Action != '2' and Action != '3' and Action != '4' and Action != '5' and Action != '6' and Action != '7' and Action != '8' and Action != '9' and Action != '10':
                print('Invalid input')
                Action = input('Choose an action: ')
            if Action == '1':
                Age()
            elif Action == '2':
                Doctor()
            elif Action == '3':
                if In_College == True:
                    print('You are already in college')
                    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                else:
                    Go_To_College()
            elif Action == '4':
                if In_College == False:
                    print('You are not in College yet')
                    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                else:
                    Study()
            elif Action == '5':
                if In_College == False:
                    print('You are not in College yet')
                    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                else:
                    Drop_Out()
            elif Action == '6':
                Relationship()
            elif Action == '7':
                Mind_Body()
            elif Action == '8':
                Ask_For_Money()
            elif Drivers_License == False and player_info[3] > 16:
                if Action == '9':
                    Drivers_Test()
                elif Action == '10':
                    Commit_Suicide()
            else:
                if Action == '9':
                    Commit_Suicide()
                
    Suicide = False
    Sickness = False
    Effort_In_School = 0
    money = 0
    High_School_Diploma = True
    College_Diploma = True
    Drivers_License = False
    action = ''
    In_College = False
    while action != '1':
        print('1.) Start a new life')
        print('2.) Credits')
        action = input('Choose an action: ')
        while action != '1' and action != '2':
            print('Invalid input')
            action = input('Choose an action: ')
        if action == '1':
            New_Life()
            print('My name is: ' + player_info[1] + ' ' + player_info[2])
            P_Situation = 'Baby'
            A_Situation = 'Baby'
            Last_P_Situation = 'Baby'
        elif action == '2':
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            print('Creator: Caden Kowalski')
            print('Start Date: 12/3/18')
            print('Days Spent: 5')
            print('Actual Time Coding: 7:01:16')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
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
Life_Simulator(5000)
