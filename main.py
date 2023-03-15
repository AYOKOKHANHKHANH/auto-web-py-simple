import unittest
from tests.test import BiTest

if __name__ == '__main__':
    
    landing_page = unittest.TestLoader().loadTestsFromTestCase(BiTest)
    
    test_suite = unittest.TestSuite([landing_page])
    
    unittest.TextTestRunner().run(test_suite)