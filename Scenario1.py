import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner


class GoogleSearch1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\SeleniumDrivers\chromedriver.exe")

    def test_search_automationStepByStep(self):
        self.driver.get("https://play.google.com/store?hl=en_US&gl=US")
        self.driver.find_element(By.LINK_TEXT, "Apps").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".TwyJFf").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "a[title='Education']").click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "q").send_keys("TED")
        time.sleep(3)
        self.driver.find_element(By.ID, "gbqfb").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "//body/div[@id='fcxH9b']/div[@class='WpDbMd']/c-wiz[@class='zQTmif SSPGKf I3xX3c']/div[@class='T4LgNb']/div[@class='N4FjMb ']/div[@jscontroller='WcZbQd']/c-wiz[@jsrenderer='LRovxc']/c-wiz[@class='UBeTzd Ubi8Z']/c-wiz/div[1]/div[2]/div[1]/c-wiz[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]").click()



if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Alwqar/PycharmProjects/TestAutomation/reports'))
