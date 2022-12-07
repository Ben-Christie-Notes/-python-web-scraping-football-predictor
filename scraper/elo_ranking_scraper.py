from selenium import webdriver
from selenium.webdriver.common.by import By

def get_data():
  driver = webdriver.Chrome()
  driver.implicitly_wait(10)
  driver.get('https://www.eloratings.net/')

  team_data = driver.find_elements(By.CLASS_NAME, 'ui-widget-content')

  driver.close()
  
  return team_data

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

def clean_data(arr):
  # clean data
  for i, _ in enumerate(arr):
    if i == 5 or i == 6:
      if len(arr[i]) > 1:
        arr[i] = arr[i].replace('+', '')
        # change minus to hyphen (look the same but aren't)
        arr[i] = arr[i].replace('−', '-')
      
      arr[i] = int(arr[i])
    elif i != 1:
      arr[i] = int(arr[i])

def create_dict(arr):
  # create a dictionary
  team_dict = {
    'rank': arr[0],
    'name': arr[1],
    'rating': arr[2],
    'avg_rank': arr[3],
    'avg_rating': arr[4],
    '1_yr_rank_chg': arr[5],
    '1_yr_rating_chg': arr[6],
    'total_games': arr[7],
    'total_home_games': arr[8],
    'total_away_games': arr[9],
    'total_neutral_games': arr[10],
    'total_wins': arr[11],
    'total_losses': arr[12],
    'total_draws': arr[13],
    'total_goals_scored': arr[14],
    'total_goals_conceded': arr[15]
  }

  return team_dict


def prep_data():
  team_dictionaries = []
  team_data = get_data()

  for team in team_data:
    arr = team.text.split('\n')
    clean_data(arr)

    team_dict = create_dict(arr)
    
    team_dictionaries.append(team_dict)
  
  return team_dictionaries
