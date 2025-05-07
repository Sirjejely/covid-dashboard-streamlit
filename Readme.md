COVID-19 Data App 📊
This project visualizes and analyzes COVID-19 data using Python. It was initially developed in a Jupyter Notebook, then later converted into a .py file for deployment using Streamlit.

🔧 Project Workflow
🧪 Phase 1: Development in Jupyter Notebook
Import Libraries

pandas, numpy, matplotlib, seaborn, plotly.express, streamlit

Load the Dataset

Read a cleaned CSV file using pandas.read_csv().

Example:

df = pd.read_csv('covid_data.csv')
Explore the Dataset

Checked for missing values using df.isnull().sum()

Previewed data with df.head() and checked data types.

Data Cleaning (if needed)

Removed/filled null values.

Renamed or selected relevant columns for analysis.

Data Analysis

Calculated descriptive statistics (df.describe())

Grouped data by country, date, or region.

Data Visualization

Created charts using:

Matplotlib/Seaborn for static plots.

Plotly Express for interactive plots.

Tested Visualization Outputs

Ensured plots were readable and provided insights (e.g., confirmed cases vs deaths).

🖥️ Phase 2: Deploying with Streamlit
Create a New Python File

Copied the working code from Jupyter Notebook to a new file called covid_app.py.

Refactor for Streamlit

Added Streamlit functions such as:
import streamlit as st
st.title("COVID-19 Dashboard")
st.sidebar.selectbox("Select a Country", country_list)
st.plotly_chart(fig)
Used st.cache_data() for performance optimization.

Tested Locally
Ran the app in terminal using:
             streamlit run covid_app.py
Fixed Streamlit Not Found Error

Added Python and Scripts path to environment variables (e.g., C:\Users\YourUser\AppData\Roaming\Python\PythonXX\Scripts)

Verified with:
where streamlit
Re-ran the App

Verified that the browser opened automatically and rendered interactive charts.

💻 How to Run This App
Clone the repository:
    git clone https://github.com/your-username/covid19-app.git
cd covid19-app
Install dependencies:
          pip install -r requirements.txt
Run the Streamlit app:
                    streamlit run covid_app.py
📁 Folder Structure
Copy   
Edit
covid19-app/
├── covid_data.csv
├── covid_app.py
├── notebook_dev.ipynb
├── requirements.txt
└── README.md