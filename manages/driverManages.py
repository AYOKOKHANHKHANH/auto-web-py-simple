from selenium import webdriver


# def get_driver(browser):
#     driver = chrome_driver_init()
#     return driver

def chrome_driver_init():
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(30)
    driver.maximize_window()
    print('Open Chrome browser')
    
    return driver