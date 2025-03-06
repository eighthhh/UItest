# author: "eight"
# date: 2025/2/27 11:37
import time

import pytest
from selenium import webdriver
from common.login_page import LoginPage
from common.home_page import HomePage


@pytest.fixture(scope="module")
def setup():
    # 在测试开始前执行的代码，例如初始化浏览器
    driver = webdriver.Chrome()
    yield driver
    # 在测试结束后执行的代码，例如关闭浏览器
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestUI:

    def test_login(self, setup):
        # 创建登录页面对象
        login_page = LoginPage(setup)
        # 打开登录页面
        login_page.open()
        # 输入用户名和密码
        login_page.input_username("lisa")
        login_page.input_password("bai123")
        # 点击登录按钮
        login_page.click_login_button()
        # 断言登录成功后的页面是否正确
        print(login_page.get_title())
        assert login_page.get_title() == "登录 - phpwind 9.0 - Powered by phpwind"

    def test_logout(self, setup):
        # 创建登录页面对象
        login_page = LoginPage(setup)
        # 打开登录页面
        login_page.open()
        # 输入用户名和密码
        login_page.input_username("lisa")
        time.sleep(1)
        login_page.input_password("bai123")
        # 点击登录按钮
        login_page.click_login_button()
        # 创建首页对象
        home_page = HomePage(setup)
        # 点击退出按钮
        home_page.click_logout_button()
        # 断言退出后是否回到登录页面
        print(home_page.get_title())
        assert home_page.get_title() == "新帖 - phpwind 9.0 - Powered by phpwind"


