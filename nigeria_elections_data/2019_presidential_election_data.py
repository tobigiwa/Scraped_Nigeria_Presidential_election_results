from main import browser_driver, dispatchList
from typing import List, Dict
import pandas as pd
import re


URL = "https://en.wikipedia.org/wiki/2019_Nigerian_general_election"
browser_driver.get(URL)

table_header = [i.text for i in dispatchList("table:nth-of-type(7)  > thead > tr > th")[:9]] 
table_header_without_nicolas = table_header[:3] + table_header[4:] # a column data was not consistent

pattern = re.compile("\d{1,2}\.\d{1,2}")
raw_results = [re.sub(pattern, '', i.text, count=0) for i in dispatchList("table:nth-of-type(7) tbody tr")[:38]]

browser_driver.quit()  # quit automated web browser

def transform_results(raw_data_point: str, header: List[List[str]] = [table_header, table_header_without_nicolas]) -> Dict[str, str]: # the header parameter is a list, table_header and table_header_without_nicolas
    pattern = re.compile("[a-zA-Z]+")

    str_data_point, states = re.sub(pattern,'', raw_data_point, count=0), pattern.findall(raw_data_point) # separats the states and string digits    
    integer_data_point = list(map(int, [i.replace(',', '') for i in str_data_point.split()]))  # converts the string digits to integers 
    votes_data = ['_'.join(states)] + integer_data_point
    if len(votes_data) == 9:
            return {key: value for key, value in zip(header[0], votes_data)} # use heaer_table
    else:
        return {key: value for key, value in zip(header[1], votes_data)} # use heaer_table_without_nicolas


votes = list(map(transform_results, raw_results))

dataFrame = pd.DataFrame(votes, columns=table_header)
dataFrame.to_csv("2019_presidential_data_point.csv", index=False)