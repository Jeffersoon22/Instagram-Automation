from Steps.Login_steps import LoginAutomation
from Session import credentials

login_steps = LoginAutomation()


class TestLogin:
    def test_login_button(self):
        button = login_steps.check_sign_in_button()
        assert button.is_displayed() and button.is_enabled()

    def test_click_sign_in(self):
        login_steps.click_sign_in()

    def test_login(self):
        login_steps.sign_in_Instagram(credentials.user_credentials)
