from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_scenario(context, scenario):
    """ Setup: Runs before each scenario """
    chrome_option = Options()
    chrome_option.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    context.driver.maximize_window()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def after_scenario(context, scenario):
    """ Teardown: Runs after each scenario """
    if context.driver:
        context.driver.quit()
