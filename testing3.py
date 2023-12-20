import unittest
from dao.listLeaseHistory import listLeaseHistory

class MyTestCase(unittest.TestCase):

    def testCase3(self):
        # Retrieve lease history
        leaseHistory = listLeaseHistory()

        if leaseHistory is not None:
            leaseR=any(leaseHistory[0]==createdLease)
            self.assertEqual(leaseR)

if __name__ == '__main__':
    unittest.main()
