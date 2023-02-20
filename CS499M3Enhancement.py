print("--Travel Helper--")
#program is used to help user organize information on potential vacations
#the point of this is to give the user data visualization to help decide where they really want to vacation most

# establish dictionaries that will be utilized
vacationData = {}
vacationData2 = {}
vacationData3 = {}

# request input from user
userInput = int(input('How many places are you interested in visiting for a Vacation?! (You may include places you have already visited)'))

# adds user input as data that will be used to sort
for i in range(0,userInput):
    locations = input(" Please enter the City and Country of location: ")
    type = input(" Please enter the Type of vacation? (Tourist or Cruise): ")
    iLevel = input("From a scale of 1-10, what is your interest level in this location? (Enter 1-10):")
    recur = input("Have you vacationed here previously?")
    vacationData[locations] = iLevel
    vacationData2[locations] = type
    vacationData3[locations] = recur

# define a function for asking how user wants to organize sorting function
def option():
    choice = int(input('Enter the sort function you would like to use: \n \
    1: Sort vacation by interest level \n \
    2: Sort vacation by vacation type \n \
    3: Sort vacation by whether or not this is a recurring vacation : \n \
    4: Exit\n \
    Option: '))

    if choice == 1:
        # sort vacation options by interest level of locations
        sort_vacationData= sorted(vacationData.items(), reverse=True)
        for i in sort_vacationData:
            print(i[1],i[0])
        # gives user option to sort using a different option
        print('Would you like to sort with a different category?? "y" or "n": ')
        inp = input()
        if inp == 'y':
            option()

        # exit call
        exit()

    elif choice == 2:
        # sort vacation options by vacation type ( tourist type attractions or cruise )
        sort_vacationData2 = sorted(vacationData2.items(), key=lambda x: x[1], reverse=True)
        for i in sort_vacationData2:
            print(i[1], i[0])
        # gives user option to sort using a different option
        print('Would you like to sort with a different category? "y" or "n": ')
        inp = input()
        if inp == 'y':
            option()

        # exit function call
        exit()

    elif choice == 3:
        # sort vacation options by whether or not location has been visited before
        sort_vacationData3 = sorted(vacationData3.items(), key=lambda x: x[1], reverse=True)
        for i in sort_vacationData3:
            print(i[1], i[0])
        # gives user option to sort using a different option
        print('Would you like to sort with a different category? "y" or "n": ')
        inp = input()
        if inp == 'y':
            option()

        # exit function call
        exit()
    #This is for if the user decides not to sort using a different option
    else:
        print('Vacation helper has closed')
        exit()


option()