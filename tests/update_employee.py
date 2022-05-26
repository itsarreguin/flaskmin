"""Update employee information"""

import unittest
from selenium import webdriver


class UpdateEmployeeData(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(25)
        driver.maximize_window()
        driver.get(url='http://127.0.0.1:5000/dashboard/')

    def test_update_employee_name(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/main/section/div[2]/table/tbody/tr[4]/td[2]/a').click()
        
        first_name = driver.find_element_by_name('first_name')
        update_btn = driver.find_element_by_name('update')
        
        self.assertTrue(first_name.is_enabled() and update_btn.is_enabled())
        
        first_name.clear()
        first_name.send_keys('Sheldon Lee')

        update_btn.click()

    def test_update_employee_username(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/main/section/div[2]/table/tbody/tr[4]/td[2]/a').click()
        
        username = driver.find_element_by_name('username')
        update_btn = driver.find_element_by_name('update')
        
        self.assertTrue(username.is_enabled() and update_btn.is_enabled())
        
        username.clear()
        username.send_keys('shelylee')

        update_btn.click()
    
    @classmethod
    def tearDown(cls) -> None:
        return cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)