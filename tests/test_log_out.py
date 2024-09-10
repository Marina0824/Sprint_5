from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sources.data import existing_email, existing_password
from sources.locators import StellarBurgersLocators


class TestMoveFromPersonalAccount:
    def test_move_to_constructor(self, driver):
        driver.find_element(*StellarBurgersLocators.LOG_IN_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(existing_email)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(existing_password)
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarBurgersLocators.BUTTON_LOGOUT))
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGOUT).click()
        success = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(StellarBurgersLocators.BUTTON_LOGIN))
        assert success.is_displayed()
