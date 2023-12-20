import unittest
from dao.findCarsByID import findCarsByID
from dao.findCustomerByID import findCustomerByID



class MyTestCase(unittest.TestCase):
    def testExcption(self):
        self.assertEqual("Car ID not found", str(findCarsByID()))
        self.assertEqual("Customer ID not found", str(findCustomerByID()))

if __name__=='__main__':
    unittest.main()