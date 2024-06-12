
class Employee:
    
    def __init__(self, emp_id, name, department, position):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.position = position


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, department, position):
        employee = Employee(emp_id, name, department, position)
        self.employees.append(employee)
        print("Employee added successfully!")

    def display(self):
        if len(self.employees) == 0:
            print("No employees found.")
        else:
            for employee in self.employees:
                print("Employee ID:", employee.emp_id)
                print("Name:", employee.name)
                print("Department:", employee.department)
                print("Position:", employee.position)
                print("-----------------------")

    def search_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                print("Employee found!")
                print("Employee ID:", employee.emp_id)
                print("Name:", employee.name)
                print("Department:", employee.department)
                print("Position:", employee.position)
                return
        print("Employee not found.")

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print("Employee removed successfully!")
                return
        print("Employee not found.")


manager = EmployeeManagementSystem()


def main():
    # print('*****************MAIN MENU***********************')
    # print('1. for Managers')
    # print('2. for Employees')
    # choice = input('Enter your choice: ')

    # if choice == '1':
        print('****************Managers******************')
        print('1. Add Employees')
        print('2. Display Employees')
        print('3. Search Employees')
        print('4. Delete Employees')

        option = input('Enter your option: ')
        if option == '1':
            emp_id = input('Enter employee id: ')
            name = input('Enter employee name: ')
            department = input('Enter department: ')
            position = input('Enter position: ')
            manager.add_employee(emp_id, name, department, position)
         
            main()

        elif option == '2':
            manager.display()
            main()
        elif option == '3':
            emp_id = input('Enter employee id: ')
            manager.search_employee(emp_id)
            main()
        elif option == '4':
            emp_id = input('Enter employee id: ')
            manager.remove_employee(emp_id)
            main()
        else:
            print('Incorrect option')


    # elif choice == '2':
    #     print('*****************Employees*********************')
    #     print('1. Display Employee')
    #     emp_choice = input('Enter your choice: ')
    #     if emp_choice == '1':
    #         manager.display()
    #     else:
    #         print("Incorrect option")

    # else:
    #     print('Incorrect choice')

    # main()


main()