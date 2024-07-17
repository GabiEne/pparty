
import streamlit as st
import pandas as pd

# Load the data from the specific sheet
data = pd.read_excel(r'C:\Users\gabri\Desktop\infinit\adstream 2022\pparties\BD_GabiDOBRITA.xlsx', sheet_name='0, Baza de date_iunie 2024')

# Extract unique localities from the 'Valori' column
localities = data['Valori'].unique()

st.title('Vote Analysis by Locality and Political Party')

# Locality selection
selected_locality = st.selectbox('Select Locality', localities)

# Filter data based on selected locality
filtered_data = data[data['Valori'] == selected_locality]

# Extract unique political parties
political_parties = filtered_data.columns[2:]  # Assuming first two columns are locality and another identifier

# Political party selection
selected_party = st.selectbox('Select Political Party', political_parties)

# Display the number of votes for the selected political party
votes = filtered_data[selected_party].sum()

st.write(f'Total votes for {selected_party} in {selected_locality}: {votes}')
