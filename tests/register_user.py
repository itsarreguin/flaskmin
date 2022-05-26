"""Register new user in the app"""

import unittest
from selenium import webdriver


class RegiterUser(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.get(url='http://127.0.0.1:5000')
    
    def test_register_new_user(self):
        driver = self.driver
        driver.find_element_by_link_text(link_text='Sign Up').click()
        
        self.assertEqual('Flaskmin | Sign Up', driver.title)
        
        first_name = driver.find_element_by_id(id_='first_name')
        last_name = driver.find_element_by_id(id_='last_name')
        username = driver.find_element_by_id(id_='username')
        email = driver.find_element_by_id(id_='email')
        password = driver.find_element_by_id(id_='password_hash')
        password_confirm = driver.find_element_by_id(id_='password_verify')
        submit_button = driver.find_element_by_id(id_='submit')
        
        self.assertTrue(
            first_name.is_enabled()
            and last_name.is_enabled()
            and username.is_enabled()
            and email.is_enabled()
            and password.is_enabled()
            and password_confirm.is_enabled()
            and submit_button.is_enabled()
        )
        
        first_name.send_keys('Monty')
        driver.implicitly_wait(10)

        last_name.send_keys('Python')
        driver.implicitly_wait(10)
        
        username.send_keys('python')
        driver.implicitly_wait(10)
        
        email.send_keys('email@example.com')
        driver.implicitly_wait(10)
        
        password.send_keys('my485p@ssw0rd')
        driver.implicitly_wait(10)

        password_confirm.send_keys('my485p@ssw0rd')
        driver.implicitly_wait(10)
        
        submit_button.click()
        driver.implicitly_wait(30)
    
    @classmethod
    def tearDown(cls) -> None:
        return cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)