print("-Student/Course Record Maintenance-")

# establish dictionaries
primaryDictionary = dict()
secondaryDictionary = dict()

# request input from user
initialInput = int(input('How many student records do you want to input? '))

#prompt requesting information from user to further program
for i in range(0, initialInput):
        fN, lN = input("Enter the complete name (First and last name) of student (Case sensitive): ").split()
        studentID = input("Enter Student ID Number: ")
        studentDOB = input('Enter date of birth (MM/DD/YYYY): ')
        primaryDictionary[fN, lN] = (studentID, studentDOB)



# define a function for sorting names based on last name from z-a
def sort():
    ls = list()
    # fetch key and value using / items() method
    for uName, details in primaryDictionary.items():
        # store both names as a tuple
        tup = (uName[0], uName[1])
        # add tuple to list
        ls.append(tup)

    # sort list
    ls = sorted(ls)
    for i in ls:
        # print names
        print(i[1], i[0])
    return


# define a function for finding the date of birth using last name
def dob(lname):
    ls = list()

    for sname, details in primaryDictionary.items():
        tup = (sname, details)
        ls.append(tup)

    for i in ls:
        if i[0][1] == lname:
            print(i[1][1])
    return


# define a function for searching student id number by using last name
def searchdetail(lname):
    ls = list()

    for sname, details in primaryDictionary.items():
        tup = (sname, details)
        ls.append(tup)

    for i in ls:
        if i[0][1] == lname:
            print(i[1][0])
    return

# define a function for asking the user for input information
def option():
    choice = int(input('Enter the operation detail: \n \
    1: Sort students using last name \n \
    2: Look up date of birth using last name \n \
    3: Search student id number using last name: \n \
    4: Maintain course records \n \
    5: Exit\n \
    Option: '))



    if choice == 1:
        # function sort call
        sort()
        # give user option to perform a different function
        print('Do you want to perform a different function? "y" or "n": ')
        inp = input()
        if inp == 'y':
            option()

        # exit function call
        exit()

    elif choice == 2:
        last = input('Enter last name of student: ')
        dob(last)
        # give user option to perform a different function
        print('Do you want to perform a different function? "y" or "n": ')
        inp = input()
        if inp == 'y':
            option()

        exit()

    elif choice == 3:
        last = input('Enter last name of student: ')
        searchdetail(last)
        # give user option to perform a different function
        print('Do you want to perform a different function? "y" or "n": ')
        inp = input()
        if inp == 'y':
            option()

    elif choice == 4:
        # request input from user
        secondInput = int(input('How many course records do you want to maintain? '))

         # add student information to the dictionary
        for i in range(0, secondInput):
            cId1, cId2 = input("Enter course ID (ex: CS 499) (Case sensitive): ").split()
            courseName = input("Enter course name: ")
            courseCredit = input('Enter course credit hours: ')
            secondaryDictionary[cId1, cId2] = (courseName, courseCredit)

option()


#sort function
def sort2():
    ls = list()
    # fetch key and value using / items() method
    for sName, details in secondaryDictionary.items():
        # store both names as a tuple
        tup = (sName[1], sName[0])
        # add tuple to list
        ls.append(tup)

    # sort list
    ls = sorted(ls)
    for i in ls:
        # print names
        print(i[1], i[0])
    return

#course ID search function
def cIdLookup(cids):
    ls = list()

    for coName, details in secondaryDictionary.items():
        tup = (coName, details)
        ls.append(tup)

    for i in ls:
        if i[0][1] == cids:
            print(i[1][0])
    return

# define a function for searching student id number by using last name
def searchdetail2(id):
    ls = list()

    for cname, details in secondaryDictionary.items():
        tup = (cname, details)
        ls.append(tup)

    for i in ls:
        if ([0],i[0]) == id:
            print(i[1][0])
    return
#Second set of course options
def options():
    choice2 = int(input('Enter the operation detail: \n \
    1: Sort courses using course ID \n \
    2: Look up course name using course ID \n \
    3: Look up course credit hours using course ID: \n \
    4: Exit\n \
    Option: '))

    if choice2 == 1:
    # function call asking to further or end program
        sort2()
        print('Want to perform some other operation??? "y" or "n": ')
        inp = input()
        if inp == 'y':
            options()

        # exit function call
        exit()

    elif choice2 == 2:
        coN = input('Enter course ID: ')
        cIdLookup(coN)

        print('Want to perform some other operation??? "y" or "n": ')
        inp = input()
        if inp == 'y':
            options()

            exit()

    elif choice2 == 3:
        id = input('Enter course ID: ')
        searchdetail2(id)

        print('Want to perform some other operation??? "y" or "n": ')
        inp = input()
        if inp == 'y':
            options()

        exit()



options()

options()












