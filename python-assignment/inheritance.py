
class Employee:
    def __init__(self, id, name, place, address, phone):
        self.id = id
        self.name = name
        self.place = place
        self.address = address
        self.phone = phone

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Place:", self.place)
        print("Address:", self.address)
        print("Phone:", self.phone)
class PermanentEmployee(Employee):
    def __init__(self, id, name, place, address, phone, joining_date, designation, salary):
        super().__init__(id, name, place, address, phone)
        self.joining_date = joining_date
        self.designation = designation
        self.salary = salary
    def display(self):
        super().display()
        print("Joining Date:", self.joining_date)
        print("Designation:", self.designation)
        print("Salary:", self.salary)
class ContractEmployee(Employee):
    def __init__(self, id, name, place, address, phone, start_date, contract_end_date, hourly_rate):
        super().__init__(id, name, place, address, phone)
        self.start_date = start_date
        self.contract_end_date = contract_end_date
        self.hourly_rate = hourly_rate

    def display(self):
        super().display()
        print("Start Date:", self.start_date)
        print("End Date:", self.contract_end_date)
        print("Hourly Rate:", self.hourly_rate)
print(" Permanent Employee")
p1 = PermanentEmployee(1, "Anu", "Kochi", "Pulikunn House", "9876543210", "01-01-2024", "Manager", 50000)
p1.display()

print("\n-Contract Employee ")
c1 = ContractEmployee(2, "Rahul", "Kannur", "Thekkan House", "9123456780", "01-03-2024", "01-09-2024", 200)
c1.display()