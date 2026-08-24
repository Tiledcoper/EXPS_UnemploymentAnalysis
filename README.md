# 📊 Unemployment Analysis with Python

> **An end-to-end data analysis project exploring unemployment trends, regional differences, labour-market relationships, and the impact of COVID-19 in India.**

---

## 🚀 Project Overview

This project focuses on analyzing unemployment data in India and turning raw data into meaningful insights using **Python**.

The project combines **data cleaning, exploratory data analysis, statistical comparisons, interactive visualization, and dashboard development** to better understand how unemployment changed across time and regions.

We also developed an interactive **Streamlit dashboard** that makes it easier to explore the results and compare different states and area types.

---

## 🎯 What We Did

### 🧹 Data Cleaning & Preparation

The dataset was first cleaned and prepared for analysis.

The preprocessing included:

- Cleaning and standardizing column names
- Converting dates and numerical columns to the correct data types
- Removing duplicate records
- Handling missing values in required fields
- Creating additional time-based features such as `Year`, `Month`, `Month_Name`, and `Period`
- Splitting the data into **Pre-COVID** and **COVID period**

This created a cleaner and more reliable dataset for the analysis.

---

## 🔎 Exploratory Data Analysis

The analysis explores unemployment from several different perspectives.

### 📈 Unemployment Trends

We examined how the average unemployment rate changed over time, looking for major increases, decreases, and turning points.

### 🗺️ Regional Analysis

States and regions were compared based on their average unemployment rates to identify areas with relatively higher unemployment.

### 🏙️ Rural vs Urban

We compared **Rural** and **Urban** unemployment levels using statistical summaries and distribution plots to understand differences between the two area types.

### 📅 Monthly Patterns

Monthly averages were analyzed to identify possible recurring patterns in unemployment across the available period.

### 🔗 Labour-Market Relationships

We explored the relationship between:

- Unemployment Rate
- Estimated Employed
- Labour Participation Rate

using correlation analysis and interactive visualizations.

---

## 🦠 COVID-19 Impact Analysis

One of the main objectives of the project was to investigate the change in unemployment around the COVID-19 period.

We compared **Pre-COVID** and **COVID-period** observations using:

- Average unemployment
- Median unemployment
- Minimum and maximum values
- Number of observations
- Change in percentage points
- Relative percentage change

The analysis showed a significant increase in unemployment during the COVID period, while also demonstrating that the impact varied across regions.

> **Note:** This is an observational comparison and does not prove that COVID-19 alone caused the observed changes.

---

## 📊 Data Visualization

To make the analysis easier to understand, we used **Plotly** to build several interactive visualizations, including:

- 📈 Time-series line charts
- 📊 State-level ranking charts
- 📦 Box plots
- 📅 Monthly unemployment charts
- 🔗 Correlation heatmaps
- 🫧 Animated labour-market scatter plots

The animated visualization shows the relationship between labour participation and unemployment while using bubble size to represent estimated employment and animation to show changes over time.

---

## 🌐 Interactive Streamlit Dashboard

The project was extended into an interactive **Streamlit dashboard** to allow users to explore the analysis without running the notebook manually.

The dashboard includes:

### 🎛️ Interactive Filters
Users can filter the analysis by:

- States / regions
- Area type

### 📌 Key Performance Indicators

The dashboard displays:

- Average unemployment
- Median unemployment
- Average employed
- Labour participation
- Peak unemployment observation

### 📑 Dashboard Sections

| Section | Description |
|---|---|
| 📈 Trends | Explore unemployment changes over time |
| 🦠 COVID-19 | Compare unemployment before and during COVID-19 |
| 🗺️ Regional | Compare states and Rural vs Urban areas |
| 🔎 Relationships | Explore labour-market relationships |
| 💡 Insights | Display calculated findings and policy-oriented insights |

The dashboard also allows users to download analytical tables as CSV files.

---

## 💡 Key Insights

The analysis highlights several important observations:

- Unemployment changed significantly throughout the analyzed period.
- Some regions experienced considerably higher unemployment than others.
- Rural and Urban areas showed different unemployment patterns.
- Unemployment increased substantially during the COVID period.
- The impact of the COVID period was not uniform across all states.
- Labour participation and employment provide additional context when interpreting unemployment trends.

---

## 🛠️ Technologies Used

**Python** 🐍  
**Pandas** · **NumPy** · **Plotly** · **Streamlit**  
**Jupyter Notebook** · **VS Code**

---

## 📂 Project Structure

```text
Unemployment-Analysis/
│
├── 📓 Unemployme.ipynb
├── 🌐 app_unemployment.py
├── 📊 Unemployment in India.csv
├── 📋 requirements.txt
└── 📖 README.md
```

---

## 📦 Installation & Usage

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard:

```bash
streamlit run app_unemployment.py
```

Make sure the CSV dataset is placed in the same directory as the application.

To explore the full analysis, open:

```text
Unemployme.ipynb
```

---

## 🔮 Future Improvements

Some possible extensions for the project include:

- Adding unemployment forecasting
- Applying Machine Learning models
- Including more recent unemployment data
- Adding geographical maps
- Expanding the historical time period
- Deploying the Streamlit dashboard online

---

## 📌 Conclusion

This project demonstrates a complete **data analysis workflow**, starting from raw unemployment data and ending with an interactive analytical dashboard.

By combining **data cleaning, exploratory analysis, visualization, and interactive tools**, the project provides a clear view of unemployment trends and regional differences in India, while highlighting the major changes observed during the COVID-19 period.

**Built with Python 🐍 · Pandas · NumPy · Plotly · Streamlit**
