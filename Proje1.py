import pandas as pd


def inputControl(SchoolNum, Resultofexams): #Control Function
    
    while True:
        try: 
            SchoolNum = int(SchoolNum)
            Resultofexams = int(Resultofexams)

            assert SchoolNum >= 0 # Test if it is negative
            assert Resultofexams >= 0 # Test if it is negative
            assert Resultofexams <= 100 # Test if it is greater than 100
            break
        except AssertionError:
            if Resultofexams > 100 or Resultofexams < 0:
              print("The Resultofexams cannot be negative or greater than 100. Please re-enter!")
              Resultofexams = input('Exam Resultofexams: ')
            elif SchoolNum < 0:
              print("The school SchoolNum you entered is negative. Please re-enter!")
              SchoolNum = input('School SchoolNumber: ')
            else:
              Resultofexams = input('Exam Resultofexams: ')
              SchoolNum = input('School SchoolNumber: ')
            
        except ValueError:
            print('School SchoolNum and exam Resultofexams can only be Schoolnumbers! Please re-enter!')
            SchoolNum = input('School SchoolNumber: ')
            Resultofexams = input('Exam Resultofexams: ')
    return (SchoolNum, Resultofexams)
    
name = input('Name: ')
lastname = input('Surname: ')
SchoolNum = input('School Number : ')
Resultofexams = input("Result of exam : ")

SchoolNum, Resultofexams = inputControl(SchoolNum, Resultofexams)

if int(Resultofexams) >= 90 or int(Resultofexams) >= 100:
    status = 'Passed'
    letter_grade = 'A'
elif int(Resultofexams) >= 80 or int(Resultofexams) >= 79:
    status = 'Passed'
    letter_grade = 'B'
elif int(Resultofexams) >= 70 or int(Resultofexams) >= 59:
    status = 'Passed'
    letter_grade = 'C'
elif int(Resultofexams) >= 60 or int(Resultofexams) >= 49:
    status = 'Passed'
    letter_grade = 'D'
elif int(Resultofexams) >= 0 or int(Resultofexams) >= 39:
    status = 'Failed'
    letter_grade = 'F'
    Resultofexams
else:
    status = 'Invalid value.'
    letter_grade = ''
    
print(status, letter_grade, Resultofexams)

student_dict = {'Name': [name],
                'Surname': [lastname],
                'School SchoolNumber': [SchoolNum],
                'Exam Resultofexams': [Resultofexams],
                'Letter Grade': [letter_grade],
                'Status': [status],
                'Lesson': 'Physics'
               }

student_list = pd.DataFrame(student_dict)
student_list.to_csv("studentList.csv", mode='a', header=False, index=False)
student_list = pd.read_csv("studentList.csv")
print(student_list)
