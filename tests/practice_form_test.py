#from selene.support.shared import browser
from selene import browser, have, command
import os
import tests

def test_student_registration_form():
    browser.open('/automation-practice-form')

    browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    # WHEN
    browser.element('#firstName').type('Tom')
    browser.element('#lastName').type('Skov')
    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
    browser.element('#userNumber').type('1234567891')
    browser.element('#userEmail').type('Tom.Skov@yahoo.com')
    browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#currentAddress').type('Gagarinsky 19')
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('NCR')
    ).click()


    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('2003')
    browser.element(f'.react-datepicker__day--0{12}').click()

    browser.element('#subjectsInput').type('History').press_enter()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resources/foto.jpg')
        )
    )

    browser.element('#submit').press_enter()

    # THEN

    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Tom Skov',
            'Tom.Skov@yahoo.com',
            'Male',
            '1234567891',
            '12 May,2003',
            'History',
            'Reading',
            'foto.jpg',
            'Gagarinsky 19',
            'NCR Delhi',
        )
    )
