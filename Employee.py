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
        vacation = self.calculate_vacation()
        if (vacation != None):
            print("Name: %s %s, Duration: %s years, Vacation Accrued: %s days" % (self.name, self.type._value_, self.longevity, vacation) )
        else:
            print("Name: %s %s, Duration: %s years, Vacation Accrued: None" % (self.name, self.type._value_, self.longevity))
class Fulltime(Employee):
    def calculate_vacation(self):
        if (self.longevity >=0):
            return int(self.longevity) * 5
        else:
            return None

class Tempopary(Employee):
    def calculate_vacation(self):
        return None

class Contractor(Employee):
    def calculate_vacation(self):
        return None



