from Steps.Buttons_steps import ButtonsAutomation

my_buttons = ButtonsAutomation()


class TestButtons:
    def test_home_button(self):
        home_button = my_buttons.check_home_button()
        assert home_button.is_enabled() and home_button.is_displayed()

    def test_search_button(self):
        search_button = my_buttons.check_search_button()
        assert search_button.is_displayed() and search_button.is_enabled()

    def test_add_button(self):
        add_button = my_buttons.check_add_icon()
        assert add_button.is_enabled() and add_button.is_displayed()

    def test_activity_button(self):
        activity_button = my_buttons.check_following_heart_button()
        assert activity_button.is_enabled() and activity_button.is_displayed()

    def test_profile_button(self):
        profile_button = my_buttons.check_profile_button()
        assert profile_button.is_enabled() and profile_button.is_displayed()

    def test_close_app(self):
        my_buttons.close_app()
