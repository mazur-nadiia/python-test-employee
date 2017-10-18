import EmployeeType


class Employee(object):
    def factory(self, name, type, longevity):
        self.name = name
        self.longevity = longevity
        self.type = type

        if type == EmployeeType.EmployeeType.FULLTIME:
            return Fulltime()
        if type == EmployeeType.EmployeeType.CONTRACTOR:
            return Contractor()
        if type == EmployeeType.EmployeeType.TEMPORARY:
            return Tempopary()
        assert 0, "Creation failed for : " + type

    factory = staticmethod(factory)

    def print_employee(self):
        vacation = self.calculate_vacation(self.longevity)
        print("Name: %s %s, Duration: %s years, Vacation Accrued: %s days" % (self.name, self.type._value_, self.longevity, vacation) )

class Fulltime(Employee):
    def calculate_vacation(self, longevity):
        return int(longevity) * 5


class Tempopary(Employee):
    def calculate_vacation(self, longevity):
        return None

class Contractor(Employee):
    def calculate_vacation(self, longevity):
        return None


obj = Employee.factory(Employee, "Fred Johnson", EmployeeType.EmployeeType.FULLTIME, 1.5)
obj.print_employee()

obj2 = Employee.factory(Employee, "Jane James", EmployeeType.EmployeeType.CONTRACTOR, 0.8)
obj.print_employee()