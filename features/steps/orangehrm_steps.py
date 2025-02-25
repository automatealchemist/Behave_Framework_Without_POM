import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given(u'Launch chrome browser')
def launchbrowser(context):
    chrome_option = Options()
    chrome_option.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    context.driver.maximize_window()

@when(u'Open Orange HRM Home Page')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then(u'Verify the logo present on page')
def verifyLogo(context):
    time.sleep(5)
    status = context.driver.find_element(By.CSS_SELECTOR,'#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-branding > img').is_displayed()
    assert status is True
    context.driver.quit()

