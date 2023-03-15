import time
import pytest
import unittest
from manages.driverManages import chrome_driver_init
from pages.landingPage import BiwocoPage

@pytest.mark.usefixtures('drive_class')
class BiTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = chrome_driver_init()
        self.driver.get('https://biwoco.com')
        
    def tearDown(self):
        self.driver.close()
        
    def test_click_services(self):
        biwoco = BiwocoPage(self.driver)
        biwoco.click_services()
        assert (self.driver.current_url,'https://www.biwoco.com/service')