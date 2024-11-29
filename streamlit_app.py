import streamlit as st
import pandas as pd
import json

# Define the path to your JSON file
json_file_path = "data/ratings.json"

# Read the JSON file into a DataFrame
def read_json_to_dataframe(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return pd.DataFrame(data)

# Write the DataFrame back to the JSON file
def write_dataframe_to_json(dataframe, file_path):
    with open(file_path, "w") as file:
        json.dump(dataframe.to_dict(orient="records"), file, indent=2)

# Main Streamlit app
st.title("Recipe Editor")

# Load the data into a DataFrame
df = read_json_to_dataframe(json_file_path)

# Display the DataFrame in Streamlit's data_editor
edited_df = st.data_editor(df, num_rows="dynamic")

# Button to save changes
if st.button("Save Changes"):
    write_dataframe_to_json(edited_df, json_file_path)
    st.success("Changes saved to the JSON file!")
