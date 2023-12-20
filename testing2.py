import unittest
from dao.createLease import createLease
from dao.listLeaseHistory import listLeaseHistory

class MyTestCase(unittest.TestCase):

    def test_lease_creation_and_history(self):
        # Create a lease
        createdLease = createLease()
        leaseHistory = listLeaseHistory()
        # Check if the created lease is in the lease history
        if createdLease is not None:
            for i in leaseHistory
                lease_found = any(createdLease[0][0] == i[0])
            self.assertTrue(lease_found)
            
if __name__ == '__main__':
    unittest.main()
