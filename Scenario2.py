import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner


class GoogleSearch2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\SeleniumDrivers\chromedriver.exe")

    def test_search_automationStepByStep(self):
        self.driver.get("https://play.google.com/store?hl=en_US&gl=US")
        self.driver.find_element(By.NAME, "q").send_keys("Facebook")
        time.sleep(3)
        self.driver.find_element(By.ID, "gbqfb").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//body/div[@id='fcxH9b']/div[contains(@class,'WpDbMd')]/c-wiz[contains(@class,'zQTmif SSPGKf I3xX3c')]/div[contains(@class,'T4LgNb')]/div[contains(@class,'N4FjMb')]/div[contains(@jscontroller,'WcZbQd')]/c-wiz[contains(@jsrenderer,'LRovxc')]/c-wiz[contains(@class,'UBeTzd Ubi8Z')]/c-wiz/div[contains(@class,'')]/div[contains(@class,'ZmHEEd')]/div[1]/c-wiz[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]").click()



if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Alwqar/PycharmProjects/TestAutomation/reports'))
