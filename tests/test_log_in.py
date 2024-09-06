from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sources.data import existing_email, existing_password
from sources.locators import StellarBurgersLocators


class TestLogIn:
    def test_button_log_in_to_account(self, driver):
        driver.find_element(*StellarBurgersLocators.LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(existing_email)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(existing_password)
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN).click()
        success = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarBurgersLocators.BUTTON_ORDER))
        assert success.is_displayed()

    def test_button_personal_account(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        success = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarBurgersLocators.BUTTON_LOGIN))
        assert success.is_displayed()

    def test_link_in_registration_form(self, driver):
        driver.find_element(*StellarBurgersLocators.LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.REGISTER).click()
        element = driver.find_element(*StellarBurgersLocators.LINK_LOGIN)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.find_element(*StellarBurgersLocators.LINK_LOGIN).click()
        success = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarBurgersLocators.BUTTON_LOGIN))
        assert success.is_displayed()

    def test_link_in_password_recovery_form(self, driver):
        driver.find_element(*StellarBurgersLocators.LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LINK_PASSWORD_RECOVERY).click()
        driver.find_element(*StellarBurgersLocators.LINK_LOGIN).click()
        success = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarBurgersLocators.BUTTON_LOGIN))
        assert success.is_displayed()
