from locators.landingPageLocator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class  BiwocoPage:
    def __init__(self, driver):
        self.driver = driver
        
    def check_exists_by_xpath(self,xpath):
        try:
            self.driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True
        
    def click_services(self):
        print('Click Services button')
        btn_services = Wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, get_btn_services_xpath())))
        btn_services.click()