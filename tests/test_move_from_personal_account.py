from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sources.data import get_exist_user_data
from sources.locators import StellarBurgersLocators


class TestMoveFromPersonalAccount:
    def test_move_to_constructor(self, driver):
        existing_email, existing_password = get_exist_user_data()
        driver.find_element(*StellarBurgersLocators.LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(existing_email)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(existing_password)
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCTOR).click()
        success = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarBurgersLocators.BUTTON_ORDER))
        assert success.is_displayed()

    def test_move_to_logo(self, driver):
        existing_email, existing_password = get_exist_user_data()
        driver.find_element(*StellarBurgersLocators.LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(existing_email)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(existing_password)
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LOGO).click()
        success = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarBurgersLocators.BUTTON_ORDER))
        assert success.is_displayed()
