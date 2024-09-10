from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sources.locators import StellarBurgersLocators


class TestConstructorSection:
    def test_rolls(self, driver):
        driver.find_element(*StellarBurgersLocators.SECTION_SAUCES).click()
        driver.find_element(*StellarBurgersLocators.SECTION_ROLLS).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(StellarBurgersLocators.ROLLS))
        rolls = driver.find_element(*StellarBurgersLocators.ROLLS).text
        assert rolls == 'Булки'

    def test_sauces(self, driver):
        driver.find_element(*StellarBurgersLocators.SECTION_SAUCES).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(StellarBurgersLocators.SAUCES))
        sauces = driver.find_element(*StellarBurgersLocators.SAUCES).text
        assert sauces == 'Соусы'

    def test_fillings(self, driver):
        driver.find_element(*StellarBurgersLocators.SECTION_FILLINGS).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(StellarBurgersLocators.FILLINGS))
        fillings = driver.find_element(*StellarBurgersLocators.FILLINGS).text
        assert fillings == 'Начинки'
