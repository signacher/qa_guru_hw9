from data import users
from data.users import User, Gender, Subject, Hobbie, Month
from pages.registration_page import RegistrationPage

def test_student_registration_form():
    registration_page = RegistrationPage()
    student = User(first_name='Ivan',
                   last_name='Ivanov',
                   email='name@example.ru',
                   gender=Gender.Male.value,
                   phone_number='1234567891',
                   birth_day='21',
                   birth_month=Month.May.value,
                   birth_year='1999',
                   subject=Subject.computer_science.value,
                   hobbie=Hobbie.reading.value,
                   upload_filename='css_selector.png',
                   current_address='Moscowskaya Street 18',
                   state='NCR',
                   city='Delhi')
    registration_page.open()

    registration_page.register(student)

    # registration_page.should_have_registered(student)

