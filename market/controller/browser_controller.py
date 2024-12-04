import pathlib
from selenium.webdriver import Firefox

from ..model.database_keys import DatabaseKeys


class BrowserController:
    def __init__(self):
        self.executable = str((pathlib.Path(__file__).parents[1] / 'resources' / 'geckodriver').absolute())
        self.database_passwords_recover = DatabaseKeys()

    def open_gmail(self):
        username, password = self.database_passwords_recover.get_username_password('gmail')

        url = 'https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
        driver = Firefox(executable_path=self.executable)
        driver.maximize_window()
        driver.get(url)
        driver.find_element_by_id('identifierId').send_keys(username)
        driver.find_element_by_id('identifierNext').click()
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
        driver.find_element_by_id('passwordNext').click()

    def open_facebook(self):
        username, password = self.database_passwords_recover.get_username_password('facebook')

        url = 'https://www.facebook.com/'
        driver = Firefox(executable_path=self.executable)
        driver.maximize_window()
        driver.get(url)

        driver.find_element_by_id('email').send_keys(username)
        driver.find_element_by_id('pass').send_keys(password)
        driver.find_element_by_id('u_0_b').click()

    def open_google(self):
        url = 'http://www.google.com/'
        driver = Firefox(executable_path=self.executable)
        driver.maximize_window()
        driver.get(url)
