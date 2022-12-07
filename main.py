# import prep_data function
from scraper.elo_ranking_scraper import prep_data

import pandas as pd

team_data = prep_data()

df = pd.DataFrame(team_data)
df.set_index('rank', inplace = True)


