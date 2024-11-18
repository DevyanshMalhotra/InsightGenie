import streamlit as st
import pandas as pd
from utils.google_sheets import connect_google_sheet
from utils.google_search import google_search
from utils.llm_handler import generate_response_with_context

st.title("InsightGenie:AI Agent Dashboard")
st.write("Welcome! Upload a CSV file or connect to a Google Sheet to get started.")

upload_option = st.radio("Select Input Method", ["CSV File", "Google Sheet"])
df = None  # Initialize df to avoid undefined reference

if upload_option == "CSV File":
    file = st.file_uploader("Upload your CSV file", type=["csv"])
    if file:
        try:
            df = pd.read_csv(file)
            st.success("File uploaded successfully!")
            st.write("Preview of Uploaded Data:")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error reading file: {e}")

elif upload_option == "Google Sheet":
    sheet_url = st.text_input("Enter Google Sheet URL")
    if sheet_url:
        try:
            df = connect_google_sheet(sheet_url)
            st.success("Google Sheet connected successfully!")
            st.write("Preview of Google Sheet Data:")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Failed to connect to Google Sheet: {e}")

# Ensure df is defined before showing further options
if df is not None:
    selected_column = st.selectbox("Select the primary column for queries:", df.columns)
    query_column = st.selectbox("Select the column to query:", df.columns)

    query_template = st.text_input("Enter your query template (e.g., 'Find {query_column} for {entity}'):")    

    if st.button("Run Query"):
        if selected_column and query_column:
            results = []
            entity_to_find = query_template.split("for")[-1].strip()

            for _, row in df.iterrows():
                entity = row[selected_column]

                if str(entity_to_find).lower() in str(entity).lower():
                    if query_column in df.columns:
                        response = f"The {query_column} for {entity_to_find} is {row[query_column]}"
                    else:
                        response = f"Column '{query_column}' not found in the dataset."
                    results.append({"Entity": entity, "Response": response})
                    break
            else:
                st.warning(f"'{entity_to_find}' not found in the dataset. Searching online...")
                dynamic_query = query_template.replace("{entity}", entity_to_find).replace("{query_column}", query_column)
                search_results = google_search(dynamic_query)
                response = generate_response_with_context(entity_to_find, query_template, " ".join(search_results))
                results.append({"Entity": entity_to_find, "Response": response})

            if results:
                results_df = pd.DataFrame(results)
                st.write("Extracted Information:")
                st.dataframe(results_df)
                st.download_button(
                    label="Download Results as CSV",
                    data=results_df.to_csv(index=False),
                    file_name="extracted_information.csv",
                    mime="text/csv",
                )
            else:
                st.warning("No valid data found to process!")
else:
    st.warning("Please upload a CSV file or connect to a Google Sheet to proceed.")
