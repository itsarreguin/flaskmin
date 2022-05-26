"""Log in a register user in the app"""

import unittest
from selenium import webdriver


class LoginUser(unittest.TestCase):
    
    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.get(url='http://127.0.0.1:5000')
    
    def test_login_user(self):
        driver = self.driver
        driver.find_element_by_link_text('Login').click()
        
        self.assertEqual('Flaskmin | Login', driver.title)
        
        username = driver.find_element_by_id('username')
        password = driver.find_element_by_id('password')
        submit_button = driver.find_element_by_id('submit')
        
        self.assertTrue(
            username.is_enabled()
            and password.is_enabled()
            and submit_button.is_enabled()
        )
        
        username.send_keys('python')
        driver.implicitly_wait(10)
        
        password.send_keys('my485p@ssw0rd')
        driver.implicitly_wait(10)
        
        submit_button.click()
    
    @classmethod
    def tearDown(cls) -> None:
        return cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)