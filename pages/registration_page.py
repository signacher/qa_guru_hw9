from selene.support.shared import browser
from selene import have
from selene import command
import os
from selenium.webdriver import Keys

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').send_keys(value)

    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(f'{value}')).element('..').click()

    def fill_mobile_number(self, value):
        browser.element('[id="userNumber"]').send_keys(value)

    def fill_date_of_birth(self, day, month, year ):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def select_subject(self, value):
        browser.element('#subjectsInput').send_keys(value).press_enter()

    def select_hobby(self, value):
        browser.all('.custom-control-label').element_by(have.exact_text(value)).perform(command.js.scroll_into_view).click()

    def fill_current_adress(self, value):
        browser.element('[id="currentAddress"]').send_keys(value)

    def upload_file(self, filename):
        browser.element('#uploadPicture').set_value(
            os.path.abspath(os.path.join(os.path.dirname(__file__) + f'../../resources/{filename}')))

    def select_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)).click()

    def select_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)

    def should_user_data(self, *values):
        browser.element('.table').all('td').even.should(
            have.exact_texts(values))