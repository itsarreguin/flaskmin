"""Delete employee tests"""

import unittest
from selenium import webdriver


class DeleteEmployee(unittest.TestCase):
    
    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(25)
        driver.maximize_window()
        driver.get(url='http://127.0.0.1:5000/dashboard')
    
    def test_delete_employee(self):
        driver = self.driver
        # Change the XPath for your own delete test
        delete_employee = driver.find_element_by_xpath('/html/body/main/section/div[2]/table/tbody/tr[4]/td[7]/a')
        self.assertTrue(delete_employee.is_displayed())

        delete_employee.click()
    
    @classmethod
    def tearDown(cls) -> None:
        return cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)