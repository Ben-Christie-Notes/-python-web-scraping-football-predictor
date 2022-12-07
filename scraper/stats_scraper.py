from selenium import webdriver
from selenium.webdriver.common.by import By

def get_data():
  file = open('./scraper/fbref_competition_links.txt', 'r')
  
  data = []

  for line in file:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(line)

    data.append(driver.find_element(By.ID, 'stats_squads_standard_for'))

    driver.close()
  file.close()

  return data

test = get_data()

for table in test:
  print(table)