def get_teams(df):
    years = df['season_end_year'].unique().tolist()
    years.sort()
    return years

def return_table(df,end_year):
    table = df[df['season_end_year'] == end_year]
    table = table.reset_index(drop=True)
    table.index = table.index + 1
    table = table[['team','played', 'won','drawn','lost', 'gd', 'points']]
    return table