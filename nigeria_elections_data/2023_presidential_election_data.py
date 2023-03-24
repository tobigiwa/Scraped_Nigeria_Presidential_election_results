from main import browser_driver, dispatchList
from typing import List, Dict
import pandas as pd
import re


URL = "https://en.wikipedia.org/wiki/2023_Nigerian_presidential_election#By_state"
browser_driver.get(URL)

table_header = [i.text for i in dispatchList("table:nth-of-type(12) > thead > tr > th a")] 
table_header =  [i.replace(' ', '_') for i in table_header] + ["Others", "Total_valid_votes"] # replace space between name with underscore + include two extra columns

pattern = re.compile("\d{1,2}%|\d{1,2}.\d{1,2}%|\[\d+\]")
raw_results = [re.sub(pattern, '', i.text, count=0) for i in dispatchList("table:nth-of-type(12) tbody tr")]

browser_driver.quit()  # quit automated web browser

def transform_results(raw_data_point: str, header: List[str] = table_header) -> Dict[str, str]:
    pattern = re.compile("[a-zA-Z]+")

    str_data_point, states = re.sub(pattern,'', raw_data_point, count=0), pattern.findall(raw_data_point) # separats the states and string digits    
    integer_data_point = list(map(int, [i.replace(',', '') for i in str_data_point.split()]))  # converts the string digits to integers 
    votes_data = ['_'.join(states)] + integer_data_point
    return {key: value for key, value in zip(header, votes_data)} 


votes = list(map(transform_results, raw_results))

dataFrame = pd.DataFrame(votes, columns=table_header)
dataFrame.to_csv("2023_presidential_data_.csv", index=False)