import streamlit as st
from data_fetcher import fetch_train_data
from data_parser import parse_train_data
import pandas as pd
import time

# Set the title of the app
st.title("Real-Time Train Schedule - Circumvesuviana")
data_placeholder = st.empty()

# Initialize a variable to hold the DataFrame
train_data_df = pd.DataFrame()

# Function to update the train schedule
def update_schedule():
    global train_data_df  # Use the global variable
    while True:
        # Fetch data from the API
        raw_data = fetch_train_data()
        
        # Check if the data is not None or empty
        if raw_data:
            # Parse the data
            new_data = parse_train_data(raw_data)
            if not new_data.empty:
                # Update the existing DataFrame in place
                train_data_df = new_data
                with data_placeholder.container():
                    st.dataframe(train_data_df)  # Show the updated DataFrame
            else:
                with data_placeholder.container():
                    st.write("Nessun dato disponibile.")

        # Wait for 30 seconds before refreshing
        time.sleep(10)

# Call the function to update the schedule
update_schedule()
