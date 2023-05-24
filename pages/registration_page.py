from selene.support.shared import browser
from selene import have
from selene import command
import os
from data.users import  User

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def register(self, student:User):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').send_keys(student.last_name)
        browser.element("#userEmail").type(student.email)
        browser.all('[name=gender]').element_by(have.value(f'{student.gender}')).element('..').click()
        browser.element('[id="userNumber"]').send_keys(student.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(student.birth_year)
        browser.element('.react-datepicker__month-select').send_keys(student.birth_month)
        browser.element(f'.react-datepicker__day--0{student.birth_day}').click()

        browser.element('#subjectsInput').send_keys(student.subject).press_enter()

        browser.all('.custom-control-label').element_by(have.exact_text(student.hobbie)).perform(command.js.scroll_into_view).click()
        browser.element('[id="currentAddress"]').send_keys(student.current_address)
        browser.element('#uploadPicture').set_value(
            os.path.abspath(os.path.join(os.path.dirname(__file__) + f'../../resources/{student.upload_filename}')))
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(student.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.city)).click()
        browser.element('#submit').perform(command.js.click)

    def should_have_registered(self, student:User):
        full_name = f'{student.first_name} {student.last_name}'
        date_of_birth = f'{student.birth_day} {student.birth_month},{student.birth_year}'
        subjects = ', '.join([subject.value for subject in student.subject])
        hobbies = ', '.join([hobby.value for hobby in student.hobbie])
        state_city = f'{student.state} {student.city}'
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                student.email,
                student.gender,
                str(student.phone_number),
                date_of_birth,
                subjects,
                hobbies,
                student.upload_filename,
                student.current_address,
                state_city
            )
        )