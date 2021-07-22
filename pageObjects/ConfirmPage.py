from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By. ID, "country")
    # driver.find_element_by_id("country").send_keys("ind")
    countryName = (By.LINK_TEXT, "India")
    # driver.find_element_by_link_text("India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    # driver.find_element_by_css_selector("[type='submit']")
    message = (By.CLASS_NAME, "alert-success")
    # driver.find_element_by_class_name("alert-success")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def successText(self):
        return self.driver.find_element(*ConfirmPage.message)
