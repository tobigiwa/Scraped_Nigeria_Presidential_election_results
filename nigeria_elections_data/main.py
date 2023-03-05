from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from typing import List


browser_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def dispatch(locator:str, strategy:webdriver = By.CSS_SELECTOR, driver:webdriver = browser_driver) -> str:
    "Call to selenium.webdriver.remote.webelement.WebElement.find_element()"
    return driver.find_element(strategy, locator)


def dispatchList(locator:str, strategy: webdriver = By.CSS_SELECTOR, driver:webdriver = browser_driver) -> List[WebElement]:
    "Call to selenium.webdriver.remote.webelement.WebElement.find_elements()"
    return driver.find_elements(strategy, locator)
