from pages.registration_page import RegistrationPage

def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Ivanov')

    registration_page.fill_email('name@example.ru')

    registration_page.select_gender('Male')

    registration_page.fill_mobile_number('1234567891')

    registration_page.fill_date_of_birth('21', 'May', '1999')

    registration_page.select_subject('Computer Science')

    registration_page.select_hobby("Reading")

    registration_page.fill_current_adress('Moscowskaya Street 18')

    registration_page.upload_file('css_selector.png')

    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')

    registration_page.submit_form()

    # THEN

    registration_page.assert_user_info(
            'Ivan Ivanov',
            'name@example.ru',
            'Male',
            '1234567891',
            '21 May,1999',
            'Computer Science',
            'Reading',
            'css_selector.png',
            'Moscowskaya Street 18',
            'NCR Delhi',
        )

