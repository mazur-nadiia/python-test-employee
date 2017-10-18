import unittest
import EmployeeType
from Employee import Employee

class TestEmployee(unittest.TestCase):

    def test_fulltime_positive(self):
        employee = Employee.factory(Employee, "Fred Johnson", EmployeeType.EmployeeType.FULLTIME, 1.5)
        self.assertEqual(employee.calculate_vacation(2.5), 10)
        employee.print_employee()

    def test_fulltime_negative(self):
        employee = Employee.factory(Employee, "Eddie Mercury", EmployeeType.EmployeeType.FULLTIME, -4)
        self.assertEqual(employee.calculate_vacation(-4), None)
        employee.print_employee()

    def test_fulltime_zero(self):
        employee = Employee.factory(Employee, "Capitan Morgan", EmployeeType.EmployeeType.FULLTIME, 0)
        self.assertEqual(employee.calculate_vacation(0), 0)
        employee.print_employee()

    def test_contractor(self):
        employee = Employee.factory(Employee, "Jane James", EmployeeType.EmployeeType.CONTRACTOR, 0.8)
        self.assertEqual(employee.calculate_vacation(0.8), None)
        employee.print_employee()

    def test_temporary(self):
        employee = Employee.factory(Employee, "Laura Ashley", EmployeeType.EmployeeType.TEMPORARY, 2.5)
        self.assertEqual(employee.calculate_vacation(2.5), None)
        employee.print_employee()


if __name__ == "__main__":
    unittest.main()





