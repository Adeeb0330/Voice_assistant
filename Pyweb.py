import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

class infow():
    def __init__(self):
        service = Service(r"C:\msedgefile\msedgedriver.exe")  # Use Service to specify the path
        self.driver = webdriver.Edge(service=service)  # Pass the service object

    def get_info(self, query):
        self.driver.get("https://www.wikipedia.org")
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH,'//*[@id="search-form"]/fieldset/button/i')
        enter.click()

        time.sleep(500)




