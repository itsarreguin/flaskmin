"""Delete employee after create"""

import unittest
from selenium import webdriver


class DeleteEmployee(unittest.TestCase):
    
    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(25)
        driver.maximize_window()
        driver.get(url='http://127.0.0.1:5000')
    
    @classmethod
    def tearDown(cls) -> None:
        return cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)