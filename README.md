# **Project Boeing - Flight Operations Dashboard** ✈️

## 📋 **Overview**
This repository contains a **Flight Operations Dashboard** developed as a Proof of Concept (PoC) for analyzing flight delays and operational bottlenecks. The application provides an interactive web interface to explore flight data, visualize the main causes of delays, and identify critical areas for operational optimization. 

This project was built using Python and Streamlit to showcase data analysis and visualization skills.

## 📊 **Dataset**
The data used in this project is based on the **Airline Delay Causes** dataset, which is publicly available on [Kaggle](https://www.kaggle.com/datasets/giovamata/airlinedelaycauses?resource=download). 

For the purpose of this PoC and to ensure optimal performance and fast loading times in the Streamlit application, the original dataset has been reduced to a sample of **100,000 rows**.

## 🚀 **Features**
- **Interactive Filtering:** Select a specific airline to dynamically update all metrics and charts.
- **Key Performance Indicators (KPIs):** Quick overview of the *Total Flights* and *Average Delay* for the selected carrier.
- **Delay Analysis Visualizations:**
  - **Causes of Delay:** A bar chart showing the distribution of delayed flights by cause (Carrier, Weather, NAS, Security, Late Aircraft).
  - **Weekly Trends:** A line chart displaying the evolution of average delays throughout the week to identify critical days.
  - **Geographical Bottlenecks:** A bar chart highlighting the Top 5 origin airports with the highest average delays.

## 💻 **Technologies Used**
- **Python 3**
- **Pandas:** For data manipulation, filtering, and aggregation.
- **Streamlit:** For building the interactive web application interface.

## 📁 **Repository Structure**
```
├── 📁 data
│   └── 📄 DelayedFlights_reduce.csv
├── 📝 README.md
├── 🐍 app.py
└── 📄 requirements.txt
```

## 🛠️ **Installation & Usage**
To run this application locally on your machine, follow these steps:  
 1. Clone the repository:
 ```bash
 git clone https://github.com/Nathan-Houel/Project_Boeing
 cd Project_Boeing
 ```

 2. Install the required dependencies:  
Make sure you have Python installed. Then, install the required libraries:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:  
Execute the following command in your terminal:
```bash
streamlit run app.py
```
The dashboard will automatically open in your default web browser (usually at `http://localhost:8501`).


## 👤 **Author**
**Nathan Houel** - *February 2026*