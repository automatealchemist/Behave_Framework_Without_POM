import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



@then(u'close browser')
def homepage(context):
    try :
        a = context.driver.current_url
        assert a == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        print("Test Passed")
    except :
            assert False,"Test Failed"
    finally:
        context.driver.close()



@given(u'Openhrm Page is open')
def open_browser(context):
    pass  # No need to open browser here since `before_scenario` handles it

@when(u'enter username "{user}" and password "{pwd}"')
def login_data(context, user, pwd):
    time.sleep(10)
    context.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)

@then(u'user must be successfully login into the system')
def submit_data(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)