import streamlit as st
import pandas as pd 
import preprocessor
import helper

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