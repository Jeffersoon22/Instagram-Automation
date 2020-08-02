import time
from appium import webdriver
from Helper.printColored import PrintColored as printColored
from Session import deviceConfiguration


class LoginAutomation:
    def __init__(self):
        self.driver = webdriver.Remote(deviceConfiguration.remote, deviceConfiguration.device)

    def check_sign_in_button(self):
        button = self.driver.find_element_by_id('com.instagram.android:id/log_in_button')
        return button

    def click_sign_in(self):
        printColored("იძებნება შესვლის ღილაკი").waiting()
        try:
            button = self.driver.find_element_by_id('com.instagram.android:id/log_in_button')
            printColored('შესხვლის ღილაკი არსებობს').success()
            button.click()
            printColored("აპლიკაცია მზად არის მონაცემების შესაყვანად").success()
        except:
            printColored('შესვლა შეუძლებელია...').failed()

    def sign_in_Instagram(self, credentials):
        self.driver.implicitly_wait(4)
        printColored("ვიწყებთ შესვლას ინსტაგრამზე").waiting()
        try:
            usernameInput = self.driver.find_element_by_id('com.instagram.android:id/login_username')
            passwordInput = self.driver.find_element_by_id('com.instagram.android:id/password')
            button = self.driver.find_element_by_id('com.instagram.android:id/next_button')
            if usernameInput and passwordInput:
                usernameInput.send_keys(credentials['Username'])
                passwordInput.send_keys(credentials['Password'])
                button.click()
                time.sleep(3)
        except:
            printColored('შესვლა შეუძლებელია...').failed()

