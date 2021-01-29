
#example1 
"""
class Cylinder:
  def __init__(self,radius,height):
    self.radius = radius
    self.height = height
  
  def set_radius(self,value):
    self.radius = value
  def get_radius(self):
    return self.radius
  
  def set_height(self,value):
    self.hegiht = value

  def get_height(self):
    return self.height
  
  def calc_area(self):
    base_area = (3.14)*(self.radius)**2
    surface_area = 2*(3.14)*(self.radius)*(self.height)
    total_area = 2*base_area + surface_area
    return f"Area of cylinder is :{total_area}"

  def calc_volume(self):
    base_area = (3.14)*(self.radius)**2
    volume = base_area*self.height
    return f"Volume of cylinder is : {volume}"


object1 = Cylinder(3,5)
print(object1.calc_area())
print(object1.calc_volume())
"""
#example2
"""
class Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
  
  def set_name(self,name):
    self.name = name
  def get_name(self):
    return self.name

  def set_salary(self,salary):
    self.salary = salary
  def get_salary(self):
    return self.salary
  
  def display(self):
    print(f"Name of employee :{self.name}\n"+
      f"Salary of employee : {self.salary}")

class Company:
  def __init__(self):
    self.employee_list = []
  
  def add_employee(self, new_employee):
    if isinstance(new_employee, Employee):
      self.employee_list.append(new_employee)
    else:
      print("There is no employee such that !!!")

  def avg_salary(self):
    all_salary = 0
    employee_number = len(self.employee_list)
    for employee in self.employee_list:
      all_salary += employee.salary
    avg_salary = all_salary/employee_number
    return f"Average salary :{avg_salary}"
  
  def display(self):
    print("***************************************")
    for employee in self.employee_list:
      employee.display()
      print("***************************************")

employee1 = Employee("ahmet",9000)
employee2 = Employee("cihat",6000)
employee3 = Employee("ahsen",5000)
employee4 = Employee("eylul",12000)
cd_project = Company()
cd_project.add_employee(employee1)
cd_project.add_employee(employee2)
cd_project.add_employee(employee3)
cd_project.add_employee(employee4)

cd_project.display()
print(cd_project.avg_salary())
"""

#example3
class DNA:
  def __init__(self,DNA):
    self.DNA = DNA