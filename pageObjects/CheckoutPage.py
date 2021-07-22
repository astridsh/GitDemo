from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    # driver.find_elements_by_css_selector(".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    # driver.find_elements_by_css_selector(".card-footer button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")
    # driver.find_element_by_xpath("//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def CheckOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        comfirmPage = ConfirmPage(self.driver)
        return comfirmPage
