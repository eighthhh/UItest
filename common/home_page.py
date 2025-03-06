# author: "eight"
# date: 2025/2/27 14:08
from selenium.webdriver.common.by import By
import time
from common.config import HOST
from common.readyml import get_yaml_data
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = HOST + get_yaml_data('./config/test.yml')['index']['path']
        self.driver.get(url)
        self.driver.implicitly_wait(2)#隐式等待2S
        #self.driver.get("http://47.107.116.139/phpwind")


    def click_logout_button(self):
        self.driver.find_elements(By.CLASS_NAME,"header_login_later")[0].click()
        time.sleep(1)
        logout_button = self.driver.find_elements(By.CLASS_NAME, "icon_quit")[0]
        logout_button.click()
        time.sleep(2)

    def get_title(self):
        return self.driver.title

