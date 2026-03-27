import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
import requests
import yfinance as yf

# data={
#     "Name": ["Alice","Bob","Avirup"],
#     "Age": [25,30,28]
# }

# df = pd.DataFrame(data)

# st.dataframe(df)
# st.table(df)

# # st.title("Streamlit Basics")
# # st.header("This is a header")
# # st.subheader("This is a subheader")
# # st.text("This is a plain text")
# # st.markdown("**Markdown** _is_ supported")

# # st.text_input("Whats your name?")

# # if st.button("Click Me!"):
# #     st.write("Button was clicked!")

# name = st.text_input("Enter Your Name")
# if name:
#     st.write(f"Hello, {name}")

# age = st.slider("Select your age:",0,100,25)
# st.write(f"You are {age} years old.")


# number = st.number_input("Enter Your Number", min_value=0, max_value=100, value=5)
# st.write(f"You Chose, {number}")

# option = st.selectbox("Choose your favorite fruit", ("Apple", "Banana", "Cherry"))
# st.write(f"You selected: {option}")

# choices = st.multiselect("Choose your favorite color", ["Red", "Blue", "Yellow"], default="Red")
# st.write(f"You selected: {choices}")

# upload_file = st.file_uploader("Choose a CSV file", type="csv")
# if upload_file is not None:
#     df = pd.read_csv(upload_file)
#     st.write(df.head(10))


# st.write("BMI Calculator!")

# height = st.number_input("Enter your height(inch):", min_value=12, max_value=84, value=60)
# weight = st.number_input("Enter your weight(pound):", min_value=10, max_value=500, value=200)

# if st.button("Calculate BMI"):
#     bmi = ((weight/(height **2))*703)
#     st.write(f"Your BMI is {bmi:.2f}")

#     if bmi < 18.5:
#         st.warning("Underweight")
#     elif 18.5 <= bmi < 25:
#         st.success("Normal Weight")
#     elif 25 <= bmi < 30: 
#         st.warning("Overweight")
#     else:
#         st.error("Obse")

# st.title("Main Area")
# st.write("This is the main content of the app.")

# # Sidebar
# st.sidebar.title("Sidebar Menu")
# username = st.sidebar.text_input("Enter you name:")
# option = st.sidebar.selectbox("Choose a category:", ["News", "Sports", "Tech"])

# if username:
#     st.sidebar.write(f"Hello, {username}!")

# col1, col2 = st.columns(2)

# with col1:
#     st.header("Column 1")
#     st.write("Content for Column 1")

# with col2:
#     st.header("Column 2")
#     st.write("Content for Column 2")

# # col1, col2, col3 = st.column(3,1,2)

# with st.expander("See more details:"):
#     st.write("Here you can add extra information")

# # Sample data
# chart_data = pd.DataFrame(
#     np.random.randn(10, 3),
#     columns=["A", "B", "C"])

# st.line_chart(chart_data)
# st.area_chart(chart_data)
# st.bar_chart(chart_data)

# # MatPlotLib graph
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
# ax.set_title("Matplotlib Line Chart")
# st.pyplot(fig)


# # Plotly Express
# df = pd.DataFrame({
#     "Fruit": ["Apple", "Banana", "Orange", "Apple", "Banana", "Orange"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["NY", "NY", "NY", "LA", "LA", "LA"]
# })
# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
# st.plotly_chart(fig)


# # Altair Chart
# df = pd.DataFrame({
#     'x': range(1, 11),
#     'y': [x**2 for x in range(1, 11)]
# })
# chart = alt.Chart(df).mark_line().encode(
#     x='x',
#     y='y')
# st.altair_chart(chart, use_container_width=True)

# # Mini Project
# st.title("COVID-19 Live Cases Dashboard")
# @st.cache_data
# def load_data():
#     url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
#     response = requests.get(url)
#     data = response.json()
#     df = pd.DataFrame({
#         "date": list(data["cases"].keys()),
#         "cases": list(data["cases"].values()),
#         "deaths": list(data["deaths"].values()),
#         "recovered": list(data["recovered"].values())
#     })

#     return df

# df = load_data()

# # Plot cases over time
# fig = px.line(df, x="date", y=["cases", "deaths", "recovered"],
#               title="Global COVID-19 Cases Over Time")
# st.plotly_chart(fig, use_container_width=True)



# # 1. Loading CSV Files
# # The simplest way to load data in Streamlit is using Pandas.


# # df = pd.read_csv("sample.csv")
# # st.write(df.head())  # Display first 5 rows

# # # 2. Loading Excel Files
# # df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# # st.write(df)

# # Make sure to install openpyxl:
# # pip install openpyxl

# # Loading Data from an API
# def get_bitcoin_price():
#     url = "https://api.coingecko.com/api/v3/simple/price"
#     params = {"ids": "bitcoin", "vs_currencies": "usd"}
#     resp = requests.get(url, params=params, timeout=10)

#     if resp.ok:
#         data = resp.json()
#         return data["bitcoin"]["usd"]
#     else:
#         st.error(f"API error: {resp.status_code}")
#         return None
# st.subheader("💰 Live Bitcoin Price")

# price = get_bitcoin_price()
# if price:
#     st.success(f"Current BTC Price: ${price:,.2f}")



# #  User File Upload
# uploaded_file = st.file_uploader("Choose a CSV file", type=["csv", "xlsx"])
# if uploaded_file is not None:
#     if uploaded_file.name.endswith("csv"):
#         df = pd.read_csv(uploaded_file)
#     else:
#         df = pd.read_excel(uploaded_file)
#     st.write(df.head())

# # 5. Filtering Data
# # Example: Filter by category
# category = st.selectbox("Select Category", df["units_sold"].unique())
# filtered_df = df[df["units_sold"] == category]
# st.write(filtered_df)

# # 6. Allow Users to Download Data
# csv = df.to_csv(index=False).encode("utf-8")
# st.download_button(
#     label="Download data as CSV",
#     data=csv,
#     file_name="data.csv",
#     mime="text/csv",
# )

 

# # 7. Mini Project – Stock Price Viewer
# # Goal: Allow users to select a stock, fetch recent price data from Yahoo Finance, and download it as CSV.

# st.title("Stock Price Viewer")
# # User selects stock
# ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, MSFT):", "AAPL")

# if st.button("Get Data"):
#     stock = yf.Ticker(ticker)
#     df = stock.history(period="1mo")  # 1 month data
#     st.line_chart(df["Close"])
 

#     # Download option
#     csv = df.to_csv().encode("utf-8")
#     st.download_button(
#         label="Download CSV",
#         data=csv,
#         file_name=f"{ticker}_data.csv",
#         mime="text/csv"
#     )



# # Understanding st.session_state
# # Think of it like a global memory box for your app.
# # You can: Initialize values (st.session_state["counter"] = 0)
# # Read them (st.session_state.counter)
# # Update them on interaction

# st.title("Counter Demo")

# # Initialize state
# if "count" not in st.session_state:
#     st.session_state.count = 0

# # Buttons to modify state
# if st.button("Increment"):
#     st.session_state.count += 1
 
# if st.button("Decrement"):
#     st.session_state.count -= 1

# st.write("Current Count:", st.session_state.count)
# # Unlike normal variables, this counter won’t reset every time you click a button.


# # Using State with Widgets
# # You can directly bind widgets to session_state.

# st.title("Session State with Widgets")
# st.text_input("Enter your name:", key="username")
# st.slider("Select age:", 0, 100, key="age")

# st.write("Hello,", st.session_state.username, "!")
# st.write("Your age is:", st.session_state.age)

# # Here, username and age values stay persistent even if you interact with other widgets.

 

# # 4. Callbacks with State
# # Callbacks let you run a function when a widget changes.


# st.title("Callback Example")

# def reset_age():
#     st.session_state.age1 = 18
# st.number_input("Enter age:", min_value=0, max_value=100, key="age1")
# st.button("Reset Age", on_click=reset_age)
# st.write("Current Age:", st.session_state.age1)


# # 5. Forms with State
# # Forms group widgets together.
# # They prevent reruns until the submit button is clicked.
# # Combined with session state → stable input handling.

st.title("Form Example")

with st.form("user_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.session_state["user"] = {"name": name, "age": age}
    st.success(f"Saved: {name}, {age} years old")

if "user" in st.session_state:
    st.write("Stored User:", st.session_state["user"])



# Mini Project – Simple Chat App
# Goal: Build a chatbox where messages persist instead of resetting.


st.title("Simple Chat App")

# Initialize messages list in session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input form
with st.form("chat_form"):
    msg = st.text_input("Enter a message:")
    send = st.form_submit_button("Send")

# Append new message if submitted
if send and msg:
    st.session_state.messages.append(msg)

# Display chat history
st.subheader("Chat History")
for i, m in enumerate(st.session_state.messages, 1):
    st.write(f"{i}. {m}")


# Tools for Optimization:
# Caching Data → @st.cache_data
@st.cache_data
def load_data():
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    return pd.read_csv(url)
df = load_data()  # Now it's cached 
st.write(df.head())

# Prevents reloading data every rerun.
# Caching Computations → @st.cache_resource

import time
@st.cache_resource
def expensive_function(x):
    time.sleep(3)  # simulate heavy computation
    return x * x
st.write("Square:", expensive_function(10))


# Combining Forms + Callbacks + Caching
# Mini example: Search App

@st.cache_data
def load_data():
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    return pd.read_csv(url)

df = load_data()

st.title("Flight Data Search")

with st.form("search_form"):
    month = st.selectbox("Select Month", df["Month"].unique())
    submit = st.form_submit_button("Search")

if submit:
    st.write("Flights in", month)
    st.dataframe(df[df["Month"] == month])
# Only searches when "Submit" is clicked. Data loaded once via cache



# Mini Project – To-Do List App
# Let’s combine everything:
st.title("To-Do List")
# Initialize state
if "tasks" not in st.session_state:
    st.session_state.tasks = []
 
# Form to add tasks
with st.form("task_form"):
    task = st.text_input("New Task")
    add = st.form_submit_button("Add Task")

if add and task:
    st.session_state.tasks.append(task)

# Display tasks with delete buttons
for i, t in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4,1])
    col1.write(t)
    if col2.button("X", key=f"del_{i}"):
        st.session_state.tasks.pop(i)
        st.rerun()



# Sales Dashboard
# Goal:
# An interactive dashboard where users can: 
# Select year & region. View KPIs (total sales, profit, customers). See sales trends & top products

st.set_page_config(page_title="Sales Dashboard", layout="wide")
# Sample dataset (replace with real sales data)
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/yannie28/Global-Superstore/master/Global_Superstore(CSV).csv"
    return pd.read_csv(url)

df = load_data()

 

# Sidebar filters
st.sidebar.header("Filters")
year = st.sidebar.selectbox("Select Year", sorted(df['Order Date'].str[:4].unique()))
region = st.sidebar.multiselect("Select Region", df['Region'].unique(), default=df['Region'].unique())


# Filter data
filtered_df = df[(df['Order Date'].str[:4] == year) & (df['Region'].isin(region))]

# KPIs
total_sales = int(filtered_df["Sales"].sum())
total_profit = int(filtered_df["Profit"].sum())
total_customers = filtered_df["Customer ID"].nunique()

st.title("Sales Dashboard")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Sales", f"${total_sales:,}")
kpi2.metric("Total Profit", f"${total_profit:,}")
kpi3.metric("Unique Customers", total_customers)

 

st.markdown("---")

# Charts
col1, col2 = st.columns([2, 1])

with col1:
    sales_trend = filtered_df.groupby(filtered_df["Order Date"].str[:7])["Sales"].sum().reset_index()
    fig = px.line(sales_trend, x="Order Date", y="Sales", title="Monthly Sales Trend")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    top_products = filtered_df.groupby("Product Name")["Sales"].sum().nlargest(5).reset_index()
    fig = px.bar(top_products, x="Sales", y="Product Name", orientation="h", title="Top 5 Products")
    st.plotly_chart(fig, use_container_width=True)