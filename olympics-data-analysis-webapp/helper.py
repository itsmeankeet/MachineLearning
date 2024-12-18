import numpy as np

def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()
    medal_tally['total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']
    return medal_tally


def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')
    countries = np.unique(df['region'].dropna().values).tolist()
    countries.sort()
    countries.insert(0, 'Overall')
    return years, countries

def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if(year == 'Overall' and country == 'Overall'):
        temp_df = medal_df
    if(year == 'Overall' and country != 'Overall'):
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if(year != 'Overall' and country == 'Overall'):
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if(year != 'Overall' and country != 'Overall'):
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]
    if(flag == 1): 
        temp_df = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year', ascending=True).reset_index()
    else:
        temp_df = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()
    temp_df['total'] = temp_df['Gold'] + temp_df['Silver'] + temp_df['Bronze']
    return temp_df

def data_over_time(df, col):
    nations_over_time = df.drop_duplicates(['Year',col])['Year'].value_counts().reset_index().sort_values('Year')
    nations_over_time.rename(columns={'Year':'Edition', col:'count'}, inplace=True)
    return nations_over_time

def most_successful(df, sport):
    """Returns DataFrame of most successful athletes by medal count for a given sport"""
    # Filter for valid medals and sport
    temp_df = df[df['Medal'].notna()]
    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]
    
    # Group and count medals
    medals = temp_df.groupby(['Name', 'region', 'Sport'])['Medal'].count().reset_index()
    medals = medals.sort_values('Medal', ascending=False)
    medals.columns = ['Name', 'Region', 'Sport', 'Medals']
    # Add index column starting from 0
    medals = medals.reset_index(drop=True)
    # Return top 10 athletes
    return medals.head(15)