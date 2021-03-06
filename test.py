import unittest
import EmployeeType
from Employee import Employee
from EmployeeType import EmployeeType


class TestEmployee(unittest.TestCase):

    def test_fulltime_positive(self):
        employee = Employee.factory(Employee, "Fred Johnson", EmployeeType.FULLTIME, 2.5)
        self.assertEqual(employee.calculate_vacation(), 10)
        employee.print_employee()

    def test_fulltime_negative(self):
        employee = Employee.factory(Employee, "Eddie Mercury", EmployeeType.FULLTIME, -4)
        self.assertEqual(employee.calculate_vacation(), None)
        employee.print_employee()

    def test_fulltime_zero(self):
        employee = Employee.factory(Employee, "Capitan Morgan", EmployeeType.FULLTIME, 0)
        self.assertEqual(employee.calculate_vacation(), 0)
        employee.print_employee()

    def test_contractor(self):
        employee = Employee.factory(Employee, "Jane James", EmployeeType.CONTRACTOR, 0.8)
        self.assertEqual(employee.calculate_vacation(), None)
        employee.print_employee()

    def test_temporary(self):
        employee = Employee.factory(Employee, "Laura Ashley", EmployeeType.TEMPORARY, 3.5)
        self.assertEqual(employee.calculate_vacation(), None)
        employee.print_employee()


if __name__ == "__main__":
    unittest.main()





