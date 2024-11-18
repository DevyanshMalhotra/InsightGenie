# InsightGenie: AI Agent Dashboard

InsightGenie is a versatile AI-powered tool designed to extract, analyze, and retrieve specific information from datasets (CSV or Google Sheets) using dynamic queries. With integrated search capabilities and advanced response generation, InsightGenie simplifies data extraction and enhances productivity.

![Dashboard Interface](https://github.com/DevyanshMalhotra/InsightGenie/raw/main/images/image1.png)

---

## 🌟 Features

1. **File Upload and Google Sheets Integration**:
   - Upload CSV files or connect Google Sheets using the Google Sheets API.
   - Preview data and select columns for queries.

2. **Dynamic Query Input**:
   - Define custom queries with placeholders like `{entity}` for dynamic replacements.

3. **Automated Web Search**:
   - Perform web searches for entities using dynamically generated queries.
   - Extract relevant information from search results.

4. **AI-Powered Contextual Responses**:
   - Use Hugging Face's FLAN-T5 to generate focused, context-aware responses.

5. **Results Visualization and Export**:
   - Display extracted results in a table format.
   - Download the results as a CSV file.

---

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **APIs**:
  - Google Sheets API
  - Hugging Face Transformers
- **Search Capability**: Web scraping with BeautifulSoup
- **Libraries**: Pandas, Requests, Transformers, Streamlit

---

## 📂 Project Structure

InsightGenie/
├── app.py                 # Main application script  
├── requirements.txt       # List of dependencies  
├── utils/                 # Utility scripts  
│   ├── google_sheets.py   # Google Sheets integration  
│   ├── google_search.py   # Web search logic  
│   ├── llm_handler.py     # AI model interaction  
├── service_account.json   # Google API credentials (gitignored)  
├── README.md              # Project documentation  
├── data/                  # Example CSV files  
           

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/DevyanshMalhotra/InsightGenie.git
cd insightgenie
```

### 2. Install Dependencies
Install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Setup Google API Credentials
- Create a service account in your Google Cloud Console.
- Download the JSON key file and save it as `service_account.json` in the project root.
- Share your Google Sheet with the service account email (Editor permission).

### 4. Run the Application
Start the Streamlit dashboard:

```bash
streamlit run app.py
```

### 5. Access the Dashboard
- Open the URL provided by Streamlit in your browser.
- Upload a CSV file or connect a Google Sheet to begin.

---

## 📝 Usage Instructions

### Upload Data:
- Choose either a CSV file or a Google Sheet.
- Preview the uploaded data in the dashboard.

### Define Queries:
- Select the primary column for entities.
- Enter a dynamic query template (e.g., `Find the {query_column} for {entity}`).

### Run Queries:
- Perform automated searches or extract information directly from the dataset.
- View extracted information in the dashboard.

### Download Results:
- Export the results as a CSV file for further use.

---

## 📸 Screenshots

- **Dashboard Interface**
- **Results Table**

---

## 🛡️ API Key Management

### Google Sheets:
- Store the service account credentials in `service_account.json`. Ensure the file is listed in `.gitignore`.

### Environment Variables:
- Use environment variables for sensitive data like API keys for deployment.

---

## 🎥 Demo Video

Watch the project walkthrough [here](#).

---

## 🌐 Deployment

Deploy the project for free using Streamlit Cloud:

1. Push your repository to GitHub.
2. Sign up for Streamlit Cloud.
3. Connect your repository and deploy the app.

---

## 📢 Acknowledgments

- **Hugging Face Transformers** for LLM capabilities.
- **Google Sheets API** for seamless data integration.
- **BeautifulSoup** for web scraping.
- **Streamlit** for building an interactive UI.

---

## 🧩 FAQ

**Q: What happens if an entity isn't found in the dataset?**  
A: The application performs an automated web search for missing entities and uses the AI model to generate responses.

**Q: How are large datasets handled?**  
A: Data is processed in batches to ensure scalability and prevent timeouts.

**Q: Can additional features be added?**  
A: Yes! The modular structure allows for easy integration of new features such as batch queries or advanced error handling.
```

This version is fully formatted in Markdown and ready for your `README.md`.
