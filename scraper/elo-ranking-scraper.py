from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.eloratings.net/')

teamData = driver.find_elements(By.CLASS_NAME, 'ui-widget-content')

# print(teamData[0].text)

# {
#     rank: 1,
#     name: Brazil,
#     rating: 2150,
#     avg_rank: 4,
#     avg_rating: 1999,
#     1_yr_rank_chg: 0,
#     1_yr_rating_chg: +1,
#     total_games: 1030,
#     total_h_games: 364,
#     total_a_games: 331,
#     total_n_games: 335,
#     total_wins: 657,
#     total_losses: 162,
#     total_draws: 211,
#     total_goals_scored: 2237,
#     total_goals_conceded: 914
# }
