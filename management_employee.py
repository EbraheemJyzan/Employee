from datetime import date
Emploee = {
                'Empl1':{
                    'id' : 4,
                    'name' : 'Ahmed',
                    'joining_date' : date(2024,12,25),
                    'depatment' : 'front_end',
                    'salary' : 20000
                } ,
                'Empl2':{
                    'id' : 3,
                    'name' : 'Salim',
                    'joining_date' : date(2007,5,21),
                    'depatment' : 'back_end',
                    'salary' : 10000
                } ,
                'Empl3':{
                    'id' : 2,
                    'name' : 'Khalid',
                    'joining_date' :date(2024,4,12),
                    'depatment' : 'front_end',
                    'salary' : 9000
                } ,
                'Empl4':{
                    'id' : 1,
                    'name' : 'Mohamed',
                    'joining_date' : date(2022,3,12),
                    'depatment' : 'back_end',
                    'salary' : 30000
                }
         }
#1
# list all employee
def voiw_all_emploee():
    print(Emploee)

#2
# list all employee by id
def viow_emploee_by_id():
    print('all emploee by id . ')
    for key , value in Emploee.items():
                print(value['id'])

#3
# delete employee
def delete_emploee():
    x = input('Enter id employee that you remove it , like this  Empl1,Empl2..etc :  ')
    Emploee.pop(x)


#4
# create employee
def creat_emploee():
    number_empl = input('enter number emploee: ')
    id = int (input('enter id : '))
    name = input('enter name : ')
    # joining_date = input('joining_date: ')
    department = input('enter department : ')
    salary = int(input('enter salary: '))
    print("enter joining date : ")
    date_year = int(input('year: '))
    date_month = int(input('month: '))
    date_day = int(input('day: '))
    Emploee[number_empl]= {
                        'id' : id ,
                        'name' : name ,
                        'joining_date' : date(date_year,date_month,date_day),
                        'depatment' : department ,
                        'salary' : salary
                    }

def updat_emploee():

    num_empl = input('number of emploee : ')
    name_value = input('name of value: ')
    new_item= input('new item: ')
    Emploee[num_empl][name_value]=new_item
    print(Emploee)

#5
# search employee
def search_emploee():
    search = input('input name of employee to searched : ')
    for key , value in Emploee.items():
        if value['name']== search:
            for obj in value:
                print(obj ,':',value[obj], ', ' , end=' ')

#6
# sorted employee
def sort_emploee():
    sorted_py = input('sorted employee py : ')
    print(dict(sorted(Emploee.items(),
                key=lambda item: (item[1][sorted_py])),reverse=True))

#7
# report employee
def report_all_emploee():
    print('id  , name , joining_date    ,  dapartment  ,  salary ')
    for i , j in Emploee.items():
            print('\n')
            for obj in j :
                print( j[obj] ,',' , end=' ' )


#8
# group total salary employee to front_end and back_end
def group_emploee():
    list_front = 0
    list_back = 0
    for key , value in Emploee.items():
        if Emploee[key]['depatment']=='front_end':
            list_front += Emploee[key]['salary']
        else:
            list_back += Emploee[key]['salary']
    print('Total salary of front_end', ': ' , list_front)
    print('Total salary of back_end', ': ' , list_back)


#9
# first joining date and last joining date employee
def joind_date():
    joind_date = []
    for i , j in Emploee.items():
        joind_date.append(Emploee[i]['joining_date'])
    joind_date.sort()
    print('first joined at : ' , joind_date[0])
    print('last joined at : ', joind_date[-1])

#10
# get low and high salary
def low_high_salary():
    salarys = []
    for key, value in Emploee.items():
        salarys.append(Emploee[key]['salary'])
    salarys.sort()
    print('low salarys is : ', salarys[0])
    print('high salarys is : ', salarys[-1])

x = 0
while x>=0 :
    print("wlecom back . ")

    chose = input('''\t\t\t\t to voiw_all_emploee press 'v_all'
                 to viow_emploee_by_id press 'v_by_id'
                 to create employee press 'c' 
                 to update employee press 'u' 
                 to delete  employee press 'd' 
                 to sort employee press 'sort' 
                 to search employee press 'sr'
                 to report_all_employee press 'repo'
                 to group total salary employee 'group_salary'
                 to low and high salary 'low_high'
                 to get fist and last joining date press 'joining' 
                   : ''')
    if chose =='v_all' :
        voiw_all_emploee()
        x += 1 ; continue
    elif chose == 'v_by_id':
        viow_emploee_by_id()
        x += 1;
        continue
    elif chose == 'c':
        creat_emploee()
        x += 1;
        continue
    elif chose == 'u':
        updat_emploee()
        x += 1;
        continue
    elif chose == 'd':
        delete_emploee()
        x += 1;
        continue
    elif chose == 'sort':
        sort_emploee()
        x += 1;
        continue
    elif chose == 'sr' :
        search_emploee()
        x += 1;
        continue
    elif chose == 'repo':
        report_all_emploee()
        x += 1;
        continue
    elif chose == 'low_high':
        low_high_salary()
        x += 1;
        continue
    elif chose == 'group_salary':
        group_emploee()
        x += 1;
        continue
    elif chose == 'joining':
        joind_date()
        x += 1;
        continue
    else:
        break