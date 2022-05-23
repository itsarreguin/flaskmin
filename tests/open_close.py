"""Simple test to visit application"""

import unittest
from selenium import webdriver


class OpenClose(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(20)
        driver.maximize_window()

    def test_visit_flaskmin_local(self):
        driver = self.driver
        driver.get(url='http://127.0.0.1:5000')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)