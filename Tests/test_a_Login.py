import allure
from Steps.Login_steps import LoginAutomation
from Session import credentials

login_steps = LoginAutomation()




class TestLogin:
    @allure.title('შესვლის ღილაკის არსებობის შემოწმება')
    @allure.step('მოწმდება ღილაკია რის თუ არა აქტიური და ხილვადი')
    def test_login_button(self):
        button = login_steps.check_sign_in_button()
        allure.attach.file('Screenshots/Main_page.png', name='Main_page', attachment_type=allure.attachment_type.PNG)
        assert button.is_displayed() and button.is_enabled()

    @allure.title('შესვლის დასაწყებად ღილაკზე დაჭერა')
    @allure.step("ვაჭერთ შესვლის ღილაკს")
    def test_click_sign_in(self):
        login_steps.click_sign_in(login_steps.check_sign_in_button())

    @allure.title('შეყვანილი მომხმარებლის სახელის დადარება შესაყვანთან')
    @allure.step('ვადარებთ შესაყვანი მომხმარებლის სახელისა და შეყვანილის სიზუსტეს')
    def test_input_username(self):
        username = login_steps.input_username(credentials.user_credentials)
        assert credentials.user_credentials['Username'] == username

    @allure.title('შეყვანილი მომხმარებლის პაროლის დადარება შესაყვანთან')
    @allure.step('ვადარებთ შესაყვანი მომხმარებლის პაროლისა და შეყვანილის სიზუსტეს')
    def test_input_password(self):
        password = login_steps.input_password(credentials.user_credentials)
        assert credentials.user_credentials['Password'] == password

    @allure.title('დადასტურება შეყვანილი მონაცემების')
    @allure.step(f'ვაჭერთ შესვლის ღილაკს და შევსლა მონაცემებით:\n'
                 f'იუზერის სახელი : {credentials.user_credentials["Username"]}\n'
                 f'პაროლი: {credentials.user_credentials["Password"]}')
    def test_login(self):
        login_steps.signin_Instagram()
        allure.attach.file('Screenshots/Logged_in.png', name='Logged_in_page', attachment_type=allure.attachment_type.PNG)

