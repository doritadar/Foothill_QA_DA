from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

links_landing_titles = {
    "DOCS" :["#global > div > section > ul.unstyled.pull-right.group > li:nth-child(2) > a", "Docs"],
    "FEATURES" : ["#global > div > section > ul.unstyled.pull-left.group > li:nth-child(1) > a", "Features"],
    "COMPANY" : ["#global > div > section > ul.unstyled.pull-left.group > li:nth-child(2) > a", "Sauce Labs: Values"],
    "COMMUNITY" : ["#global > div > section > ul.unstyled.pull-left.group > li:nth-child(3) > a:nth-child(1)", "Open Sauce"],
    "SOLUTIONS" : ["#global > div > section > ul.unstyled.pull-left.group > li:nth-child(3) > a:nth-child(3)", "Selenium Testing by Sauce Labs"],
    "RESOURCES" : ["#global > div > section > ul.unstyled.pull-right.group > li:nth-child(1) > a", "Resources"],
    "ENTERPRISE" : ["#global > div > section > ul.unstyled.pull-right.group > li:nth-child(3) > a", "Sauce Labs: Enterprise-grade testing on Sauce"],
    "PRICING" : ["#global > div > section > ul.unstyled.pull-right.group > li:nth-child(4) > a", "Sauce Labs: Pricing"],
    "SIGN UP" : ["#global > div > section > ul.unstyled.pull-right.group > li:nth-child(5) > a", "Sauce Labs: Sign Up for a Free Trial"],
    "LOGIN" : ["#global > div > section > ul.unstyled.pull-right.group > li:nth-child(6) > a", "Sauce Labs: Login"],
    }



class SauceLabsThreeHorizontalBar(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_sauce_labs_three_horizintal_bar(self):
        driver = self.driver
        
        for link in links_landing_titles:
            driver.get(self.base_url)
            driver.find_element_by_xpath("//li/a[@class='hamburger']").click()
            driver.find_element_by_css_selector(links_landing_titles[link][0]).click()
            expected_title = links_landing_titles[link][1]
            try: self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e: self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
