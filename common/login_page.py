# author: "eight"
# date: 2025/2/27 11:25
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.config import HOST
from common.readyml import get_yaml_data

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = HOST + get_yaml_data('./config/test.yml')['login']['path']
        self.driver.get(url)
        self.driver.implicitly_wait(2)#隐式等待2S
        #self.driver.get("http://47.107.116.139/phpwind/index.php?m=u&c=login")

    def input_username(self, username):
        username_input = self.driver.find_element(By.ID, "J_u_login_username")
        username_input.send_keys(username)

    def input_password(self, password):
        password_input = self.driver.find_element(By.ID, "J_u_login_password")
        password_input.send_keys(password)
        self.driver.implicitly_wait(2)  # 隐式等待2S

    def click_login_button(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn_big.btn_submit.mr20")
        login_button.click()

    def get_title(self):
        return self.driver.title

