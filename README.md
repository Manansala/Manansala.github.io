# Joshua Manansala ePortfolio


    
#With the original artifact being a template/diagram for how this program was wanted to be run, I created the code to include all of the neccessary features. I employed strategies for building collaborative environments by notaing the purpose of each section of code. This allows other team members to pick up from any of the coding and edit as they see fit to better the project. The design and notation portrays professional quality written and visual commnication which helps promote team work. This code design is an example of complete and efficient computing solutions for the task at hand. This code promotes best practices and uses proper algorithmic priniciples. The techniques within this project displays efficient techniques, skills and tools. When running this code, all of the intended uses of the program execute completely and without error. A security mindset is displayd as this program only functions with the proper student information. Without proper information, this program ceases to be effective which helps keep private information safe.

      
##("-Student/Course Record Maintenance-")

   #establish dictionaries
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



  #define a function for sorting names based on last name from z-a
        def sort():
        ls = list()
        # fetch key and value using / items() method
        for uName, details in primaryDictionary.items():
             # store both names as a tuple
            tup = (uName[0], uName[1])
            # add tuple to list
            ls.append(tup)

   #sort list
      ls = sorted(ls)
      for i in ls:
          # print names
          print(i[1], i[0])
      return


  #define a function for finding the date of birth using last name
  def dob(lname):
      ls = list()

      for sname, details in primaryDictionary.items():
          tup = (sname, details)
          ls.append(tup)

      for i in ls:
          if i[0][1] == lname:
              print(i[1][1])
      return


  #define a function for searching student id number by using last name
    def searchdetail(lname):
      ls = list()

      for sname, details in primaryDictionary.items():
          tup = (sname, details)
          ls.append(tup)

      for i in ls:
          if i[0][1] == lname:
              print(i[1][0])
      return

  #define a function for asking the user for input information
    def option():
      choice = int(input('Enter the operation detail: \n \
      1: Sort students using last name \n \
      2: Look up date of birth using last name \n \
      3: Search student id number using last name: \n \
      4: Maintain course records \n \
      5: Exit\n \
      Option: '))



      if choice == 1:
          #function sort call
          sort()
          # give user option to perform a different function
          print('Do you want to perform a different function? "y" or "n": ')
          inp = input()
          if inp == 'y':
              option()

          #exit function call
          exit()

      elif choice == 2:
          last = input('Enter last name of student: ')
          dob(last)
          #give user option to perform a different function
          print('Do you want to perform a different function? "y" or "n": ')
          inp = input()
          if inp == 'y':
              option()

          exit()

      elif choice == 3:
          last = input('Enter last name of student: ')
          searchdetail(last)
          #give user option to perform a different function
          print('Do you want to perform a different function? "y" or "n": ')
          inp = input()
          if inp == 'y':
              option()

      elif choice == 4:
          #request input from user
          secondInput = int(input('How many course records do you want to maintain? '))

           #add student information to the dictionary
          for i in range(0, secondInput):
              cId1, cId2 = input("Enter course ID (ex: CS 499) (Case sensitive): ").split()
              courseName = input("Enter course name: ")
              courseCredit = input('Enter course credit hours: ')
              secondaryDictionary[cId1, cId2] = (courseName, courseCredit)

  option()


  #sort function
    def sort2():
      ls = list()
      #fetch key and value using / items() method
      for sName, details in secondaryDictionary.items():
          #store both names as a tuple
          tup = (sName[1], sName[0])
          #add tuple to list
          ls.append(tup)

   #sort list
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

  #define a function for searching student id number by using last name
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
      #function call asking to further or end program
          sort2()
          print('Want to perform some other operation??? "y" or "n": ')
          inp = input()
          if inp == 'y':
              options()

          #exit function call
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
      
      
#print("--Travel Helper--")
#program is used to help user organize information on potential vacations
#the point of this is to give the user data visualization to help decide where they really want to vacation most

#establish dictionaries that will be utilized
vacationData = {}
vacationData2 = {}
vacationData3 = {}

#request input from user
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
