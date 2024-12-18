import streamlit as st
import pandas as pd 
import preprocessor
import helper
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df, region_df)

st.sidebar.title("Olympics Analysis")
user_menu = st.sidebar.radio("Select an Option",
                 (
                     'Medal Tally',
                     'Overall Analysis',
                     'Country-wise Analysis',
                     'Athlete-wise Analysis',
                 )
                )
if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years, countries = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", countries)

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title(f"Medal Tally in {selected_year}")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(f"Overall Medal Tally of {selected_country}")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(f"Medal Tally of {selected_country} in {selected_year}")
    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]
    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Cities")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col3:
        st.header("Athletes")
        st.title(athletes)
    with col2:
        st.header("Nations")
        st.title(nations)

    nations_over_time = helper.data_over_time(df,'region')
    nations_over_time.rename(columns={'count':'No of Nations'}, inplace=True)
    st.title("Participation Over Time")
    # Create an interactive line chart using Plotly Express
    # px.line creates a line plot with:
    # - nations_over_time dataframe as the data source
    # - Year values on x-axis 
    # - count values on y-axis
    # The resulting chart allows zooming, panning, and hovering for data points
    fig = px.line(nations_over_time, x="Edition", y="No of Nations") 
    # Display the interactive Plotly chart in the Streamlit app
    st.plotly_chart(fig)

    st.title("Events over the years")
    events_over_time = helper.data_over_time(df,'Event')
    events_over_time.rename(columns={'count':'No of Events'}, inplace=True)
    fig = px.line(events_over_time, x="Edition", y="No of Events")
    st.plotly_chart(fig)

    st.title("Athletes over the years")
    athletes_over_time = helper.data_over_time(df,'Name')
    athletes_over_time.rename(columns={'count':'No of Athletes'}, inplace=True)
    fig = px.line(athletes_over_time, x="Edition", y="No of Athletes")
    st.plotly_chart(fig)

    st.title("Sports over the years")
    sports_over_time = helper.data_over_time(df,'Sport')
    sports_over_time.rename(columns={'count':'No of Sports'}, inplace=True)
    fig = px.line(sports_over_time, x="Edition", y="No of Sports")
    st.plotly_chart(fig)

    st.title("No of Events over time(Every Sport)")
    fig,ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year','Sport','Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int), annot=True)
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox("Select a Sport", sport_list)
    x = helper.most_successful(df, selected_sport)
    st.table(x)
