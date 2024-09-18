from datetime import date
class Employee:
        L = []
        def __init__(self, emp_id, name, joining_date,salary):
            self.emp_id = emp_id
            self.name = name
            self.joining_date = joining_date
            self.salary = salary
        # create employee
        @classmethod
        def create(cls,dect):
            id_ = dect['id']
            name_ = dect['name']
            joining_date_ = dect['joining_date']
            salary_ = dect['salary']
            return cls(id_,name_,joining_date_,salary_)

        def __str__(self):
            return f'{self.name} : {self.emp_id} : {self.joining_date} : {self.salary}'

        def save(self):
            pass
        # update employee
        @classmethod
        def update(cls,emp_ids,data):
            for i in range(len(Employee.L)):
                     if cls.L[i].emp_id == emp_ids:
                        cls.L[i].name = data['name']
                        cls.L[i].joining_date = data['joining_date']
                        cls.L[i].salary = data['salary']

        @classmethod
        def sort(cls,sort_by):
            if sort_by == 'name' :
                Employee.L.sort(key=lambda x:x.name,reverse=False)
                for n in range(len(Employee.L)):
                    print(cls.L[n].emp_id ,",",cls.L[n].name,",",cls.L[n].joining_date)
            elif sort_by == 'emp_id' :
                Employee.L.sort(key=lambda x:x.emp_id,reverse=False)
                for n in range(len(Employee.L)):
                    print(cls.L[n].emp_id ,",",cls.L[n].name,",",cls.L[n].joining_date)

            elif sort_by == 'joining_date' :
                Employee.L.sort(key=lambda x:x.joining_date,reverse=False)
                for n in range(len(Employee.L)):
                    print(cls.L[n].emp_id ,",",cls.L[n].name,",",cls.L[n].joining_date)
            elif sort_by == 'salary' :
                Employee.list_emp.sort(key=lambda x:x.salary,reverse=False)
                for n in range(len(Employee.L)):
                    print(cls.L[n].emp_id ,",",cls.L[n].name,",",cls.L[n].joining_date,",",cls.L[n].salary)
        @classmethod
        def search(cls, search_by, value):
            if search_by == 'emp_id':
                for i in range(len(Employee.L)):
                    if cls.L[i].emp_id == value:
                        print("Employee is find . ")
                        print(cls.L[i].emp_id ,",",cls.L[i].name,",",cls.L[i].joining_date,",",cls.L[i].salary)
                    elif value not in cls.L[i].emp_id:
                        print('employee not fond !!! ')
                        break
                    else:
                        pass
            elif search_by == 'name':
                for i in range(len(Employee.L)):
                    if cls.L[i].name == value:
                        print("Employee is find . ")
                        print(cls.L[i].emp_id ,",",cls.L[i].name,",",cls.L[i].joining_date,",",cls.L[i].salary)
                    elif value not in cls.L[i].name:
                        print('employee not fond !!! ')
                        break
            else:
                print('field not fond  !!!!!!!!!!!!!!!! ')

        @classmethod
        def delete(cls,emp_ids):
            for i in range(len(Employee.L)):
                     if cls.L[i].emp_id == emp_ids:
                         del cls.L[i]

        # view employee
        @classmethod
        def display(cls):
            for i in range(len(cls.L)):
                if i == 0:
                    print("=============================================================")
                    print("=  emp_id   |  name     |     joining_date      |  salary   = ")
                print("=\t", cls.L[i].emp_id, "\t\t|  ", cls.L[i].name, "\t|\t\t", cls.L[i].joining_date,
                      "\t|\t", cls.L[i].salary, "   =")
                print("-------------------------------------------------------------")

# set information pre create employee
def pre_creat_emp():
    emp_id = input("inter id : ")
    name = input("inter name : ")
    print('enter joining date : ')
    year = int(input('year: '))
    month = int(input('month: '))
    day = int(input('day: '))
    salary = input("inter salary : ")

    info_imp = {
        "id": emp_id,
        "name": name,
        "joining_date": date(year,month,day),
        "salary": salary,
        }
    Employee.L.append(Employee.create(info_imp))

# set information pre create employee
def pre_updat_emp():
    name = input("inter name : ")
    print('enter joining date : ')
    year = int(input('year: '))
    month = int(input('month: '))
    day = int(input('day: '))
    salary = input("inter salary : ")

    info_updat_imployee = {
        "name": name,
        "joining_date": date(year,month,day),
        "salary": salary,
        }
    return info_updat_imployee

x = 0
while x>=len(Employee.L) :
    print("wlecom back . ")

    chose = input('''\t\t\t\t to create employee press 'c' 
                 to update employee press 'u' 
                 to delete  employee press 'd' 
                 to display  employee press 'disp'
                 to sort employee press 'sort' 
                 to search employee press 'sr' 
                   : ''')
    if chose =='c' :
        pre_creat_emp()
        x += 1 ; continue

    elif chose == 'u':
        update_employee = input('enter emp_id to update employee information : ')
        Employee.update(update_employee,pre_updat_emp())
        for i in range(len(Employee.L)):
            print(Employee.L[i].emp_id,", ",Employee.L[i].name,", ",Employee.L[i].joining_date,',' , Employee.L[i].salary)
            print("========================================")

    elif chose == 'd':
        employee_id = input('enter employee emp_id to delete it : ')
        Employee.delete(employee_id)

    elif chose == 'disp':
        Employee.display()

    elif chose == 'sort':
        sort_by = input("you whant sort employee by : 'emp_id , name , joining_date , salary' enter filed : ")
        Employee.sort(sort_by)

    elif chose == 'sr' :
        search_by = input('search by emp_id or name , enter value : ')
        if search_by == 'emp_id':
            value = input('enter emp_id: ')
        else:
            value = input('enter name : ')
        Employee.search(search_by, value)

    else:
        break
print(Employee.list_emp[0].name)
