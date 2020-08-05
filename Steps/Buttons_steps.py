import time
from Helper.printColored import PrintColored as printColored
from Steps.Login_steps import LoginAutomation


class ButtonsAutomation:
    def __init__(self):
        self.driver = LoginAutomation().driver

    def check_home_button(self):
        self.driver.save_screenshot('Screenshots/'+'Home_button_on_page.png')
        time.sleep(3)
        printColored('იძებნება ჰოუმ ღლაკი').waiting()
        try:
            home_button = self.driver.find_element_by_accessibility_id('Home')
            if home_button.is_displayed() and home_button.is_enabled():
                printColored('ჰოუმ ღილაკი არსებობს').success()
                return home_button
        except:
            printColored('ჰოუმის ღილაკი არ არსებობს').failed()

    def check_search_button(self):
        self.driver.save_screenshot('Screenshots/'+'Search_button_on_page.png')
        printColored('იძებნება ძებნის ღილაკი').waiting()
        try:
            search_button = self.driver.find_element_by_accessibility_id('Search and explore')
            if search_button.is_enabled() and search_button.is_displayed():
                printColored('ძებნის ღილაკი ნაპოვნია').success()
                return search_button
        except:
            printColored('ძებნის ხატულა არ მოიძებნა').failed()

    def check_add_icon(self):
        self.driver.save_screenshot('Screenshots/'+'Add_Post_button_on_page.png')
        printColored('იძებნება პოსტის დამატების ღილაკი').waiting()
        try:
            add_button = self.driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Camera"]')
            if add_button.is_displayed() and add_button.is_enabled():
                printColored('ახალი პოსტის ღილაკი ნაპოვნია').success()
                return add_button
        except:
            printColored('ახალი პსოტისთვის ღილაკი ვერ მოიძებნა').failed()

    def check_Activity_button(self):
        self.driver.save_screenshot('Screenshots/'+'Activity_button_on_page.png')
        printColored('იძებნება სიახლეების ღილაკი ♡').waiting()
        try:
            heart_button = self.driver.find_element_by_accessibility_id('Activity')
            if heart_button.is_enabled() and heart_button.is_displayed():
                printColored('სიახლეების ღილაკი ნაპოვნია').success()
                return heart_button
        except:
            printColored('სიახლეების ღილაკი ვერ მოიძებნა').failed()

    def check_profile_button(self):
        self.driver.save_screenshot('Screenshots/'+'Profile_button_on_page.png')
        printColored('იძებნება პროფილის ღილაკი').waiting()
        try:
            profile_button = self.driver.find_element_by_accessibility_id('Profile')
            if profile_button.is_displayed() and profile_button.is_enabled():
                printColored('პროფილის ღილაკი ნაპოვნია').success()
                return profile_button
        except:
            printColored('პროფილის ღილაკი ვერ მოიძებნა').failed()

    def close_app(self):
        time.sleep(2)
        printColored('აპლიკაცია იხურება').waiting()
        self.driver.close_app()
        self.driver.save_screenshot('Screenshots/'+'Close.png')
        printColored('აპლიკაცია დაიხურა').success()
