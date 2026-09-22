

class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        
        self.author = author
        self.price = price
        self.quantity = quantity
  
  
  #call total value:


    def total_value(self):
        return self.price * self.quantity


    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Value:", self.total_value())
        

b1 = Book("math", "Kush", 50, 8)
b2 = Book("hindi", "Aditya", 60, 3)
b3 = Book("english", "Riya", 70, 5)



total = b1.total_value() + b2.total_value() + b3.total_value()

print("Total Value of All Books=", total) 
b1.display()
b2.display()
b3.display()

# second question


class Employee:
    def __init__(self, name, department, salary, performance_score):
        self.name = name
        self.department = department
        self.salary = salary
        self.performance_score = performance_score

    # Calculate 10% bonus
    def calculate_bonus(self):
        return self.salary * 10/ 100

    # Display employee details
    def display(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Performance Score:", self.performance_score)
        

e1 = Employee("Ankit", "cs", 50000, 5)
e2 = Employee("Riya", "ca", 35000, 8)
e3 = Employee("Ayushi", "gov", 65000, 6)



e1.display()
e2.display()
e3.display()


print("Employees Eligible for Bonus:",)

employees = [e1, e2, e3]

for emp in employees:
    if emp.performance_score >= 8:
        bonus = emp.calculate_bonus()

        print("Name:", emp.name)
        print("Bonus Received:", bonus)





#third question :

class ElectricBill:
    def __init__(self, units, rate_per_unit):
        self.units = units
        self.rate_per_unit = rate_per_unit


    def calculate_bill(self):
        return self.units * self.rate_per_unit


    def final_bill(self):
        bill = self.calculate_bill()

        if bill >= 2000:
            surcharge = bill * 5 / 100
            return bill + surcharge
        else:
            return bill


c1 = ElectricBill(100, 20)
c2 = ElectricBill(150, 15)
c3 = ElectricBill(200, 12)


customers = [c1, c2, c3]

total = 0

for customer in customers:
    bill = customer.final_bill()

    print("Units:", customer.units)
    print("Rate per Unit:", customer.rate_per_unit)
    print("Final Bill:", bill)


    total = total + bill


average = total / len(customers)

print("Average Electricity Bill:", average)
