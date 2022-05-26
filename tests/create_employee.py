"""Create new employee after log in"""

import unittest
from selenium import webdriver


class CreateEmployee(unittest.TestCase):
    
    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(25)
        driver.maximize_window()
        driver.get(url='http://127.0.0.1:5000/dashboard/')
    
    def test_create_new_employee(self):
        driver = self.driver
        driver.find_element_by_link_text('Add employee').click()
        
        first_name = driver.find_element_by_id('first_name')
        last_name = driver.find_element_by_id('last_name')
        email = driver.find_element_by_id('email')
        username = driver.find_element_by_id('username')
        create_button = driver.find_element_by_id('create')
        
        self.assertTrue(
            first_name.is_enabled()
            and last_name.is_enabled()
            and email.is_enabled()
            and username.is_enabled()
            and create_button.is_enabled()
        )
        
        first_name.send_keys('Sheldon')
        driver.implicitly_wait(10)
        
        last_name.send_keys('Cooper')
        driver.implicitly_wait(10)
        
        email.send_keys('sheldon@example.com')
        driver.implicitly_wait(10)
        
        username.send_keys('shelly')
        driver.implicitly_wait(10)
        
        create_button.click()
    
    @classmethod
    def tearDown(cls) -> None:
        return cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)