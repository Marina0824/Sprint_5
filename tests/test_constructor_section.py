from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sources.locators import StellarBurgersLocators


class TestConstructorSection:
    def test_rolls(self, driver):
        driver.find_element(*StellarBurgersLocators.SECTION_SAUCES).click()
        driver.find_element(*StellarBurgersLocators.SECTION_ROLLS).click()
        roll = WebDriverWait(driver, 10).until(EC.presence_of_element_located(StellarBurgersLocators.ROLL))
        assert roll.is_displayed()

    def test_sauces(self, driver):
        driver.find_element(*StellarBurgersLocators.SECTION_SAUCES).click()
        sauce = WebDriverWait(driver, 10).until(EC.presence_of_element_located(StellarBurgersLocators.SAUCE))
        assert sauce.is_displayed()

    def test_fillings(self, driver):
        driver.find_element(*StellarBurgersLocators.SECTION_FILLINGS).click()
        filling = WebDriverWait(driver, 10).until(EC.presence_of_element_located(StellarBurgersLocators.FILLING))
        assert filling.is_displayed()
