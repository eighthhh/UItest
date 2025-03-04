# author: "eight"
# date: 2025/2/27 17:34
import os
import pytest

if __name__ == "__main__":
    #先单独执行这一行。设置一下allure生成json格式的临时报告路径./temp就是放到当前路径的temp文件夹下。
    pytest.main(['-vs', '--alluredir=./reports/temp', '--clean-alluredir'])

    #pytest.main()
    #allure generate 命令，固定的
    os.system('allure generate ./reports/temp -o ./reports/allure --clean')




    #os.system('pytest --alluredir=./allure-results --clean')
    #os.system('allure serve ./allure-results --clean')

    # 命令运行测试
    # pytest --alluredir=./allure-results
    # 运行完毕后，可以使用以下命令生成测试报告：
    # allure serve ./allure-results
