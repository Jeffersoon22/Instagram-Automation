import time
from appium import webdriver
from Helper.printColored import PrintColored as printColored
from Session import deviceConfiguration


class LoginAutomation:

    def __init__(self):
        self.driver = webdriver.Remote(deviceConfiguration.remote, deviceConfiguration.device)

    def check_sign_in_button(self):
        self.driver.save_screenshot('Screenshots/' + 'Main_page.png')
        button = self.driver.find_element_by_id('com.instagram.android:id/log_in_button')
        return button

    def click_sign_in(self, function):
        printColored("იძებნება შესვლის ღილაკი").waiting()
        try:
            button = function
            printColored('შესხვლის ღილაკი არსებობს').success()
            button.click()
            printColored("აპლიკაცია მზად არის მონაცემების შესაყვანად").success()
        except:
            printColored('შესვლა შეუძლებელია...').failed()

    def input_username(self, credentials):
        self.driver.implicitly_wait(4)
        # self.driver.save_screenshot('Screenshots/'+self.driver.current_activity+'.png') არ იღებს security policy გამო
        printColored('ვეძებთ მომხმარებლის სახელის შესაყვან ველს').waiting()
        try:
            username_Input = self.driver.find_element_by_id('com.instagram.android:id/login_username')
            if username_Input:
                printColored('შეგვყავს მომხმარებლის სახელი').success()
                username_Input.send_keys(credentials['Username'])
            return username_Input.text
        except:
            printColored('მომხმარებლის სახელის შესაყვანი ველი არ მოიძებნა')

    def input_password(self, credentials):
        # self.driver.save_screenshot('Screenshots/'+self.driver.current_activity+'.png') არ იღებს security policy გამო
        printColored('ვეძებთ მომხმარებლის პაროლის შესაყვან ველს').waiting()
        try:
            password_Input = self.driver.find_element_by_id('com.instagram.android:id/password')
            if password_Input:
                printColored('შეგვყავს მომხმარებლის პაროლს').success()
                password_Input.send_keys(credentials['Password'])
            return password_Input.text
        except:
            printColored('მომხმარებლის პაროლის შესაყვანი ველი არ მოიძებნა')

    def signin_Instagram(self):
        # self.driver.save_screenshot('Screenshots/self_from_login.png') არ იღებს security policy-ს გამო

        printColored("ვიწყებთ შესვლას ინსტაგრამზე").waiting()
        try:
            username_Input = self.driver.find_element_by_id('com.instagram.android:id/login_username').text
            password_Input = self.driver.find_element_by_id('com.instagram.android:id/password').text
            button = self.driver.find_element_by_id('com.instagram.android:id/next_button')
            if username_Input is not None and password_Input is not None:
                button.click()
                time.sleep(4)  # მგონი 4 ეყოფა
                self.driver.save_screenshot('Screenshots/' + 'Logged_in.png')
        except:
            printColored('შესვლა შეუძლებელია...').failed()
