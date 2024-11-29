import streamlit as st
import pandas as pd
import json
import numpy as np
import re

# Define the path to your JSON file
json_file_path = "data/ratings.json"

# Read the JSON file into a DataFrame
def read_json_to_dataframe(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return pd.DataFrame(data)

# Write the DataFrame back to the JSON file
def write_dataframe_to_json(dataframe, file_path):
    # Replace NaN with empty string to ensure valid JSON
    dataframe = dataframe.replace({np.nan: ""})
    with open(file_path, "w") as file:
        json.dump(dataframe.to_dict(orient="records"), file, indent=2)

def prettify_column_name(column_name):
    return re.sub(r'(_)', ' ', column_name).title()

# Main Streamlit app
st.title("Recipe Editor")

# Load the data into a DataFrame
df = read_json_to_dataframe(json_file_path)

# Ensure 'rating' column can handle blanks
if 'rating' in df.columns:
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Display the DataFrame in Streamlit's data_editor
prettified_columns = [re.sub(r'(_)', ' ', col).title() for col in df.columns]
edited_df = st.data_editor(df, num_rows="dynamic", columns=prettified_columns)

# Button to save changes
if st.button("Save Changes"):
    write_dataframe_to_json(edited_df, json_file_path)
    st.success("Changes saved to the JSON file!")
