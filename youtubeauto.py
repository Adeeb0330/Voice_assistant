from idlelib import query

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

from Pyweb import infow



class Music():
    def __init__(self):
        service = Service(r"C:\msedgefile\msedgedriver.exe")  # Use Service to specify the path
        self.driver = webdriver.Edge(service=service)  # Pass the service object

    def play(self, query):
        self.driver.get("https://www.youtube.com/results?search_query="+query)
        video = self.driver.find_element(By.XPATH,'//*[@id="video-title"]/yt-formatted-string')
        video.click()
        time.sleep(100)



