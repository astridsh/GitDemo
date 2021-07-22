import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# @pytest.mark.usefixtures("setup")
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitle()

        i = -1
        #//div[@class='card h-100']/div/h4/a
        #product =//div[@class='card h-100']
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                #Add item into cart
                checkOutPage.getCardFooter()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        confirmPage = checkOutPage.CheckOutItems()
        log.info("Entering country name as ind")
        confirmPage.getCountry().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.getCountryName().click()
        confirmPage.getCheckBox().click()
        confirmPage.getSubmit().click()
        textMatch = confirmPage.successText().text
        log.info("Text received from application is "+ textMatch)

        assert ("Success! thrasd you!" in textMatch)




