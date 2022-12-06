from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.eloratings.net/')

teamData = driver.find_elements(By.CLASS_NAME, 'ui-widget-content')
