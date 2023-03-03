from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
from typing import List, Dict

URL = "https://en.wikipedia.org/wiki/2023_Nigerian_presidential_election#By_state"

browser_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser_driver.get(URL)

def dispatch(locator:str, strategy:webdriver = By.CSS_SELECTOR, driver:webdriver = browser_driver) -> str:
    "Call to selenium.webdriver.remote.webelement.WebElement.find_element()"
    return driver.find_element(strategy, locator)


def dispatchList(locator:str, strategy: webdriver = By.CSS_SELECTOR, driver:webdriver = browser_driver) -> List[WebElement]:
    "Call to selenium.webdriver.remote.webelement.WebElement.find_elements()"
    return driver.find_elements(strategy, locator)


table_header = [i.text for i in dispatchList("table:nth-of-type(13) > thead > tr > th a")] 
table_header += ["Others", "Total_valid_votes"] # includes two extra columns

pattern = re.compile("\d{1,2}%|\d{1,2}.\d{1,2}%|\[\d+\]")
raw_results = [re.sub(pattern, '', i.text, count=0) for i in dispatchList("table:nth-of-type(13) tbody tr")]


def transform_results(raw_data_point: str, header: List[str] = table_header) -> Dict[str, str]:

    pattern = re.compile("[a-zA-Z]+")
    
    str_data_point, states = re.sub(pattern,'', raw_data_point, count=0), pattern.findall(raw_data_point) # separats the states and string digits    
    integer_data_point = list(map(int, [i.replace(',', '') for i in str_data_point.split()]))  # converts the string digits to integers 
    votes_data = ['_'.join(states)] + integer_data_point
    return {key: value for key, value in zip(header, votes_data)}


votes = list(map(transform_results, raw_results))
for i in votes:
    print(i)




time.sleep(1)
browser_driver.quit()