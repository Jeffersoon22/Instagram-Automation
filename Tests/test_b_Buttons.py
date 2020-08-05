import allure
from Steps.Buttons_steps import ButtonsAutomation

my_buttons = ButtonsAutomation()


class TestButtons:
    @allure.title('მთავარი გვერდის ღილაკის არსებობის შემოწმება')
    @allure.step('მოწმდება მთავარი გვერდის ღილაკი არის თუ არა ჩართული და ხილვადი')
    def test_home_button(self):
        home_button = my_buttons.check_home_button()
        allure.attach.file('Screenshots/Home_button_on_page.png', name='Home_on_page', attachment_type=allure.attachment_type.PNG)
        assert home_button.is_enabled() and home_button.is_displayed()

    @allure.title('ძებნის ღილაკის არსებობის შემოწმება')
    @allure.step('მოწმდება ძებნის ღილაკი არის თუ არა ჩართული და ხილვადი')
    def test_search_button(self):
        search_button = my_buttons.check_search_button()
        allure.attach.file('Screenshots/Search_button_on_page.png', name='Search_on_page', attachment_type=allure.attachment_type.PNG)
        assert search_button.is_displayed() and search_button.is_enabled()

    @allure.title('პოსტის დამატების ღილაკის არსებობის შემოწმება')
    @allure.step('მოწმდება ახალი პოსტის ღილაკი არის თუ არა ჩართული და ხილვადი')
    def test_add_button(self):
        add_button = my_buttons.check_add_icon()
        allure.attach.file('Screenshots/Add_Post_button_on_page.png', name='Add_Post_on_page', attachment_type=allure.attachment_type.PNG)
        assert add_button.is_enabled() and add_button.is_displayed()

    @allure.title('აქტივობის ღილაკის არსებობის შემოწმება')
    @allure.step('მოწმდება აქტივობის ღილაკი არის თუ არა ჩართული და ხილვადი')
    def test_activity_button(self):
        activity_button = my_buttons.check_Activity_button()
        allure.attach.file('Screenshots/Activity_button_on_page.png', name='Activity_on_page', attachment_type=allure.attachment_type.PNG)
        assert activity_button.is_enabled() and activity_button.is_displayed()

    @allure.title('პროფილის ღილაკის არსებობის შემოწმება')
    @allure.step('მოწმდება პროფილის ღილაკი არის თუ არა ჩართული და ხილვადი')
    def test_profile_button(self):
        profile_button = my_buttons.check_profile_button()
        allure.attach.file('Screenshots/Profile_button_on_page.png', name='Profile_on_page', attachment_type=allure.attachment_type.PNG)
        assert profile_button.is_enabled() and profile_button.is_displayed()

    @allure.title('აპლიკაციის დახურვა')
    @allure.step('იხურება აპლიკაცია')
    def test_close_app(self):
        my_buttons.close_app()
        allure.attach.file('Screenshots/Close.png', name='Close_page', attachment_type=allure.attachment_type.PNG)
