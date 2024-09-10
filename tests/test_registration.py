from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sources.helpers import get_sign_up_data
from sources.locators import StellarBurgersLocators


class TestRegistration:
    def test_registration_success(self, driver):
        email_data, password_data = get_sign_up_data()
        driver.find_element(*StellarBurgersLocators.LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.REGISTER).click()
        driver.find_element(*StellarBurgersLocators.NAME_FIELD).send_keys("pp")
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*StellarBurgersLocators.BUTTON_REGISTER).click()
        login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarBurgersLocators.BUTTON_LOGIN))
        assert login_button.is_displayed(), "Button is not displayed"

    def test_incorrect_password_error(self, driver):
        driver.find_element(*StellarBurgersLocators.LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.REGISTER).click()
        driver.find_element(*StellarBurgersLocators.NAME_FIELD).send_keys("pp")
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys("pppp@yandex.ru")
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys("pp")
        driver.find_element(*StellarBurgersLocators.BUTTON_REGISTER).click()
        error_incorrect_password = driver.find_element(*StellarBurgersLocators.ERROR_INCORRECT_PASSWORD)
        assert error_incorrect_password.is_displayed(), "Error is not displayed"
