from selenium import webdriver
import unittest
import time

links_landing_titles = {
    r"Japanese Department" : r"Japanese" ,
    "Journalism and Mass Communication" : r"Journalism and Mass Communication" ,
    }

class DeAnzaHeaders(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/directory/dir-az.html"
        self.verificationErrors = []
    
    def test_de_anza_headers(self):
        driver = self.driver

        for link in links_landing_titles:
            driver.get(self.base_url)
            driver.find_element_by_link_text(link).click()
            expected_title = links_landing_titles[link]
            time.sleep(5)
            try: self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e: self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
