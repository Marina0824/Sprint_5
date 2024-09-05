from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sources.locators import StellarBurgersLocators


class TestConstructorSection:
    def test_rolls_is_current(self, driver):
        rolls = driver.find_element(*StellarBurgersLocators.IS_CURRENT)
        assert rolls is not None

    def test_move_to_sauces(self, driver):
        driver.find_element(*StellarBurgersLocators.SECTION_SAUCES).click()
        sauces = WebDriverWait(driver, 10).until(EC.presence_of_element_located(StellarBurgersLocators.IS_CURRENT))
        assert sauces is not None

    def test_move_to_fillings(self, driver):
        driver.find_element(*StellarBurgersLocators.SECTION_FILLINGS).click()
        fillings = WebDriverWait(driver, 10).until(EC.presence_of_element_located(StellarBurgersLocators.IS_CURRENT))
        assert fillings is not None
