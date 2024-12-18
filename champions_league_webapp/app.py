import streamlit as st
import pandas as pd
import helper

df = pd.read_csv('pldatas.csv')

user_menu = st.sidebar.radio("Select an Option", 
                    (
                        'League Table Overview',
                        'Clubwise Stats',
                        'Playerwise Stats',
                        'Seasonwise Stats',
                        'Countrywise Stats'
                    )
                )
if user_menu == 'League Table Overview':
    years = helper.get_teams(df)
    years = [year - 1 for year in years]  # Add 1 to each year
    st.sidebar.title("League Table Overview ")
    selected_year = st.sidebar.selectbox("Select The Year", years)
    st.title(f'Premier League Standing of {selected_year}')
    table_df = helper.return_table(df, selected_year + 1)  # Subtract 1 to match original data
    st.table(table_df)